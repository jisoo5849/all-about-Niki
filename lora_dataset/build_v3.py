"""LoRA 학습용 이미지 v3: 생성 모델 4개를 같은 프롬프트·시드·크기로 비교한다.

캐릭터 특징은 LoRA-FINE-TUNING-Image-models 의 character-bible.md (컨셉 시트 + 니키 작가 상상도)를 따른다.
그림체는 9명 모두 니키 상상도에 맞춘다. 캐릭터 설명은 머리·얼굴 / 상의 / 하의로 나눠, 화면에 들어오는 부분만 넣는다
(상반신 컷에 부츠가 적혀 있으면 모델이 전신을 그렸다).

  python build_v3.py   ->  shots.json, prompts_en.md
"""
import json
from pathlib import Path

OUT = Path(__file__).parent

# 니키 작가 상상도에서 읽은 그림체 (작품·작가 이름은 넣지 않는다)
STYLE = (
    "Hand-drawn Japanese anime feature film style: clean confident dark outlines, flat cel shading with one soft "
    "shadow tone, soft rosy blush on the cheeks, large clear expressive eyes with simple round highlights, "
    "hand-painted watercolor backgrounds, dappled sunlight filtering through leaves, bright clear fresh colors, "
    "warm gentle natural light, original character design."
)
PLAIN = "Plain soft cream background without any lettering."
NEGATIVE = ("photorealistic, 3d render, cgi, semi-realistic, text, letters, watermark, logo, signature, blurry, "
            "deformed hands, extra fingers, extra limbs, duplicate face, multiple people")

# 캐릭터별 부정어 추가 (cfg 4 인 Qwen-Image 2512 에서만 실제로 듣는다. 시험에서 Qwen 이 제임스를 늙게 그렸다)
NEG_EXTRA = {"james": ", wrinkles, lined face, aged skin, gray hair, old man"}

FRAME = {
    "full": ("Full-body illustration of a single character from head to toe", (1024, 1536)),
    "waist": ("Medium shot from the waist up of a single character, the picture is cropped at the waist so the legs "
              "are out of frame", (1024, 1280)),
    "face": ("Close-up portrait of a single character, the face and shoulders fill the whole picture, cropped just "
             "below the shoulders", (1024, 1024)),
}
VIEW = {
    "front": "front view facing the viewer",
    "3ql": "three-quarter view turned slightly to the left",
    "3qr": "three-quarter view turned slightly to the right",
    "side": "side profile view facing right, in profile with only one eye visible",
    # 'glancing back' 을 넣으면 얼굴을 보여 주려고 앞모습을 그렸다
    "back": "rear view, the character stands facing away from the viewer toward the background, so we see only the "
            "back, the back of the head and the hair",
}
# (화면, 각도, 배경: None=무지 / 0~3=장면, 내용: stand / calm / ('pose', i) / ('expr', i))
MATRIX = [
    ("full", "front", None, "stand"),
    ("full", "3ql", None, ("pose", 0)),
    ("full", "3qr", None, "stand"),
    ("full", "side", None, "stand"),
    ("full", "back", None, "stand"),
    ("full", "3qr", 0, ("pose", 1)),
    ("full", "front", 1, ("pose", 2)),
    ("full", "3ql", 2, ("pose", 3)),
    ("waist", "front", None, ("expr", 0)),
    ("waist", "3qr", None, ("expr", 1)),
    ("waist", "3ql", 0, ("expr", 2)),
    ("waist", "side", 1, ("expr", 3)),
    ("waist", "front", 2, ("expr", 4)),
    ("waist", "3qr", 3, ("expr", 5)),
    ("face", "front", None, ("expr", 0)),
    ("face", "3ql", None, ("expr", 1)),
    ("face", "3qr", 3, ("expr", 2)),
    ("face", "side", None, "calm"),
    ("face", "front", 0, ("expr", 3)),
    ("face", "3ql", 1, ("expr", 4)),
]

SLEEVES = ("the floppy cream sleeve cuffs hang far below her wrists, closed and empty-looking")

# head: 머리·얼굴·체형, upper: 상의, lower: 하의·신발 (전신 컷에만)
CHAR = {
    "niki": dict(
        seed=21100,
        head=("Niki, a shy 12-year-old girl, very small and thin, a dark brown chin-length bob with blunt straight-cut "
              "bangs and slightly uneven wispy ends, a few loose strands sticking up at the crown, large clear "
              "sky-blue eyes, light freckles across her nose and cheeks, rosy cheeks, pale creamy skin, small mouth"),
        upper=("wearing a wine-red cape coat over a cream round-collar shirt whose extremely long sleeves droop far "
               "past her wrists, " + SLEEVES),
        lower="dark mocha-brown wool shorts, charcoal gray tights and low-heeled brown boots",
        stand=f"standing still with her arms hanging straight down",
        calm="calm quiet face with her gaze lowered",
        expr=["shy with her eyes downcast behind her bangs", "a bright open-mouthed happy smile",
              "observant with calm eyes glancing sideways", "a small gentle smile",
              "scared but determined with wide eyes and lips pressed tight", "a tiny teasing smirk"],
        pose=["walking forward timidly", "sitting on a low wooden stool with her knees together",
              "crouching down low to look at a small flower on the ground",
              "running across the grass with her cape fluttering behind her"],
        scene=["a sunny summer meadow with tall green grass and fluffy white clouds",
               "a sunlit glass greenhouse full of potted plants", "a quiet cobblestone village street",
               "the shade of a big leafy tree on a grassy hill"],
    ),
    "putor": dict(
        seed=21200,
        head=("Putor, an elderly dwarf healer in his sixties, very short, about the height of a child, with a plump "
              "round body and round sloping shoulders, fluffy white hair with pointed ear tips peeking out of it, a "
              "long fluffy white beard with pale green herb powder at the tips, bushy white eyebrows, a round red nose "
              "tip, small half-moon reading glasses with half-circle lenses and flat tops perched on the tip of his "
              "nose, no hat"),
        upper=("a dusty antique-brass travel coat over an ink-black vest and a parchment-colored shirt, a small brass "
               "healer badge on his chest, a huge boxy brown leather medicine bag full of glass vials hanging on a "
               "shoulder strap in front of his belly and covering half of his round body"),
        lower="a small empty leather flint case with a paper tag at his belt, short brown boots",
        stand="standing in a relaxed neutral pose",
        calm="calm kind face looking over his half-moon glasses",
        expr=["worried with a deep frown and his beard drooping", "fussy scolding with puffed cheeks",
              "frightened with wide eyes and his white beard bristling", "relieved with a soft smile",
              "muttering herb names with his eyes squeezed shut", "peering kindly over his half-moon glasses"],
        pose=["walking with short quick steps", "sitting on a tree stump sorting small glass vials",
              "kneeling on the ground grinding herbs in a small stone mortar",
              "hurrying forward anxiously, hugging the small empty flint case to his chest"],
        scene=["a cool blue-gray forest path", "a cozy cottage kitchen with bundles of dried herbs hanging overhead",
               "a sunny meadow full of wildflowers", "a rainy village street with puddles"],
    ),
    "quillins_hood": dict(
        seed=21300,
        head=("Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur "
              "trim and bone toggles, the deep hood hides his whole face in pure black shadow, a faceless figure"),
        upper="black leather gloves, a glimpse of a dark indigo coat under the cloak",
        lower="the cloak hem dragging on the ground",
        stand="standing perfectly still", calm="", expr=[],
        pose=["walking slowly with the black cloak dragging behind him",
              "standing at the edge of a cliff with the cloak blowing in the wind",
              "crouching over a tide pool, one black-gloved hand reaching toward the water",
              "turning away into the fog"],
        scene=["a rocky shore at night under cold blue-gray moonlight", "a foggy pine forest",
               "a ruined stone pier by a gray sea", "an empty beach at dawn"],
    ),
    "quillins_reveal": dict(
        seed=21350,
        head=("Quillins, a clearly aged man in his late fifties, tall and thin with drooping shoulders, his black hood "
              "pushed back and resting on his shoulders, a long gaunt face with sunken cheeks, black hair heavily "
              "streaked with white, dark gray eyes with a black tint, patches of bluish-black cracked skin with small "
              "white salt crystals on his neck and jaw"),
        upper=("a dark indigo long chieftain coat with a small round coral-pink seal at the chest under a worn "
               "ink-black cloak, black leather gloves"),
        lower="", stand="standing with his back straight", calm="calm tired face looking into the distance",
        expr=["tired sorrowful eyes looking down", "a faint sad smile", "a stern cold stare", "quiet surprise",
              "a pained grimace", "a gentle soft look"],
        pose=[], scene=["a rocky shore at night under cold blue-gray moonlight", "a foggy pine forest",
                        "a ruined stone pier by a gray sea", "an empty beach at dawn"],
    ),
    "james": dict(
        seed=21400,
        # 주름 말을 넣으면 할아버지처럼 나왔다 (사용자 검수, 2026-10-29)
        head=("James, a gentle father in his early forties, very tall and lanky with slightly stooped shoulders, a "
              "long gentle adult face with a firm jaw and smooth skin, kind warm eyes, clean-shaven, messy unruly "
              "brown hair with three stray strands sticking up at the top"),
        upper=("a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches and "
               "rolled-up sleeves, a thin silver watch chain"),
        lower="worn brown trousers and muddy brown rubber boots",
        stand="standing in a relaxed neutral pose", calm="calm kind face with a faint smile",
        expr=["a warm smile", "a sheepish laugh after a clumsy mistake", "patiently waiting with a calm gentle gaze",
              "worried with raised eyebrows", "a playful grin with one eyebrow up", "quiet sadness with a faint smile"],
        pose=["walking with long lanky strides", "sitting on a wooden bench with his long legs stretched out",
              "crouching low to press the soil around a seedling", "carrying a metal watering can at his side"],
        scene=["a sunlit glass greenhouse", "a cozy cottage interior with low wooden beams",
               "a vegetable garden at sunset", "a misty forest edge in the morning"],
    ),
    "beth": dict(
        seed=21500,
        head=("Beth, a calm mother in her early forties, tall and slender with an upright posture, long wavy black "
              "hair loosely tied at the nape, a calm intelligent face with straight eyebrows, dark chestnut eyes with "
              "faint amber glints"),
        upper=("a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and "
               "a pencil in its front pocket, a small amber brooch on her chest"),
        lower="a long dark skirt and simple brown shoes",
        stand="standing upright in a relaxed neutral pose", calm="calm composed face",
        expr=["calm neutral composure", "a gentle subtle smile", "a firm determined look",
              "a focused downward gaze as if writing in her notebook", "a secretive sideways glance",
              "quiet worry with lips pressed together"],
        pose=["walking calmly with an upright posture", "sitting at a wooden table writing in her small notebook",
              "kneeling to check seedlings in a wooden planter", "standing and pouring tea from a ceramic teapot"],
        scene=["a greenhouse at evening with warm lamp light", "a cozy cottage kitchen",
               "a windy hilltop with tall grass", "a quiet library corner with old bookshelves"],
    ),
    "taoba": dict(
        seed=21600,
        # 'ruddy face' 는 얼굴·손 전체를 빨갛게 칠했다
        head=("Taoba, a jolly gardener in his mid-fifties, medium height with a big round pot belly, curly bushy brown "
              "hair and a thick bushy brown beard with a few gray hairs merged into one big bush shape around his "
              "round face, lightly rosy cheeks, narrow smiling eyes"),
        upper=("a sage-green linen shirt with rolled-up sleeves, brown suspenders, a tan leather work apron with "
               "labeled pockets holding pruning shears and a magnifying glass"),
        lower="brown trousers and work boots",
        stand="standing in a relaxed neutral pose with his thumbs hooked in his suspenders",
        calm="calm cheerful face",
        expr=["a booming open-mouthed laugh with his eyes shut into happy curves", "whispering softly with gentle eyes",
              "gentle concern with raised bushy eyebrows", "surprised with wide round eyes", "telling a joke with a wink",
              "a serious protective look"],
        pose=["pushing a wooden wheelbarrow full of soil", "sitting on an upturned clay flower pot",
              "kneeling to examine a tiny seedling", "carrying a big sack of soil on one shoulder"],
        scene=["an overgrown glass greenhouse full of potted plants", "a garden shed with tools hanging on the wall",
               "a sunny vegetable garden", "a greenhouse at night lit by small lanterns"],
    ),
    "ilia": dict(
        seed=21700,
        # 'powder-blue ribbon' 이 분홍·파랑으로 섞여 나와, 한 가지 색의 작은 머리끈으로 못 박는다
        head=("Ilia, a slim adult woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied "
              "with one small solid powder-blue hair tie in a pale grayish blue, a smooth forehead, sharp clear "
              "eyebrows, a kind confident face"),
        upper="a sage-green work jacket over a cream t-shirt, a practical apron",
        lower="a folding notebook and small garden scissors hanging at her waist, dark trousers and brown shoes",
        stand="standing tall in a relaxed neutral pose", calm="calm confident face",
        expr=["firm scolding with her ponytail sticking straight up", "a warm big-sister smile",
              "confident and focused", "an exasperated sigh with closed eyes",
              "a gentle reassuring look with her head tilted", "laughing openly"],
        pose=["walking briskly with her folding notebook", "sitting on a wooden crate writing a care schedule",
              "kneeling to tie a young plant to a stake", "standing with one hand on her hip"],
        scene=["a sunny greenhouse", "rows of seedlings in a garden", "a potting bench in a workshop",
               "a breezy garden path in the morning"],
    ),
    "iloke": dict(
        seed=21800,
        head=("Iloke, a quiet adult man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark "
              "brown hair, thick eyebrows, an angular square jaw, steady gentle eyes"),
        upper=("a deep forest-green work vest over a cream linen shirt with rolled-up sleeves, brown leather work "
               "gloves"),
        lower="a brown leather belt with a folded umbrella hanging from it, dark trousers and brown boots",
        stand="standing in a relaxed neutral pose", calm="calm steady face",
        expr=["a calm stoic face", "a tiny smile only in his eyes", "quiet concern with slightly knitted brows",
              "slight embarrassment looking away with a faint blush", "a firm protective look",
              "relaxed and sleepy with half-closed eyes"],
        pose=["walking steadily carrying two clay flower pots",
              "sitting on a low stone wall with a folded umbrella across his knees",
              "kneeling to repair a wooden planter box", "standing in light rain under an open umbrella"],
        scene=["a rainy garden path", "a misty morning garden", "a greenhouse workshop",
               "a stone bridge over a small stream"],
    ),
    "iluki": dict(
        seed=21900,
        head=("Iluki, a playful thin adult man in his mid-twenties, medium height, a sharp pointed chin, short curly "
              "chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows"),
        upper=("an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows over a cream shirt "
               "collar"),
        lower="baggy trousers with bulging pockets, a little toy frog peeking out of one pocket, brown shoes",
        stand="standing in a relaxed neutral pose with his hands in his pockets", calm="calm face with a small smile",
        expr=["a huge mischievous grin", "an exaggerated shocked face with a dropped jaw", "pouting with puffed cheeks",
              "a sneaky plotting look with narrowed eyes", "laughing so hard that tears gather in his eyes",
              "a rare sincere gentle smile"],
        pose=["running with a toy frog held up high", "sitting cross-legged on the ground juggling small toys",
              "crouching to hide behind a large plant pot", "leaning forward and winking with a toy frog"],
        scene=["a busy greenhouse", "a sunny meadow", "a cluttered toy workbench",
               "a village street on a bright afternoon"],
    ),
}

ORDER = ["niki", "putor", "quillins", "james", "beth", "taoba", "ilia", "iloke", "iluki"]


def who(char: str, frame: str) -> str:
    """퀼린스는 전신은 두건(얼굴 없음), 상반신·얼굴은 두건을 벗은 모습."""
    if char != "quillins":
        return char
    return "quillins_hood" if frame == "full" else "quillins_reveal"


def describe(ck: str, frame: str) -> str:
    c = CHAR[ck]
    parts = [c["head"], c["upper"]] + ([c["lower"]] if frame == "full" and c["lower"] else [])
    return ", ".join(parts)


def shots():
    out = []
    for i, char in enumerate(ORDER, 1):
        for row, (frame, view, bg, what) in enumerate(MATRIX, 1):
            ck = who(char, frame)
            c = CHAR[ck]
            content = (c["stand"] if what == "stand" else c["calm"] if what == "calm"
                       else c["pose"][what[1]] if what[0] == "pose" else c["expr"][what[1]])
            back = PLAIN if bg is None else f"Background: {c['scene'][bg]}, painted in soft watercolor detail."
            head, (w, h) = FRAME[frame]
            text = f"{head}, {VIEW[view]}, {content}. {describe(ck, frame)}. {back} {STYLE}"
            out.append({"id": f"{char}_{row:02d}", "char": char, "who": ck, "dir": f"{i:02d}_{char}", "row": row,
                        "frame": frame, "view": view, "background": "plain" if bg is None else c["scene"][bg],
                        "content": content, "w": w, "h": h, "seed": CHAR[ck]["seed"] + row,
                        "text": text, "negative": NEGATIVE + NEG_EXTRA.get(char, "")})
    return out


def build():
    S = shots()
    (OUT / "shots.json").write_text(json.dumps(S, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    L = ["# LoRA 학습용 이미지 프롬프트 v3 (영문, 모든 모델 공통)", "",
         "- 같은 프롬프트·시드·크기로 4개 모델에서 그렸다.",
         "- 프롬프트 모양: `<화면 크기>, <각도>, <자세 또는 표정>. <캐릭터 설명>. <배경> <그림체 문장>`",
         "- 캐릭터 설명은 화면에 들어오는 부분만 넣었다 (전신: 머리·얼굴 + 상의 + 하의, 상반신·얼굴: 머리·얼굴 + 상의).", "",
         "## 그림체 문장 (니키 작가 상상도 기준)", "", f"> {STYLE}", "", "## 부정 프롬프트 (cfg 1 모델에서는 거의 쓰이지 않음)", "",
         f"> {NEGATIVE}", "", f"- 제임스에게만 덧붙임: `{NEG_EXTRA['james'].lstrip(', ')}`", ""]
    cur = None
    for s in S:
        if s["char"] != cur:
            cur = s["char"]
            L += [f"## {s['dir']}", ""]
        L += [f"### {s['id']} · {s['frame']} · {s['view']} · {s['w']}x{s['h']} · 시드 {s['seed']}", "",
              "```", s["text"].replace(" " + STYLE, ""), "```", ""]
    (OUT / "prompts_en.md").write_text("\n".join(L), encoding="utf-8", newline="\n")
    print(len(S), "shots -> shots.json, prompts_en.md")


if __name__ == "__main__":
    build()
