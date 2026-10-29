// 메인 ComfyUI 페이지에서 실행: 확장 결과(mgsX)로 Qwen-Image-2512 생성 작업을 낸다.
// 먼저 qwen2512_helper.js(mgsQ), consts_v2.js(mgsV2), 확장 실행 코드(runs/expand_v2_*.js 가 mgsX 를 채움)가 올라가 있어야 한다.
// r1 은 확장 프롬프트를 그대로 썼고, 반사실풍으로 나온 캐릭터가 많아 r3 부터 아래 머리말과 부정 프롬프트를 더했다.
window.mgsAnchor = {
  head: "Anime screencap, a single frame from a Japanese TV anime series, cel animation with flat simple colors and minimal soft shading, thin clean black outlines, anime-style faces with large eyes, a small simple nose and smooth simplified skin. ",
  neg: ", semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed",
};
// 손을 숨겨야 하는 컷(니키 1~4, 니키가 함께 나오는 ilia_4·iloke_4·iluki_4)에 덧붙인다
window.mgsNegHands = ", visible hands, fingers, bare hands, hands outside the sleeves";
// 제임스는 1차 나이 묘사가 Qwen 에서 할아버지처럼 나와 설명을 바꾸고 이것을 더했다 (build_v2.py CHAR_OVERRIDE)
window.mgsNegAge = { james: ", elderly, old man, grandfather, deep wrinkles, weathered skin, sagging skin, gray hair, white hair" };
// 컷별 [가로, 세로, 기본 시드, 폴더, 손 숨김] (jobs_v2.json 과 같다)
window.mgsMeta = {"niki_1":[1584,1056,12101,"01_niki",1],"niki_2":[1056,1584,12102,"01_niki",1],"niki_3":[1584,1056,12103,"01_niki",1],"niki_4":[1584,1056,12104,"01_niki",1],"niki_5":[1584,1056,12155,"01_niki",0],"putor_1":[1584,1056,12201,"02_putor",0],"putor_2":[1056,1584,12202,"02_putor",0],"putor_3":[1584,1056,12203,"02_putor",0],"putor_4":[1584,1056,12204,"02_putor",0],"putor_5":[1584,1056,12205,"02_putor",0],"quillins_1":[1584,1056,12301,"03_quillins",0],"quillins_2":[1056,1584,12302,"03_quillins",0],"quillins_3":[1056,1584,12353,"03_quillins",0],"quillins_4":[1584,1056,12354,"03_quillins",0],"quillins_5":[1328,1328,12355,"03_quillins",0],"james_1":[1584,1056,12401,"04_james",0],"james_2":[1056,1584,12402,"04_james",0],"james_3":[1584,1056,12403,"04_james",0],"james_4":[1584,1056,12404,"04_james",0],"james_5":[1056,1584,12405,"04_james",0],"beth_1":[1584,1056,12501,"05_beth",0],"beth_2":[1056,1584,12502,"05_beth",0],"beth_3":[1584,1056,12503,"05_beth",0],"beth_4":[1584,1056,12504,"05_beth",0],"beth_5":[1056,1584,12505,"05_beth",0],"taoba_1":[1584,1056,12601,"06_taoba",0],"taoba_2":[1056,1584,12602,"06_taoba",0],"taoba_3":[1584,1056,12603,"06_taoba",0],"taoba_4":[1584,1056,12604,"06_taoba",0],"taoba_5":[1056,1584,12605,"06_taoba",0],"ilia_1":[1584,1056,12701,"07_ilia",0],"ilia_2":[1056,1584,12702,"07_ilia",0],"ilia_3":[1584,1056,12703,"07_ilia",0],"ilia_4":[1584,1056,12704,"07_ilia",1],"ilia_5":[1056,1584,12705,"07_ilia",0],"iloke_1":[1584,1056,12801,"08_iloke",0],"iloke_2":[1056,1584,12802,"08_iloke",0],"iloke_3":[1584,1056,12803,"08_iloke",0],"iloke_4":[1584,1056,12804,"08_iloke",1],"iloke_5":[1056,1584,12805,"08_iloke",0],"iluki_1":[1584,1056,12901,"09_iluki",0],"iluki_2":[1056,1584,12902,"09_iluki",0],"iluki_3":[1584,1056,12903,"09_iluki",0],"iluki_4":[1584,1056,12904,"09_iluki",1],"iluki_5":[1584,1056,12905,"09_iluki",0]};
// ids: 컷 이름 목록, rnd: 회차 폴더, ks: 후보 번호 (시드 = 기본 시드 + 1000*k)
window.mgsGen2 = async (ids, rnd, ks = [0], steps = 30) => {
  const jobs = [];
  for (const id of ids) {
    const x = mgsX[id], m = mgsMeta[id], ch = id.split("_")[0];
    for (const k of ks) jobs.push({ prefix: `niki_compass_v2/${m[3]}/${rnd}/${id}_s${m[2] + 1000 * k}`, w: m[0], h: m[1],
      seed: m[2] + 1000 * k, steps, text: mgsAnchor.head + x.prompt,
      negative: mgsV2.N + mgsAnchor.neg + (m[4] ? mgsNegHands : "") + (mgsNegAge[ch] || "") });
  }
  return mgsQ.submit(jobs);
};
"mgsGen2 ready";
