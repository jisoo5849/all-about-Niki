// 메인 ComfyUI(작업공간 페이지)에서 실행: Qwen-Image-2512 작업을 허브 대기열로 보낸다.
// 공식 템플릿 image_qwen_Image_2512 의 구성(qwen_2.5_vl_7b 인코더, qwen_image_vae, AuraFlow shift 3.1)을 따른다.
// j.fast 가 true 면 같은 템플릿의 Lightning 4-step LoRA 경로(4 steps, cfg 1), 아니면 기본 경로(50 steps, cfg 4)다.
window.mgsQ = {
  // 노드 종류별 입력 이름·형식과 위젯 순서 (결과 PNG 에 넣을 화면용 워크플로우를 만들 때 쓴다)
  SPEC: {
    UNETLoader: { ins: [], out: ["MODEL"], w: (i) => [i.unet_name, i.weight_dtype] },
    CLIPLoader: { ins: [], out: ["CLIP"], w: (i) => [i.clip_name, i.type, i.device] },
    VAELoader: { ins: [], out: ["VAE"], w: (i) => [i.vae_name] },
    LoraLoaderModelOnly: { ins: [["model", "MODEL"]], out: ["MODEL"], w: (i) => [i.lora_name, i.strength_model] },
    ModelSamplingAuraFlow: { ins: [["model", "MODEL"]], out: ["MODEL"], w: (i) => [i.shift] },
    CLIPTextEncode: { ins: [["clip", "CLIP"]], out: ["CONDITIONING"], w: (i) => [i.text] },
    EmptySD3LatentImage: { ins: [], out: ["LATENT"], w: (i) => [i.width, i.height, i.batch_size] },
    KSampler: { ins: [["model", "MODEL"], ["positive", "CONDITIONING"], ["negative", "CONDITIONING"], ["latent_image", "LATENT"]],
      out: ["LATENT"], w: (i) => [i.seed, "fixed", i.steps, i.cfg, i.sampler_name, i.scheduler, i.denoise] },
    VAEDecode: { ins: [["samples", "LATENT"], ["vae", "VAE"]], out: ["IMAGE"], w: () => [] },
    SaveImage: { ins: [["images", "IMAGE"]], out: [], w: (i) => [i.filename_prefix] },
  },
  api(j) {
    const fast = !!j.fast;
    const g = {
      "1": { class_type: "UNETLoader", inputs: { unet_name: "qwen_image_2512_fp8_e4m3fn.safetensors", weight_dtype: "default" } },
      "2": { class_type: "CLIPLoader", inputs: { clip_name: "qwen_2.5_vl_7b_fp8_scaled.safetensors", type: "qwen_image", device: "default" } },
      "3": { class_type: "VAELoader", inputs: { vae_name: "qwen_image_vae.safetensors" } },
      "5": { class_type: "ModelSamplingAuraFlow", inputs: { model: fast ? ["4", 0] : ["1", 0], shift: 3.1 } },
      "6": { class_type: "CLIPTextEncode", inputs: { clip: ["2", 0], text: j.text } },
      "7": { class_type: "CLIPTextEncode", inputs: { clip: ["2", 0], text: j.negative || "" } },
      "8": { class_type: "EmptySD3LatentImage", inputs: { width: j.w, height: j.h, batch_size: 1 } },
      "9": { class_type: "KSampler", inputs: { model: ["5", 0], positive: ["6", 0], negative: ["7", 0], latent_image: ["8", 0],
             seed: j.seed, steps: fast ? 4 : (j.steps || 50), cfg: fast ? 1 : (j.cfg || 4), sampler_name: "euler", scheduler: "simple", denoise: 1 } },
      "10": { class_type: "VAEDecode", inputs: { samples: ["9", 0], vae: ["3", 0] } },
      "11": { class_type: "SaveImage", inputs: { images: ["10", 0], filename_prefix: j.prefix } },
    };
    if (fast) g["4"] = { class_type: "LoraLoaderModelOnly", inputs: { model: ["1", 0],
      lora_name: "Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors", strength_model: 1 } };
    return g;
  },
  // API 그래프를 화면용 워크플로우로 바꾼다 (ComfyUI 에 끌어다 놓으면 그대로 열림)
  ui(api) {
    const ids = Object.keys(api).map(Number).sort((a, b) => a - b);
    const nodes = [], links = [];
    const outLinks = {};
    let linkId = 0;
    ids.forEach((id, order) => {
      const n = api[id], spec = this.SPEC[n.class_type];
      const inputs = spec.ins.map(([name, type]) => {
        const src = n.inputs[name];
        const lid = ++linkId;
        links.push([lid, Number(src[0]), src[1], id, spec.ins.findIndex((x) => x[0] === name), type]);
        (outLinks[`${src[0]}:${src[1]}`] = outLinks[`${src[0]}:${src[1]}`] || []).push(lid);
        return { name, type, link: lid };
      });
      nodes.push({ id, type: n.class_type, pos: [(order % 4) * 420, Math.floor(order / 4) * 320], size: [380, n.class_type === "CLIPTextEncode" ? 200 : 110],
        flags: {}, order, mode: 0, inputs, outputs: [], properties: { "Node name for S&R": n.class_type }, widgets_values: spec.w(n.inputs) });
    });
    for (const node of nodes) {
      node.outputs = this.SPEC[node.type].out.map((type, slot) => ({ name: type, type, links: outLinks[`${node.id}:${slot}`] || [] }));
    }
    return { last_node_id: Math.max(...ids), last_link_id: linkId, nodes, links, groups: [], config: {}, extra: {}, version: 0.4 };
  },
  async submit(jobs) {
    const out = [];
    for (const j of jobs) {
      const api = this.api(j);
      const body = { prompt: api, client_id: "mgs-concept-v2", extra_data: { extra_pnginfo: { workflow: this.ui(api) } } };
      const r = await fetch("/api/prompt", { method: "POST", credentials: "same-origin",
        headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
      const d = await r.json().catch(() => ({}));
      out.push({ prefix: j.prefix, status: r.status, id: d.prompt_id,
                 err: d.error ? (d.error.message || d.error.type) : (Object.keys(d.node_errors || {}).length ? d.node_errors : undefined) });
      (window.mgsQJobs = window.mgsQJobs || []).push({ prefix: j.prefix, id: d.prompt_id, seed: j.seed });
    }
    return out;
  },
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
"mgsQ ready";
