// 메인 ComfyUI(작업공간 페이지)에서 실행: Z-Image Turbo 작업을 허브 대기열로 보낸다.
// 같은 주소(작업공간 포트)에서 로그인 쿠키로 /api/prompt 를 부르므로 허브의 접수 절차(검증·환경 고정·기록)를 그대로 거친다.
window.mgsZ = {
  api(j) {
    return {
      "66": { class_type: "UNETLoader", inputs: { unet_name: "z_image_turbo_bf16.safetensors", weight_dtype: "default" } },
      "62": { class_type: "CLIPLoader", inputs: { clip_name: "qwen_3_4b.safetensors", type: "lumina2", device: "default" } },
      "63": { class_type: "VAELoader", inputs: { vae_name: "ae.safetensors" } },
      "69": { class_type: "ModelSamplingAuraFlow", inputs: { model: ["66", 0], shift: 3, sampling: "flow" } },
      "67": { class_type: "CLIPTextEncode", inputs: { clip: ["62", 0], text: j.text } },
      "71": { class_type: "CLIPTextEncode", inputs: { clip: ["62", 0], text: j.negative } },
      "68": { class_type: "EmptySD3LatentImage", inputs: { width: j.w, height: j.h, batch_size: 1 } },
      "70": { class_type: "KSampler", inputs: { model: ["69", 0], positive: ["67", 0], negative: ["71", 0], latent_image: ["68", 0],
              seed: j.seed, steps: 8, cfg: 1, sampler_name: "res_multistep", scheduler: "simple", denoise: 1 } },
      "65": { class_type: "VAEDecode", inputs: { samples: ["70", 0], vae: ["63", 0] } },
      "9": { class_type: "SaveImage", inputs: { images: ["65", 0], filename_prefix: j.prefix } },
    };
  },
  // 결과 PNG 에 들어갈 화면용 워크플로우 (ComfyUI 에 끌어다 놓으면 그대로 열림)
  ui(j) {
    const N = (id, type, pos, size, order, inputs, outputs, widgets) => ({ id, type, pos, size, flags: {}, order, mode: 0,
      inputs, outputs, properties: { "Node name for S&R": type }, widgets_values: widgets });
    const I = (name, type, link) => ({ name, type, link });
    const O = (name, type, links) => ({ name, type, links });
    return {
      last_node_id: 71, last_link_id: 82,
      nodes: [
        N(66, "UNETLoader", [-240, 110], [380, 82], 0, [], [O("MODEL", "MODEL", [72])], ["z_image_turbo_bf16.safetensors", "default"]),
        N(62, "CLIPLoader", [-240, 420], [340, 106], 1, [], [O("CLIP", "CLIP", [79, 81])], ["qwen_3_4b.safetensors", "lumina2", "default"]),
        N(63, "VAELoader", [660, 700], [320, 58], 2, [], [O("VAE", "VAE", [74])], ["ae.safetensors"]),
        N(69, "ModelSamplingAuraFlow", [220, 110], [310, 82], 3, [I("model", "MODEL", 72)], [O("MODEL", "MODEL", [75])], [3, "flow"]),
        N(67, "CLIPTextEncode", [170, 290], [410, 160], 4, [I("clip", "CLIP", 79)], [O("CONDITIONING", "CONDITIONING", [76])], [j.text]),
        N(71, "CLIPTextEncode", [170, 520], [410, 140], 5, [I("clip", "CLIP", 81)], [O("CONDITIONING", "CONDITIONING", [82])], [j.negative]),
        N(68, "EmptySD3LatentImage", [310, 700], [260, 106], 6, [], [O("LATENT", "LATENT", [78])], [j.w, j.h, 1]),
        N(70, "KSampler", [660, 320], [315, 262], 7, [I("model", "MODEL", 75), I("positive", "CONDITIONING", 76),
          I("negative", "CONDITIONING", 82), I("latent_image", "LATENT", 78)], [O("LATENT", "LATENT", [73])],
          [j.seed, "fixed", 8, 1, "res_multistep", "simple", 1]),
        N(65, "VAEDecode", [1020, 320], [225, 46], 8, [I("samples", "LATENT", 73), I("vae", "VAE", 74)], [O("IMAGE", "IMAGE", [80])], []),
        N(9, "SaveImage", [1280, 320], [300, 420], 9, [I("images", "IMAGE", 80)], [], [j.prefix]),
      ],
      links: [[72, 66, 0, 69, 0, "MODEL"], [73, 70, 0, 65, 0, "LATENT"], [74, 63, 0, 65, 1, "VAE"], [75, 69, 0, 70, 0, "MODEL"],
              [76, 67, 0, 70, 1, "CONDITIONING"], [78, 68, 0, 70, 3, "LATENT"], [79, 62, 0, 67, 0, "CLIP"],
              [80, 65, 0, 9, 0, "IMAGE"], [81, 62, 0, 71, 0, "CLIP"], [82, 71, 0, 70, 2, "CONDITIONING"]],
      groups: [], config: {}, extra: {}, version: 0.4,
    };
  },
  async submit(jobs) {
    const out = [];
    for (const j of jobs) {
      const body = { prompt: this.api(j), client_id: "mgs-concept-batch", extra_data: { extra_pnginfo: { workflow: this.ui(j) } } };
      const r = await fetch("/api/prompt", { method: "POST", credentials: "same-origin",
        headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
      const d = await r.json().catch(() => ({}));
      out.push({ prefix: j.prefix, status: r.status, id: d.prompt_id, number: d.number,
                 err: d.error ? (d.error.message || d.error.type) : (Object.keys(d.node_errors || {}).length ? d.node_errors : undefined) });
      (window.mgsJobs = window.mgsJobs || []).push({ prefix: j.prefix, id: d.prompt_id });
    }
    return out;
  },
  // 작업 상태와 결과 파일 (허브의 /api/jobs, /api/history)
  async status(ids) {
    const res = [];
    for (const id of ids) {
      const j = await (await fetch(`/api/jobs/${id}`, { cache: "no-store" })).json().catch(() => ({}));
      let files = [];
      if (j.status === "completed") {
        const h = await (await fetch(`/api/history/${id}`, { cache: "no-store" })).json().catch(() => ({}));
        for (const o of Object.values((h[id] || {}).outputs || {})) {
          for (const im of o.images || []) files.push(`${im.subfolder}/${im.filename}`);
        }
      }
      res.push({ id, status: j.status, err: j.execution_error ? j.execution_error.exception_message : undefined, files });
    }
    return res;
  },
};
"mgsZ ready";
