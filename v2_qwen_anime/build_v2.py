"""니키와 이상한 나침반 컨셉아트 2차: Qwen-Image-2512 + 다른 애니메이션 그림체.

1차(build_prompts.py, Z-Image Turbo, 2000년대 초 손그림 판타지 장편 계열)의 캐릭터 블록과 컷 구성은 그대로 두고,
그림체 문장·시트 배경·크기·부정 프롬프트만 바꾼다. 같은 인물·같은 컷을 그림체와 모델만 바꿔 비교하려는 것이다.

  python build_v2.py                      ->  jobs_v2.json, inputs_v2_en.md
  python build_v2.py js <캐릭터|컷,...>:<시드 수>:<회차>[:fast|<steps>] [...]
                                          ->  submit_v2_<n>.js (캐릭터별로 나눠 메인 ComfyUI 페이지에 붙여 넣는다,
                                              tools/qwen2512_helper.js 의 mgsQ 가 먼저 올라가 있어야 함)
"""
import json
import sys
from pathlib import Path

OUT = Path(__file__).parent
# 저장소 안(all-about-Niki/v2_qwen_anime)에서는 한 단계 위, 작업 폴더에서는 옆의 all-about-Niki 에 1차 스크립트가 있다
V1 = OUT.parent if (OUT.parent / "build_prompts.py").exists() else OUT.parent / "all-about-Niki"
sys.path.insert(0, str(V1))
import build_prompts as v1  # noqa: E402

# 그림체: 2010년대 후반 일본 극장판 애니메이션 (빛이 많은 사실적 배경 + 선명한 셀 캐릭터)을 특징으로 묘사.
# 1차의 따뜻한 손그림·수채 질감과 겹치지 않게, 선·채색·빛·배경을 모두 반대쪽으로 잡았다.
STYLE = (
    "Modern Japanese theatrical anime film style of the late 2010s: crisp clean line art with thin even dark lines, "
    "polished digital cel shading with two crisp shadow tones and a bright rim light along the edges, "
    "large expressive eyes with layered sparkling highlights, glossy light-catching hair strands, "
    "luminous highly detailed painted backgrounds with dramatic sky light, glowing light particles and soft lens bloom, "
    "vivid saturated colors with cool blue-violet shadows, cinematic depth of field, "
    "original character design."
)
SHEET_BG = "Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions."

# Qwen-Image 기본 경로는 cfg 4 라서 부정 프롬프트가 실제로 듣는다. 1차 그림체(수채·손그림)도 막는다.
NEGATIVE = ("photorealistic, 3d render, cgi, watercolor, gouache, rough sketch, pencil texture, muted faded colors, "
            "text, letters, watermark, logo, signature, blurry, deformed hands, extra fingers, extra arms, extra legs, "
            "extra limbs, missing neck, floating head, duplicate face, merged bodies, cropped feet")
# 손을 숨겨야 하는 컷에만 덧붙인다 (성장 시트 니키 5번은 오른쪽에서 맨손이 나와야 하므로 뺀다)
NEG_HANDS = ", visible hands, fingers, bare hands, hands outside the sleeves"
HIDE_HANDS_EXCEPT = {"niki_5"}

# Qwen-Image 공식 권장 크기 (템플릿 메모: 3:2 1584x1056, 2:3 1056x1584, 1:1 1328x1328)
SIZE = {(1536, 1024): (1584, 1056), (1024, 1536): (1056, 1584), (1024, 1024): (1328, 1328)}
# 이번 작업에서 엉뚱한 그림을 부른 말은 2차에서도 피한다 (silhouette → 사람 모양 그림자)
REPLACE = {"silhouette": "figure"}

# 1차(Z-Image)에서 제임스가 10대처럼 나와 나이 묘사를 세게 넣었는데, Qwen-Image 는 그 말을 훨씬 강하게 받아
# 50~60대 할아버지처럼 그렸다 (2026-10-27 r1). 2차는 40대 초반의 매끈한 얼굴로 다시 적는다.
CHAR_OVERRIDE = {
    "james": ("James, a gentle father in his early forties, a youthful handsome adult face with smooth skin and only very "
              "faint smile lines at the corners of his eyes, kind warm eyes, clean-shaven, very tall and lanky with slightly "
              "stooped shoulders, messy unruly dark brown hair with three stray strands sticking out at the top like little "
              "cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves "
              "rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver "
              "watch chain. Signature design point: a very tall thin straight build with long limbs, a kind smooth face in "
              "his early forties, and three stray strands of hair sticking out from his messy brown hair"),
}
NEG_AGE = {"james": ", elderly, old man, grandfather, deep wrinkles, weathered skin, sagging skin, gray hair, white hair"}

DATE_DIR = "main/2026-10-27"
ROOT = "niki_compass_v2"


def convert(text: str) -> str:
    t = text.replace(v1.STYLE, STYLE).replace(v1.SHEET_BG, SHEET_BG)
    # 1차 그림체 문장 밖에 남은 손그림·수채 배경 문장도 새 그림체 쪽으로 옮긴다
    t = t.replace("Plain warm off-white paper background without any lettering.",
                  "Plain light gray studio background with a soft white glow, without any lettering.")
    for a, b in REPLACE.items():
        t = t.replace(a, b)
    return t


def hides_hands(job) -> bool:
    if job["id"] in HIDE_HANDS_EXCEPT:
        return False
    return job["char"] == "niki" or v1.NIKI_GUEST in job["text"]


def all_jobs():
    jobs = []
    for j in v1.all_jobs():
        w, h = SIZE[(j["w"], j["h"])]
        neg = NEGATIVE + (NEG_HANDS if hides_hands(j) else "")
        jobs.append({**j, "w": w, "h": h, "text": convert(j["text"]), "negative": neg,
                     "prefix": f"{ROOT}/{j['dir']}/{j['id']}"})
    return jobs


def build():
    jobs = all_jobs()
    (OUT / "jobs_v2.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    lines = ["# 니키와 이상한 나침반 · 컨셉아트 2차 확장 전 입력 (영문)", "",
             "- 1차(Z-Image Turbo)와 캐릭터 설명·컷 구성은 같고, 그림체 문장·시트 배경·크기·부정 프롬프트만 다르다.",
             "- 기존 작품·작가 이름은 넣지 않고 특징으로만 적었다.", "",
             "## 공통 그림체 문장", "", f"> {STYLE}", "", "## 공통 부정 프롬프트", "", f"> {NEGATIVE}", "",
             f"- 니키(성장 시트 제외)와 니키가 함께 나오는 컷에는 `{NEG_HANDS.lstrip(', ')}` 를 덧붙였다.", ""]
    cur = None
    for j in jobs:
        if j["char"] != cur:
            cur = j["char"]
            name = (v1.CHAR.get(cur) or v1.CHAR.get(f"{cur}_hood") or {}).get("name", cur)
            lines += [f"## {j['dir']} · {name}", ""]
        lines += [f"### {j['id']} · {j['kind']} · {j['w']}x{j['h']}", "", "```", j["text"], "```", ""]
        if j["negative"] != NEGATIVE:
            lines += ["- 부정 프롬프트: 공통 + 손 숨김", ""]
    (OUT / "inputs_v2_en.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"{len(jobs)} jobs -> jobs_v2.json, inputs_v2_en.md")


def emit_js(specs):
    """캐릭터 단위로 나눈 제출 코드. spec = '<캐릭터|컷,...>:<시드 수>:<회차>[:fast|<steps>]'. 시드는 기본 시드 + 1000*k."""
    jobs_all = all_jobs()
    n = 0
    for spec in specs:
        parts = spec.split(":")
        targets, variants, rnd = parts[:3]
        fast = len(parts) > 3 and parts[3] == "fast"
        steps = int(parts[3]) if len(parts) > 3 and parts[3].isdigit() else 50
        want = set(targets.split(","))
        for key in v1.ORDER:
            sel = [j for j in jobs_all if (j["char"] == key and (key in want or j["id"] in want))]
            if not sel:
                continue
            texts, out = [], []
            for j in sel:
                # 공통 문장은 페이지에 한 번 올려 둔 mgsV2 의 것으로 되살린다 (붙여 넣는 양을 줄인다)
                texts.append({"text": j["text"].replace(STYLE, "§S").replace(SHEET_BG, "§G"),
                              "negative": j["negative"].replace(NEGATIVE, "§N"), "h": v1.fnv(j["text"])})
                for k in range(int(variants)):
                    seed = j["base_seed"] + 1000 * k
                    out.append({"prefix": f"{ROOT}/{j['dir']}/{rnd}/{j['id']}_s{seed}", "w": j["w"], "h": j["h"],
                                "seed": seed, "t": len(texts) - 1, "fast": fast, "steps": steps})
            n += 1
            js = "\n".join([
                f"const T={json.dumps(texts, ensure_ascii=False)};",
                "const fnv = s => { let h = 0x811c9dc5; for (const x of new TextEncoder().encode(s)) "
                "{ h ^= x; h = Math.imul(h, 0x01000193) >>> 0; } return h.toString(16); };",
                "for (const x of T) { x.text = x.text.split('§S').join(mgsV2.S).split('§G').join(mgsV2.G); "
                "x.negative = x.negative.split('§N').join(mgsV2.N); }",
                "const bad = T.map((x, i) => fnv(x.text) === x.h ? null : i).filter(i => i !== null);",
                "if (bad.length) throw new Error('prompt mismatch: ' + bad.join(','));",
                f"const jobs={json.dumps(out)}.map(j => ({{...j, text: T[j.t].text, negative: T[j.t].negative}}));",
                "const r = await mgsQ.submit(jobs);",
                "r.map(x => `${x.status} ${x.prefix.split('/').slice(-2).join('/')} ${x.err ? JSON.stringify(x.err) : ''}`)",
            ]) + "\n"
            p = OUT / f"submit_v2_{n}_{key}.js"
            p.write_text(js, encoding="utf-8", newline="\n")
            print(f"{len(out)} jobs -> {p.name} ({len(js)} bytes)")


def expand_inputs():
    """확장 기능 입력: 컷 구성 = 요청, 캐릭터 설명 = 꼭 지킬 특징, 새 그림체 = 그림체 고정 문장."""
    blocks = sorted({convert(c["block"]) for c in v1.CHAR.values()}, key=len, reverse=True)
    out = []
    for j in all_jobs():
        t = j["text"].replace(STYLE, "").strip()
        blk = next((b for b in blocks if b in t), "")
        shot = t.replace(blk, "the character described in the must-keep details").strip() if blk else t
        out.append({"id": j["id"], "text": shot, "notes": blk})
    return out


def emit_expand(keys):
    """캐릭터별 확장 실행 코드. 결과는 페이지의 mgsX 와 localStorage('mgs.v2.expand')에 쌓는다."""
    inputs = [x for x in expand_inputs() if x["id"].rsplit("_", 1)[0] in keys]
    notes = sorted({x["notes"] for x in inputs})
    slim = [{**x, "notes": notes.index(x["notes"])} for x in inputs]
    js = "\n".join([
        f"const B={json.dumps(notes, ensure_ascii=False)};",
        f"const X={json.dumps(slim, ensure_ascii=False)}.map(x => ({{...x, notes: B[x.notes]}}));",
        "window.mgsX = window.mgsX || JSON.parse(localStorage.getItem('mgs.v2.expand') || '{}');",
        "(async () => { for (const x of X) { if (mgsX[x.id] && !mgsX[x.id].error) continue; const t = Date.now();",
        "  const r = await fetch('/mgs/api/expand', {method: 'POST', headers: {'Content-Type': 'application/json'},",
        "    body: JSON.stringify({text: x.text, notes: x.notes, style: mgsV2.S})});",
        "  const d = await r.json().catch(() => ({}));",
        "  mgsX[x.id] = r.ok ? {...d, input: x, sec: (Date.now() - t) / 1000} : {error: d.error || r.status, input: x};",
        "  localStorage.setItem('mgs.v2.expand', JSON.stringify(mgsX)); } })();",
        f"'expanding {len(inputs)}'",
    ]) + "\n"
    p = OUT / f"expand_v2_{'_'.join(keys)}.js"
    p.write_text(js, encoding="utf-8", newline="\n")
    print(f"{len(inputs)} inputs -> {p.name} ({len(js)} bytes)")


def emit_consts():
    """페이지에 한 번 올리는 공통 문장 (mgsV2)."""
    js = "window.mgsV2 = " + json.dumps({"S": STYLE, "G": SHEET_BG, "N": NEGATIVE}) + ";\n"
    (OUT / "consts_v2.js").write_text(js, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    build()
    emit_consts()
    if len(sys.argv) >= 3 and sys.argv[1] == "js":
        emit_js(sys.argv[2:])
