"""final_v2.json(+ ko_v2.json) 으로 프롬프트 문서 두 개를 만든다.

  python render_v2.py   ->  prompts_v2_en.md (영문, 실제로 넣은 그대로), prompts_v2_ko.md (한글판)
"""
import json
import sys
from pathlib import Path

OUT = Path(__file__).parent
sys.path.insert(0, str(OUT))
import build_v2  # noqa: E402
from extract_v2 import ANCHOR  # noqa: E402

KIND = {"1": "턴어라운드", "3": "표정 시트"}


def load():
    F = json.loads((OUT / "final_v2.json").read_text(encoding="utf-8"))
    K = json.loads((OUT / "ko_v2.json").read_text(encoding="utf-8"))
    return F, K


def common_neg(neg: str) -> list[str]:
    extra = neg[len(build_v2.NEGATIVE):].strip(", ") if neg.startswith(build_v2.NEGATIVE) else neg
    return [w.strip() for w in extra.split(",") if w.strip()]


def en(F):
    L = ["# 니키와 이상한 나침반 · 컨셉아트 2차 프롬프트 (영문, 실제 입력)", "",
         "- 생성 모델은 Qwen-Image-2512(30 steps, cfg 4, euler)이고, 편집은 Qwen-Image-Edit-2511(Lightning 4 steps)이다.",
         "- 각 컷의 '확장 입력'을 허브의 프롬프트 확장 기능에 넣었고, 돌아온 '확장 프롬프트'로 그렸다.",
         "- 실제 생성 프롬프트는 `그림체 머리말 + 확장 프롬프트 + 그림체 고정 문장` 순서다 (머리말·고정 문장은 아래 공통 문장).",
         "- 모든 값은 최종 PNG 안의 실행 정보에서 꺼냈다 (`extract_v2.py`).", "",
         "## 공통 문장", "", "### 그림체 머리말 (r3 부터 앞에 붙임)", "", f"> {ANCHOR.strip()}", "",
         "### 그림체 고정 문장 (확장 기능이 끝에 그대로 붙임)", "", f"> {build_v2.STYLE}", "",
         "### 공통 부정 프롬프트", "", f"> {build_v2.NEGATIVE}", ""]
    cur = None
    for r in F:
        ch = r["final"].split("/")[1]
        if ch != cur:
            cur = ch
            L += [f"## {ch}", ""]
        g = r["generation"]
        L += [f"### {r['shot']} · `{r['final']}`", "",
              f"- 생성: 시드 {g['seed']}, {g['w']}x{g['h']}, 원본 `{g.get('main_file', r['main_file'])}`",
              "", "**확장 입력 (요청)**", "", "```", r["expand_input"]["text"], "```", "",
              "**확장 입력 (꼭 지킬 특징)**", "", "```", r["expand_input"]["notes"], "```", "",
              "**확장 프롬프트**", "", "```", g["expanded"], "```", ""]
        if not g["anchor"]:
            L += ["- 이 컷은 그림체 머리말 없이 r1 로 그린 원본을 편집으로 애니풍으로 바꿨다.", ""]
        extra = common_neg(g["negative"])
        if extra:
            L += [f"- 부정 프롬프트 추가: `{', '.join(extra)}`", ""]
        if "edit" in r:
            L += [f"**편집 지시 (시드 {r['edit']['seed']})**", "", "```", r["edit"]["text"], "```", ""]
    (OUT / "prompts_v2_en.md").write_text("\n".join(L), encoding="utf-8", newline="\n")


def ko(F, K):
    L = ["# 니키와 이상한 나침반 · 컨셉아트 2차 프롬프트 (한글판)", "",
         "- `prompts_v2_en.md` 의 확장 프롬프트와 편집 지시를 한글로 옮겼다.",
         "- 생성 모델에는 영문이 들어갔으므로, 다시 그릴 때는 영문판을 쓴다.",
         "- 확장 기능이 남긴 어색한 표현도 고치지 않고 그대로 옮겼다.",
         "  - 예: 손 단어를 피하려고 쓴 '팔다리 끝(extremities)', 이름이 바뀐 '퀼린스(Quilins)'", ""]
    cur = None
    for r in F:
        ch = r["final"].split("/")[1]
        if ch != cur:
            cur = ch
            L += [f"## {ch}", ""]
        k = K[r["shot"]]
        L += [f"### {r['shot']} · `{r['final']}`", "", "**확장 프롬프트**", "", "```", k["expanded"], "```", ""]
        if "edit" in r:
            L += ["**편집 지시**", "", "```", k["edit"], "```", ""]
    (OUT / "prompts_v2_ko.md").write_text("\n".join(L), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    F, K = load()
    missing = [r["shot"] for r in F if r["shot"] not in K or ("edit" in r and "edit" not in K[r["shot"]])]
    if missing:
        raise SystemExit(f"한글판이 빠진 컷: {missing}")
    en(F)
    ko(F, K)
    print("prompts_v2_en.md, prompts_v2_ko.md")
