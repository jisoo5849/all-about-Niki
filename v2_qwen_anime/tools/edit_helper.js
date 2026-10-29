// 메인 ComfyUI(작업공간 페이지)에서 실행: 고른 결과 이미지를 Qwen-Image-Edit-2511 로 부분 수정한다.
// 공식 템플릿 image_qwen_image_edit_2511 의 구성을 그대로 따르고, Lightning 4-step LoRA 경로(4 steps, cfg 1)를 쓴다.
// Z-Image Turbo 는 '손을 소매 속에 숨긴' 동작을 글로만 시키면 손을 그려 버려서, 구도가 좋은 컷의 소매만 고친다.
window.mgsEdit = {
  // 결과 폴더의 PNG 를 이 작업공간의 입력 폴더로 올린다 (실행 접수 때 허브가 입력 파일을 고정한다).
  async upload(subfolder, filename, newName) {
    const src = `/api/view?filename=${encodeURIComponent(filename)}&subfolder=${encodeURIComponent(subfolder)}&type=output`;
    const blob = await (await fetch(src, { credentials: "same-origin" })).blob();
    const fd = new FormData();
    fd.append("image", new File([blob], newName, { type: "image/png" }));
    fd.append("overwrite", "true");
    fd.append("type", "input");
    const r = await fetch("/api/upload/image", { method: "POST", body: fd, credentials: "same-origin" });
    return { status: r.status, body: await r.json().catch(() => null), bytes: blob.size };
  },
  api(j) {
    return {
      "1": { class_type: "UNETLoader", inputs: { unet_name: "qwen_image_edit_2511_fp8mixed.safetensors", weight_dtype: "default" } },
      "2": { class_type: "CLIPLoader", inputs: { clip_name: "qwen_2.5_vl_7b_fp8_scaled.safetensors", type: "qwen_image", device: "default" } },
      "3": { class_type: "VAELoader", inputs: { vae_name: "qwen_image_vae.safetensors" } },
      "4": { class_type: "ModelSamplingAuraFlow", inputs: { model: ["1", 0], shift: 3.1 } },
      "5": { class_type: "CFGNorm", inputs: { model: ["4", 0], strength: 1, pre_cfg: false } },
      "6": { class_type: "LoraLoaderModelOnly", inputs: { model: ["5", 0], lora_name: "Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors", strength_model: 1 } },
      "7": { class_type: "LoadImage", inputs: { image: j.input } },
      "8": { class_type: "FluxKontextImageScale", inputs: { image: ["7", 0] } },
      "9": { class_type: "TextEncodeQwenImageEditPlus", inputs: { clip: ["2", 0], vae: ["3", 0], image1: ["8", 0], prompt: j.text } },
      "10": { class_type: "TextEncodeQwenImageEditPlus", inputs: { clip: ["2", 0], vae: ["3", 0], image1: ["8", 0], prompt: "" } },
      "11": { class_type: "FluxKontextMultiReferenceLatentMethod", inputs: { conditioning: ["9", 0], reference_latents_method: "index_timestep_zero" } },
      "12": { class_type: "FluxKontextMultiReferenceLatentMethod", inputs: { conditioning: ["10", 0], reference_latents_method: "index_timestep_zero" } },
      "13": { class_type: "VAEEncode", inputs: { pixels: ["8", 0], vae: ["3", 0] } },
      "14": { class_type: "KSampler", inputs: { model: ["6", 0], positive: ["11", 0], negative: ["12", 0], latent_image: ["13", 0],
              seed: j.seed, steps: 4, cfg: 1, sampler_name: "euler", scheduler: "simple", denoise: 1 } },
      "15": { class_type: "VAEDecode", inputs: { samples: ["14", 0], vae: ["3", 0] } },
      // 편집은 약 1MP 에서 일어나므로 원본 크기로 되돌린다
      "16": { class_type: "ImageScale", inputs: { image: ["15", 0], upscale_method: "lanczos", width: j.w, height: j.h, crop: "disabled" } },
      "17": { class_type: "SaveImage", inputs: { images: ["16", 0], filename_prefix: j.prefix } },
    };
  },
  // 결과 PNG 에 넣을 화면용 워크플로우 (ComfyUI 에 끌어다 놓으면 그대로 열림)
  ui(j) {
    const N = (id, type, pos, size, order, inputs, outputs, widgets) => ({ id, type, pos, size, flags: {}, order, mode: 0,
      inputs, outputs, properties: { "Node name for S&R": type }, widgets_values: widgets });
    const I = (name, type, link) => ({ name, type, link });
    const O = (name, type, links) => ({ name, type, links });
    return {
      last_node_id: 17, last_link_id: 22,
      nodes: [
        N(1, "UNETLoader", [-420, 60], [360, 82], 0, [], [O("MODEL", "MODEL", [1])], ["qwen_image_edit_2511_fp8mixed.safetensors", "default"]),
        N(2, "CLIPLoader", [-420, 380], [360, 106], 1, [], [O("CLIP", "CLIP", [5, 6])], ["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default"]),
        N(3, "VAELoader", [-420, 540], [360, 58], 2, [], [O("VAE", "VAE", [7, 8, 9, 10])], ["qwen_image_vae.safetensors"]),
        N(4, "ModelSamplingAuraFlow", [-20, 60], [270, 58], 3, [I("model", "MODEL", 1)], [O("MODEL", "MODEL", [2])], [3.1]),
        N(5, "CFGNorm", [-20, 160], [270, 82], 4, [I("model", "MODEL", 2)], [O("MODEL", "MODEL", [3])], [1, false]),
        N(6, "LoraLoaderModelOnly", [-20, 280], [360, 82], 5, [I("model", "MODEL", 3)], [O("MODEL", "MODEL", [4])],
          ["Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors", 1]),
        N(7, "LoadImage", [-420, 660], [320, 320], 6, [], [O("IMAGE", "IMAGE", [11]), O("MASK", "MASK", null)], [j.input, "image"]),
        N(8, "FluxKontextImageScale", [-60, 660], [270, 30], 7, [I("image", "IMAGE", 11)], [O("IMAGE", "IMAGE", [12, 13, 14])], []),
        N(9, "TextEncodeQwenImageEditPlus", [380, 60], [420, 200], 8,
          [I("clip", "CLIP", 5), I("vae", "VAE", 7), I("image1", "IMAGE", 12), I("image2", "IMAGE", null), I("image3", "IMAGE", null)],
          [O("CONDITIONING", "CONDITIONING", [15])], [j.text]),
        N(10, "TextEncodeQwenImageEditPlus", [380, 300], [420, 160], 9,
          [I("clip", "CLIP", 6), I("vae", "VAE", 8), I("image1", "IMAGE", 13), I("image2", "IMAGE", null), I("image3", "IMAGE", null)],
          [O("CONDITIONING", "CONDITIONING", [16])], [""]),
        N(11, "FluxKontextMultiReferenceLatentMethod", [840, 60], [330, 58], 10, [I("conditioning", "CONDITIONING", 15)],
          [O("CONDITIONING", "CONDITIONING", [17])], ["index_timestep_zero"]),
        N(12, "FluxKontextMultiReferenceLatentMethod", [840, 300], [330, 58], 11, [I("conditioning", "CONDITIONING", 16)],
          [O("CONDITIONING", "CONDITIONING", [18])], ["index_timestep_zero"]),
        N(13, "VAEEncode", [380, 520], [210, 46], 12, [I("pixels", "IMAGE", 14), I("vae", "VAE", 9)], [O("LATENT", "LATENT", [19])], []),
        N(14, "KSampler", [1210, 60], [315, 262], 13, [I("model", "MODEL", 4), I("positive", "CONDITIONING", 17),
          I("negative", "CONDITIONING", 18), I("latent_image", "LATENT", 19)], [O("LATENT", "LATENT", [20])],
          [j.seed, "fixed", 4, 1, "euler", "simple", 1]),
        N(15, "VAEDecode", [1560, 60], [210, 46], 14, [I("samples", "LATENT", 20), I("vae", "VAE", 10)], [O("IMAGE", "IMAGE", [21])], []),
        N(16, "ImageScale", [1560, 160], [270, 130], 15, [I("image", "IMAGE", 21)], [O("IMAGE", "IMAGE", [22])], ["lanczos", j.w, j.h, "disabled"]),
        N(17, "SaveImage", [1860, 60], [320, 360], 16, [I("images", "IMAGE", 22)], [], [j.prefix]),
      ],
      links: [[1, 1, 0, 4, 0, "MODEL"], [2, 4, 0, 5, 0, "MODEL"], [3, 5, 0, 6, 0, "MODEL"], [4, 6, 0, 14, 0, "MODEL"],
              [5, 2, 0, 9, 0, "CLIP"], [6, 2, 0, 10, 0, "CLIP"], [7, 3, 0, 9, 1, "VAE"], [8, 3, 0, 10, 1, "VAE"],
              [9, 3, 0, 13, 1, "VAE"], [10, 3, 0, 15, 1, "VAE"], [11, 7, 0, 8, 0, "IMAGE"], [12, 8, 0, 9, 2, "IMAGE"],
              [13, 8, 0, 10, 2, "IMAGE"], [14, 8, 0, 13, 0, "IMAGE"], [15, 9, 0, 11, 0, "CONDITIONING"],
              [16, 10, 0, 12, 0, "CONDITIONING"], [17, 11, 0, 14, 1, "CONDITIONING"], [18, 12, 0, 14, 2, "CONDITIONING"],
              [19, 13, 0, 14, 3, "LATENT"], [20, 14, 0, 15, 0, "LATENT"], [21, 15, 0, 16, 0, "IMAGE"], [22, 16, 0, 17, 0, "IMAGE"]],
      groups: [], config: {}, extra: {}, version: 0.4,
    };
  },
  async submit(jobs) {
    const out = [];
    for (const j of jobs) {
      const body = { prompt: this.api(j), client_id: "mgs-concept-edit", extra_data: { extra_pnginfo: { workflow: this.ui(j) } } };
      const r = await fetch("/api/prompt", { method: "POST", credentials: "same-origin",
        headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
      const d = await r.json().catch(() => ({}));
      out.push({ prefix: j.prefix, status: r.status, id: d.prompt_id, number: d.number,
                 err: d.error ? (d.error.message || d.error.type) : (Object.keys(d.node_errors || {}).length ? d.node_errors : undefined) });
      (window.mgsJobs = window.mgsJobs || []).push({ prefix: j.prefix, id: d.prompt_id });
    }
    return out;
  },
};
"mgsEdit ready";
