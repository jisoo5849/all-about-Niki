// 메인 ComfyUI(작업공간 페이지)에서 실행: 고른 컷을 결과 폴더의 final/ 아래로 정리한다.
// 후보 PNG 를 입력으로 올린 뒤 LoadImage -> SaveImage 로 다시 저장한다 (픽셀은 그대로, PNG 는 무손실).
// 원본 PNG 에 들어 있던 화면용 워크플로우를 그대로 extra_pnginfo 로 넘겨서,
// final PNG 를 ComfyUI 에 끌어다 놓으면 복사 과정이 아니라 원래 생성(또는 편집) 워크플로우가 열린다.
window.mgsFinal = {
  // PNG tEXt 청크 읽기 (ComfyUI 는 JSON 을 ASCII 로 써서 tEXt 에 넣는다)
  pngText(buf) {
    const u8 = new Uint8Array(buf), dv = new DataView(buf), out = {};
    let p = 8;
    while (p + 8 <= u8.length) {
      const len = dv.getUint32(p), type = String.fromCharCode(...u8.slice(p + 4, p + 8));
      if (type === "tEXt") {
        const data = u8.slice(p + 8, p + 8 + len), z = data.indexOf(0);
        out[new TextDecoder("latin1").decode(data.slice(0, z))] = new TextDecoder("latin1").decode(data.slice(z + 1));
      }
      if (type === "IEND") break;
      p += 12 + len;
    }
    return out;
  },
  // pick = { src: "01_niki/r4_edit/xxx_00001_.png", dest: "01_niki/niki_1" }
  async one(pick, dateDir = "main/2026-10-27/niki_compass") {
    const parts = pick.src.split("/"), fname = parts.pop(), sub = `${dateDir}/${parts.join("/")}`;
    const res = await fetch(`/api/view?filename=${encodeURIComponent(fname)}&subfolder=${encodeURIComponent(sub)}&type=output`);
    const buf = await res.arrayBuffer();
    const meta = this.pngText(buf);
    const inputName = `final_${pick.dest.replace(/\//g, "_")}.png`;
    const fd = new FormData();
    fd.append("image", new File([buf], inputName, { type: "image/png" }));
    fd.append("overwrite", "true");
    fd.append("type", "input");
    const up = await fetch("/api/upload/image", { method: "POST", body: fd, credentials: "same-origin" });
    const prompt = {
      "1": { class_type: "LoadImage", inputs: { image: inputName } },
      "2": { class_type: "SaveImage", inputs: { images: ["1", 0], filename_prefix: `niki_compass/final/${pick.dest}` } },
    };
    const extra = meta.workflow ? { extra_pnginfo: { workflow: JSON.parse(meta.workflow) } } : {};
    const r = await fetch("/api/prompt", { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt, client_id: "mgs-concept-final", extra_data: extra }) });
    const d = await r.json().catch(() => ({}));
    return { dest: pick.dest, upload: up.status, status: r.status, id: d.prompt_id, number: d.number, hasWorkflow: !!meta.workflow,
             err: d.error ? (d.error.message || d.error.type) : undefined };
  },
  async run(picks) {
    const out = [];
    for (const p of picks) out.push(await this.one(p));
    window.mgsFinalJobs = out;
    return out;
  },
  // 결과 PNG 의 API 프롬프트에서 단계 정보를 꺼낸다 (생성: 시드·크기·문장 해시 / 편집: 시드·지시문·입력 파일)
  async info(path, dateDir = "main/2026-10-27/niki_compass") {
    const parts = path.split("/"), fn = parts.pop(), sub = `${dateDir}/${parts.join("/")}`;
    const buf = await (await fetch(`/api/view?filename=${encodeURIComponent(fn)}&subfolder=${encodeURIComponent(sub)}&type=output`)).arrayBuffer();
    const p = JSON.parse(this.pngText(buf).prompt || "{}");
    const fnv = s => { let h = 0x811c9dc5; for (const x of new TextEncoder().encode(s)) { h ^= x; h = Math.imul(h, 0x01000193) >>> 0; } return h.toString(16); };
    if (p["67"] && p["70"]) return { path, kind: "gen", seed: p["70"].inputs.seed, w: p["68"].inputs.width, h: p["68"].inputs.height, hash: fnv(p["67"].inputs.text) };
    const enc = Object.values(p).find(n => n.class_type === "TextEncodeQwenImageEditPlus" && n.inputs.prompt);
    const ks = Object.values(p).find(n => n.class_type === "KSampler");
    const li = Object.values(p).find(n => n.class_type === "LoadImage");
    return { path, kind: "edit", seed: ks && ks.inputs.seed, text: enc && enc.inputs.prompt, input: li && li.inputs.image };
  },
};
"mgsFinal ready";
