// 메인 ComfyUI 와 같은 주소(작업공간 포트)의 아무 페이지에서 실행: final 폴더 45장을 한 화면에 모아 보여 준다.
// 이미지는 로그인 쿠키로 /api/view 에서 바로 읽으므로 같은 주소에서 열어야 한다.
(() => {
  const DATE_DIR = "main/2026-10-27/niki_compass/final";
  const CHARS = [
    ["01_niki", "니키 그린", ["niki_1_turnaround", "niki_2_keypose", "niki_3_expressions", "niki_4_forest_magic", "niki_5_sleeve_growth"]],
    ["02_putor", "푸토르", ["putor_1_turnaround", "putor_2_keypose", "putor_3_expressions", "putor_4_healing", "putor_5_props"]],
    ["03_quillins", "퀼린스", ["quillins_1_hooded_turnaround", "quillins_2_night_shore", "quillins_3_reveal_portrait", "quillins_4_seal", "quillins_5_glove"]],
    ["04_james", "제임스 그린", ["james_1_turnaround", "james_2_keypose", "james_3_expressions", "james_4_greenhouse", "james_5_doorframe"]],
    ["05_beth", "베스 그린", ["beth_1_turnaround", "beth_2_tea", "beth_3_expressions", "beth_4_greenhouse", "beth_5_protect"]],
    ["06_taoba", "타오바", ["taoba_1_turnaround", "taoba_2_keypose", "taoba_3_expressions", "taoba_4_greenhouse", "taoba_5_vines"]],
    ["07_ilia", "일리아", ["ilia_1_turnaround", "ilia_2_keypose", "ilia_3_expressions", "ilia_4_ribbon", "ilia_5_greenhouse"]],
    ["08_iloke", "일로케", ["iloke_1_turnaround", "iloke_2_handkerchief", "iloke_3_expressions", "iloke_4_umbrella", "iloke_5_pots"]],
    ["09_iluki", "일루키", ["iluki_1_turnaround", "iluki_2_keypose", "iluki_3_expressions", "iluki_4_toys", "iluki_5_scolded"]],
  ];
  const url = (dir, name) => `/api/view?filename=${encodeURIComponent(name + "_00001_.png")}&subfolder=${encodeURIComponent(DATE_DIR + "/" + dir)}&type=output`;
  const sections = CHARS.map(([dir, title, names]) => `
    <section><h2>${title}</h2><div class="row">
      ${names.map(n => `<a href="${url(dir, n)}" target="_blank"><figure><img loading="lazy" src="${url(dir, n)}"><figcaption>${n}</figcaption></figure></a>`).join("")}
    </div></section>`).join("");
  document.open();
  document.write(`<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>니키와 이상한 나침반 · 최종 컨셉아트</title>
    <style>
      body { margin: 0; padding: 16px; background: #f4efe4; color: #2b2622; font: 14px/1.5 system-ui, sans-serif; }
      h1 { font-size: 20px; margin: 0 0 4px; } p { margin: 0 0 16px; color: #6b6158; }
      h2 { font-size: 16px; margin: 20px 0 8px; border-bottom: 1px solid #d8cfc0; padding-bottom: 4px; }
      .row { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 8px; }
      figure { margin: 0; background: #fffaf2; border: 1px solid #e0d6c6; border-radius: 6px; overflow: hidden; }
      img { width: 100%; height: 120px; object-fit: contain; background: #fff; display: block; }
      figcaption { font-size: 11px; padding: 4px 6px; color: #6b6158; word-break: break-all; }
      a { color: inherit; text-decoration: none; }
    </style></head><body>
    <h1>니키와 이상한 나침반 · 등장인물 컨셉아트 (최종 45장)</h1>
    <p id="where"></p>
    ${sections}</body></html>`);
  document.close();
  document.getElementById("where").textContent =
    "\\\\192.168.10.29\\results\\admin\\" + DATE_DIR.split("/").join("\\") + " · 그림을 누르면 원본 크기로 열립니다.";
})();
// 이미지 보기 화면(/api/view)에서는 document.write 가 막히므로, /mgs/api/me 같은 일반 페이지를 연 뒤 실행한다.
