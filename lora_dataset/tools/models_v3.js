// 메인 ComfyUI 페이지에서 실행: 같은 프롬프트를 생성 모델 4개로 보낸다 (설정은 각 모델의 공식 템플릿 기준).
// 결과 PNG 에는 화면용 워크플로우를 넣어, ComfyUI 에 끌어다 놓으면 같은 설정으로 열린다.
window.mgsM = {
  // 노드별 입력 이름·형식, 출력 형식, 위젯 순서 (화면용 워크플로우를 만들 때 쓴다)
  SPEC: {
    UNETLoader: { ins: [], out: ["MODEL"], w: (i) => [i.unet_name, i.weight_dtype] },
    CLIPLoader: { ins: [], out: ["CLIP"], w: (i) => [i.clip_name, i.type, i.device] },
    VAELoader: { ins: [], out: ["VAE"], w: (i) => [i.vae_name] },
    ModelSamplingAuraFlow: { ins: [["model", "MODEL"]], out: ["MODEL"], w: (i) => [i.shift] },
    CLIPTextEncode: { ins: [["clip", "CLIP"]], out: ["CONDITIONING"], w: (i) => [i.text] },
    ConditioningZeroOut: { ins: [["conditioning", "CONDITIONING"]], out: ["CONDITIONING"], w: () => [] },
    EmptySD3LatentImage: { ins: [], out: ["LATENT"], w: (i) => [i.width, i.height, i.batch_size] },
    EmptyLatentImage: { ins: [], out: ["LATENT"], w: (i) => [i.width, i.height, i.batch_size] },
    EmptyFlux2LatentImage: { ins: [], out: ["LATENT"], w: (i) => [i.width, i.height, i.batch_size] },
    KSampler: { ins: [["model", "MODEL"], ["positive", "CONDITIONING"], ["negative", "CONDITIONING"], ["latent_image", "LATENT"]],
      out: ["LATENT"], w: (i) => [i.seed, "fixed", i.steps, i.cfg, i.sampler_name, i.scheduler, i.denoise] },
    CFGGuider: { ins: [["model", "MODEL"], ["positive", "CONDITIONING"], ["negative", "CONDITIONING"]], out: ["GUIDER"], w: (i) => [i.cfg] },
    Flux2Scheduler: { ins: [], out: ["SIGMAS"], w: (i) => [i.steps, i.width, i.height] },
    KSamplerSelect: { ins: [], out: ["SAMPLER"], w: (i) => [i.sampler_name] },
    RandomNoise: { ins: [], out: ["NOISE"], w: (i) => [i.noise_seed, "fixed"] },
    SamplerCustomAdvanced: { ins: [["noise", "NOISE"], ["guider", "GUIDER"], ["sampler", "SAMPLER"], ["sigmas", "SIGMAS"], ["latent_image", "LATENT"]],
      out: ["LATENT", "LATENT"], w: () => [] },
    VAEDecode: { ins: [["samples", "LATENT"], ["vae", "VAE"]], out: ["IMAGE"], w: () => [] },
    SaveImage: { ins: [["images", "IMAGE"]], out: [], w: (i) => [i.filename_prefix] },
  },
  MODELS: {
    // 1차와 같은 Z-Image Turbo 구성
    zimage_turbo: (j) => ({
      "1": { class_type: "UNETLoader", inputs: { unet_name: "z_image_turbo_bf16.safetensors", weight_dtype: "default" } },
      "2": { class_type: "CLIPLoader", inputs: { clip_name: "qwen_3_4b.safetensors", type: "lumina2", device: "default" } },
      "3": { class_type: "VAELoader", inputs: { vae_name: "ae.safetensors" } },
      "4": { class_type: "ModelSamplingAuraFlow", inputs: { model: ["1", 0], shift: 3 } },
      "5": { class_type: "CLIPTextEncode", inputs: { clip: ["2", 0], text: j.text } },
      "6": { class_type: "CLIPTextEncode", inputs: { clip: ["2", 0], text: j.negative } },
      "7": { class_type: "EmptySD3LatentImage", inputs: { width: j.w, height: j.h, batch_size: 1 } },
      "8": { class_type: "KSampler", inputs: { model: ["4", 0], positive: ["5", 0], negative: ["6", 0], latent_image: ["7", 0],
             seed: j.seed, steps: 8, cfg: 1, sampler_name: "res_multistep", scheduler: "simple", denoise: 1 } },
      "9": { class_type: "VAEDecode", inputs: { samples: ["8", 0], vae: ["3", 0] } },
      "10": { class_type: "SaveImage", inputs: { images: ["9", 0], filename_prefix: j.prefix } },
    }),
    // 공식 템플릿 image_flux2_klein_text_to_image 의 증류판 경로 (4 steps, cfg 1, 부정 조건은 0)
    flux2_klein_4b: (j) => ({
      "1": { class_type: "UNETLoader", inputs: { unet_name: "flux-2-klein-4b.safetensors", weight_dtype: "default" } },
      "2": { class_type: "CLIPLoader", inputs: { clip_name: "qwen_3_4b.safetensors", type: "flux2", device: "default" } },
      "3": { class_type: "VAELoader", inputs: { vae_name: "flux2-vae.safetensors" } },
      "4": { class_type: "CLIPTextEncode", inputs: { clip: ["2", 0], text: j.text } },
      "5": { class_type: "ConditioningZeroOut", inputs: { conditioning: ["4", 0] } },
      "6": { class_type: "CFGGuider", inputs: { model: ["1", 0], positive: ["4", 0], negative: ["5", 0], cfg: 1 } },
      "7": { class_type: "EmptyFlux2LatentImage", inputs: { width: j.w, height: j.h, batch_size: 1 } },
      "8": { class_type: "Flux2Scheduler", inputs: { steps: 4, width: j.w, height: j.h } },
      "9": { class_type: "KSamplerSelect", inputs: { sampler_name: "euler" } },
      "10": { class_type: "RandomNoise", inputs: { noise_seed: j.seed } },
      "11": { class_type: "SamplerCustomAdvanced", inputs: { noise: ["10", 0], guider: ["6", 0], sampler: ["9", 0], sigmas: ["8", 0], latent_image: ["7", 0] } },
      "12": { class_type: "VAEDecode", inputs: { samples: ["11", 0], vae: ["3", 0] } },
      "13": { class_type: "SaveImage", inputs: { images: ["12", 0], filename_prefix: j.prefix } },
    }),
    // 공식 템플릿 image_qwen_Image_2512 기본 경로 (시간 때문에 50 → 20 steps, cfg 4)
    qwen_image_2512: (j) => ({
      "1": { class_type: "UNETLoader", inputs: { unet_name: "qwen_image_2512_fp8_e4m3fn.safetensors", weight_dtype: "default" } },
      "2": { class_type: "CLIPLoader", inputs: { clip_name: "qwen_2.5_vl_7b_fp8_scaled.safetensors", type: "qwen_image", device: "default" } },
      "3": { class_type: "VAELoader", inputs: { vae_name: "qwen_image_vae.safetensors" } },
      "4": { class_type: "ModelSamplingAuraFlow", inputs: { model: ["1", 0], shift: 3.1 } },
      "5": { class_type: "CLIPTextEncode", inputs: { clip: ["2", 0], text: j.text } },
      "6": { class_type: "CLIPTextEncode", inputs: { clip: ["2", 0], text: j.negative } },
      "7": { class_type: "EmptySD3LatentImage", inputs: { width: j.w, height: j.h, batch_size: 1 } },
      "8": { class_type: "KSampler", inputs: { model: ["4", 0], positive: ["5", 0], negative: ["6", 0], latent_image: ["7", 0],
             seed: j.seed, steps: 20, cfg: 4, sampler_name: "euler", scheduler: "simple", denoise: 1 } },
      "9": { class_type: "VAEDecode", inputs: { samples: ["8", 0], vae: ["3", 0] } },
      "10": { class_type: "SaveImage", inputs: { images: ["9", 0], filename_prefix: j.prefix } },
    }),
    // 공식 템플릿 image_krea2_turbo_t2i (8 steps, cfg 1, 부정 조건은 0, 템플릿의 그림체 LoRA 는 쓰지 않음)
    krea2_turbo: (j) => ({
      "1": { class_type: "UNETLoader", inputs: { unet_name: "krea2_turbo_fp8_scaled.safetensors", weight_dtype: "default" } },
      "2": { class_type: "CLIPLoader", inputs: { clip_name: "qwen3vl_4b_fp8_scaled.safetensors", type: "krea2", device: "default" } },
      "3": { class_type: "VAELoader", inputs: { vae_name: "qwen_image_vae.safetensors" } },
      "5": { class_type: "CLIPTextEncode", inputs: { clip: ["2", 0], text: j.text } },
      "6": { class_type: "ConditioningZeroOut", inputs: { conditioning: ["5", 0] } },
      "7": { class_type: "EmptyLatentImage", inputs: { width: j.w, height: j.h, batch_size: 1 } },
      "8": { class_type: "KSampler", inputs: { model: ["1", 0], positive: ["5", 0], negative: ["6", 0], latent_image: ["7", 0],
             seed: j.seed, steps: 8, cfg: 1, sampler_name: "euler", scheduler: "simple", denoise: 1 } },
      "9": { class_type: "VAEDecode", inputs: { samples: ["8", 0], vae: ["3", 0] } },
      "10": { class_type: "SaveImage", inputs: { images: ["9", 0], filename_prefix: j.prefix } },
    }),
  },
  ui(api) {
    const ids = Object.keys(api).map(Number).sort((a, b) => a - b);
    const nodes = [], links = [], outLinks = {};
    let lid = 0;
    ids.forEach((id, order) => {
      const n = api[id], spec = this.SPEC[n.class_type];
      const inputs = spec.ins.map(([name, type], slot) => {
        const src = n.inputs[name];
        links.push([++lid, Number(src[0]), src[1], id, slot, type]);
        (outLinks[`${src[0]}:${src[1]}`] = outLinks[`${src[0]}:${src[1]}`] || []).push(lid);
        return { name, type, link: lid };
      });
      nodes.push({ id, type: n.class_type, pos: [(order % 5) * 380, Math.floor(order / 5) * 300], size: [340, n.class_type === "CLIPTextEncode" ? 200 : 100],
        flags: {}, order, mode: 0, inputs, outputs: [], properties: { "Node name for S&R": n.class_type }, widgets_values: spec.w(n.inputs) });
    });
    for (const node of nodes) node.outputs = this.SPEC[node.type].out.map((type, slot) => ({ name: type, type, links: outLinks[`${node.id}:${slot}`] || [] }));
    return { last_node_id: Math.max(...ids), last_link_id: lid, nodes, links, groups: [], config: {}, extra: {}, version: 0.4 };
  },
  async submit(model, jobs) {
    const out = [];
    for (const j of jobs) {
      const api = this.MODELS[model](j);
      const body = { prompt: api, client_id: "mgs-lora-v3", extra_data: { extra_pnginfo: { workflow: this.ui(api) } } };
      const r = await fetch("/api/prompt", { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
      const d = await r.json().catch(() => ({}));
      out.push({ model, id: j.id, prefix: j.prefix, status: r.status, pid: d.prompt_id, err: d.error ? (d.error.message || d.error.type) : (Object.keys(d.node_errors || {}).length ? d.node_errors : undefined) });
    }
    (window.mgsV3Log = window.mgsV3Log || []).push(...out);
    return out;
  },
  async status(pids) {
    const res = [];
    for (const pid of pids) {
      const j = await (await fetch(`/api/jobs/${pid}`, { cache: "no-store" })).json().catch(() => ({}));
      let file;
      if (j.status === "completed") {
        const h = await (await fetch(`/api/history/${pid}`, { cache: "no-store" })).json().catch(() => ({}));
        const im = Object.values((h[pid] || {}).outputs || {}).flatMap(o => o.images || [])[0];
        file = im && `${im.subfolder}/${im.filename}`;
      }
      res.push({ pid, status: j.status, file, err: j.execution_error && j.execution_error.exception_message });
    }
    return res;
  },
};
"mgsM ready";
