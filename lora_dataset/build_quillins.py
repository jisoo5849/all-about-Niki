"""퀼린스 학습 데이터를 두 모습으로 나눈다 (2026-10-30).

퀼린스는 스토리 초반의 얼굴 없는 두건 모습과 13장 이후 얼굴이 드러난 모습이 그림으로 보면 다른 캐릭터라,
한 트리거로 섞어 학습하면 두건 속에 얼굴이 생기거나 얼굴 장면에 두건이 다시 씌워진다.
그래서 LoRA 를 둘로 나누고(QUILLINS_HOOD_v1, QUILLINS_FACE_v1), 학습 이미지도 20장씩 따로 만든다.

- 두건 모습: 20장 모두 새로 만든다. build_v3 의 퀼린스 01~08 은 Krea2 가 두건 속에 얼굴을 그려 쓰지 않는다.
- 정체 공개 모습: 두건을 내린 모습과 50대 후반 나이를 분명히 적어 20장을 새로 만든다.

  python build_quillins.py   ->  quillins_shots.json, prompts_quillins_en.md, tools/data_quillins.js
"""
import json
import sys
from pathlib import Path

OUT = Path(__file__).parent
sys.path.insert(0, str(OUT))
import build_v3 as b  # noqa: E402

# 두건 모습 (2026-10-30 시험).
# - 'hides his whole face', 'no eyes, no mouth' 처럼 얼굴을 부정하면 오히려 얼굴을 그렸다.
# - 얼굴 컷 머리말의 'the face ... fill the picture', 그림체 문장의 큰 눈·볼 홍조, 옆모습의 'one eye visible' 도
#   두건 속에 얼굴을 부른다. 두건 모습에서는 이 말들을 모두 빼고 두건 속을 검은 그림자로만 적는다.
HOOD = dict(
    b.CHAR["quillins_hood"],
    head=("Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim "
          "and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a "
          "smooth black oval of darkness where a head should be, a mysterious hooded shadow figure"),
)
HOOD_STYLE = b.STYLE.replace("soft rosy blush on the cheeks, large clear expressive eyes with simple round highlights, ", "")
HOOD_FRAME = {
    "full": ("Full-body illustration of a single hooded figure from head to toe", b.FRAME["full"][1]),
    "waist": ("Medium shot from the waist up of a single hooded figure, the picture is cropped at the waist so the "
              "legs are out of frame", b.FRAME["waist"][1]),
    "face": ("Close-up of a single hooded figure, the hooded head and shoulders fill the whole picture, cropped just "
             "below the shoulders", b.FRAME["face"][1]),
}
HOOD_VIEW = dict(b.VIEW, side="side profile view facing right, in profile",
                 back=b.VIEW["back"].replace("the back of the head and the hair", "the back of the hood"))
# Qwen(cfg 4)에서만 듣는다
HOOD_NEG = ", face, eyes, glowing eyes, skin"

# 두건 모습 09~20: 얼굴이 없으니 표정 대신 각도·자세·배경·화면 크기로 다양하게
HOOD_EXTRA = [
    ("waist", "front", None, "standing perfectly still, the empty black shadow inside the hood facing the viewer"),
    # 'turning his hooded head' 는 Krea2 가 시드를 바꿔도 두건 속에 옆얼굴을 그렸다
    ("waist", "3qr", 0, "standing still with the deep black hood turned toward the sea"),
    ("waist", "side", 1, "standing still in profile, the deep hood hiding his face"),
    ("face", "front", None, "the deep hood filling the picture, its inside pure black shadow with no face"),
    ("face", "3ql", 2, "the deep hood and fur-trimmed collar filling the picture, the inside of the hood pure black"),
    ("waist", "3ql", 3, "one black-gloved hand raised to hold the edge of his cloak closed"),
    ("full", "front", 0, "looming over the viewer from a low camera angle, the cloak spreading like ink"),
    ("full", "back", 0, "standing still and looking out at the night sea"),
    ("full", "3qr", 3, "walking slowly along the waterline, the cloak hem dragging over wet sand"),
    ("full", "side", 1, "standing between dark pine trunks in the fog"),
    ("waist", "front", 2, "standing at the end of a stone pier, the wind pulling at the cloak"),
    ("full", "front", None, "standing with both black-gloved hands hanging at his sides"),
]

# 정체 공개 모습 (2026-10-30 시험)
# - 'bareheaded' 는 Z-Image·klein 이 대머리로, 'clearly aged ... heavily streaked with white' 는 Krea2 가 70대 백발로 그렸다.
# - 나이를 숫자로 적고 '노인이 아님'과 나이 흔적(팔자 주름·눈가 주름·회색 수염)을 함께 적어야 klein 상반신 컷도 50대로 나왔다.
FACE = dict(
    seed=23350,
    head=("Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged "
          "rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair "
          "streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind "
          "his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside "
          "his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the "
          "corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired "
          "dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on "
          "his neck and jaw"),
    # 'small round seal' 은 Qwen 이 손바닥만 하게 그렸다
    upper=("a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a "
           "worn ink-black cloak, black leather gloves"),
    lower="the worn ink-black cloak hanging down to his black boots",
    stand="standing with his back straight",
    calm="calm tired face looking into the distance",
    expr=["tired sorrowful eyes looking down", "a faint sad smile", "a stern cold stare", "quiet surprise",
          "a pained grimace", "a gentle soft look"],
    pose=["walking slowly along the waterline",
          "kneeling on wet sand beside a young gray seal pup with a bandaged flipper",
          "sitting on a large rock with his gloved hands resting on his knees",
          "standing at the end of a stone pier looking out at the sea"],
    scene=["a rocky shore at night under cold blue-gray moonlight", "a foggy pine forest",
           "a ruined stone pier by a gray sea", "an empty beach at dawn"],
)
# 그림체 문장의 큰 눈·볼 홍조가 얼굴을 어리게 만들어 정체 공개 모습에서는 작은 눈으로 바꾼다
FACE_STYLE = b.STYLE.replace("soft rosy blush on the cheeks, large clear expressive eyes with simple round highlights",
                             "simple eyes with small round highlights")
# Qwen(cfg 4)에서만 듣는다: 두건을 다시 씌우거나, 대머리·어린 얼굴·노인으로 그리는 것, 큰 인장을 막는다
FACE_NEG = (", hood on head, hooded head, hood covering the hair, bald, shaved head, young man, teenager, elderly, "
            "very old man, completely white hair, large red circle, big medallion")
# 정체 공개 모습은 klein·Qwen 만 쓴다. Krea2·Z-Image 는 목·턱의 썩은 피부와 소금 결정을 글로는 그리지 못했다.
FACE_MODELS = ["flux2_klein_4b", "qwen_image_2512"]


def describe(c: dict, frame: str) -> str:
    return ", ".join([c["head"], c["upper"]] + ([c["lower"]] if frame == "full" and c["lower"] else []))


def text_of(frame, view, bg, content, c, frames, views, style):
    back = b.PLAIN if bg is None else f"Background: {c['scene'][bg]}, painted in soft watercolor detail."
    head, (w, h) = frames[frame]
    return f"{head}, {views[view]}, {content}. {describe(c, frame)}. {back} {style}", w, h


def shots():
    out = []
    hood_rows = [(f, v, bg, HOOD["stand"] if what == "stand" else HOOD["pose"][what[1]])
                 for f, v, bg, what in b.MATRIX[:8]] + HOOD_EXTRA
    for row, (frame, view, bg, content) in enumerate(hood_rows, 1):
        text, w, h = text_of(frame, view, bg, content, HOOD, HOOD_FRAME, HOOD_VIEW, HOOD_STYLE)
        out.append(dict(id=f"quillins_hood_{row:02d}", set="hood", row=row, frame=frame, view=view, w=w, h=h,
                        seed=HOOD["seed"] + row, text=text, negative=b.NEGATIVE + HOOD_NEG))
    # 정체 공개 01~20: 다른 캐릭터와 같은 MATRIX
    for row, (frame, view, bg, what) in enumerate(b.MATRIX, 1):
        content = (FACE["stand"] if what == "stand" else FACE["calm"] if what == "calm"
                   else FACE["pose"][what[1]] if what[0] == "pose" else FACE["expr"][what[1]])
        text, w, h = text_of(frame, view, bg, content, FACE, b.FRAME, b.VIEW, FACE_STYLE)
        out.append(dict(id=f"quillins_face_{row:02d}", set="face", row=row, frame=frame, view=view, w=w, h=h,
                        seed=FACE["seed"] + row, text=text, negative=b.NEGATIVE + FACE_NEG))
    return out


def main():
    S = shots()
    (OUT / "quillins_shots.json").write_text(json.dumps(S, ensure_ascii=False, indent=1) + "\n", encoding="utf-8",
                                             newline="\n")
    L = ["# 퀼린스 두 모습 프롬프트 (영문)", "",
         "- 두건 모습(얼굴 없음)과 정체 공개 모습(얼굴 드러남)을 다른 LoRA 로 학습하도록 20장씩 나눴다.",
         "- 두건 모습은 4개 모델, 정체 공개 모습은 klein·Qwen 2개 모델에 같은 프롬프트·시드로 만들었다.",
         "- 두 모습 모두 그림체 문장에서 큰 눈·볼 홍조를 뺐다 (두건 속 얼굴, 어린 얼굴이 나와서).",
         f"- 부정어는 두건 모습에 `{HOOD_NEG.lstrip(', ')}`, 정체 공개 모습에 `{FACE_NEG.lstrip(', ')}` 를 더했다"
         " (cfg 4 인 Qwen 에서만 듣는다).", ""]
    for s in S:
        style = HOOD_STYLE if s["set"] == "hood" else FACE_STYLE
        L += [f"### {s['id']} · {s['frame']} · {s['view']} · {s['w']}x{s['h']} · 시드 {s['seed']}", "",
              "```", s["text"].replace(" " + style, ""), "```", ""]
    (OUT / "prompts_quillins_en.md").write_text("\n".join(L), encoding="utf-8", newline="\n")
    js = "window.QL = " + json.dumps([{k: s[k] for k in ("id", "set", "w", "h", "seed", "text", "negative")} for s in S],
                                     ensure_ascii=False) + ";\n"
    (OUT / "tools" / "data_quillins.js").write_text(js, encoding="utf-8", newline="\n")
    print(len(S), "shots,", len(js), "bytes js")


if __name__ == "__main__":
    main()
