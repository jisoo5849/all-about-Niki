"""니키와 이상한 나침반: 등장인물 컨셉아트 프롬프트 생성기.

컨셉시트(등장인물_컨셉시트.pdf)의 확정·제안 내용을 캐릭터 블록으로 고정하고,
모든 컷에 같은 블록을 그대로 반복한다 (시트 5장 '같은 문장을 매번 반복' 규칙).
기존 작품·캐릭터·작가 이름은 프롬프트에 넣지 않는다 (시트 5장 5단계). 그림체는 특징으로 묘사한다.

  python build_prompts.py                         ->  jobs.json (전체 컷), prompts_en.md (프롬프트 시트, 영문)
  python build_prompts.py js <캐릭터|컷,...>:<시드 수>:<회차> [...]
                                                  ->  submit.js (메인 ComfyUI 페이지에서 실행할 제출 코드,
                                                      submit_helper.js 의 mgsZ 가 먼저 올라가 있어야 함)
      예: python build_prompts.py js niki:3:r2                 (니키 5컷 × 시드 3개)
          python build_prompts.py js putor_2,putor_4:3:r3 james:2:r1
"""
import json
import sys
from pathlib import Path

OUT = Path(__file__).parent

# 그림체: 1990~2000년대 일본 손그림 판타지 장편 애니메이션 (센과 치히로·이웃집 토토로 계열)을 특징으로 묘사
STYLE = (
    "Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: "
    "clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, "
    "softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, "
    "nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, "
    "original character design."
)
SHEET_BG = "Plain warm off-white paper background, clean design sheet layout without any lettering or captions."

# Z-Image Turbo 는 cfg 1 로 돌리므로 부정 프롬프트는 사실상 쓰이지 않는다. 피할 것은 긍정 문장으로 적는다.
NEGATIVE = ("photorealistic, 3d render, cgi, glossy, plastic skin, text, letters, watermark, logo, signature, "
            "blurry, deformed hands, extra fingers, extra limbs, duplicate face, cropped feet")

# 니키의 핵심 상징 (시트 3-1: 손. 소매 속 손 -> 친구의 손 -> 맨손 [확정], 애니 연출: 소매를 실제보다 길게).
# 옷 목록 속 한 구절로만 쓰면 모델이 손을 그려 버려서, 앞에서 한 번 말하고 끝에서 따로 한 문장으로 다시 못 박는다.
# 손을 뻗거나 무언가를 쥐는 동작을 적으면 손을 그리므로, 컷마다 '소매 끝이' 동작을 하도록 쓴다.
NIKI_SLEEVES = ("Signature design point: the cream shirt sleeves are far longer than her arms, the soft sleeve cuffs "
                "droop past her fingertips and completely cover both hands, so no fingers are visible")
# 다른 캐릭터 장면에 니키가 함께 나올 때 쓰는 짧은 묘사
NIKI_GUEST = ("a small shy 12-year-old girl with a jet-black bob in a wine-red cape coat, the floppy ends of her "
              "extremely long cream sleeves dangling over her hands so that her hands stay hidden")


# 일루키 장면에 일리아가 함께 나올 때 쓰는 짧은 묘사 (일리아 블록과 같은 외형)
ILIA_GUEST = ("a slim young woman in her mid-twenties with a neat brown ponytail tied with a powder-blue ribbon, "
              "wearing a sage-green work jacket and an apron")


def sig(text):
    """캐릭터마다 시트의 핵심 상징을 블록 끝에 따로 한 문장으로 둔다."""
    return f". Signature design point: {text}"


# 캐릭터 블록: 시트의 [확정] 외형을 빠짐없이, 헥스 색은 색 이름으로 옮김
CHAR = {
    "niki": dict(
        name="니키 그린", seed=12100, color="wine red",
        block=("Niki, a shy 12-year-old girl whose hands are always hidden inside her overly long sleeves, "
               "very small and thin for her age (much shorter than the adults), "
               "chin-length straight jet-black bob with short side-swept bangs half covering her eyes, "
               "very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, "
               "wearing a wine-red cape coat over a cream round-collar shirt, "
               "dark mocha brown wool shorts, charcoal gray tights and faded brown boots. " + NIKI_SLEEVES),
    ),
    "niki_indoor": dict(
        name="니키 그린 (집 안 의상)", seed=12150, color="cream",
        block=("Niki, a shy 12-year-old girl, very small and thin for her age, chin-length straight jet-black bob "
               "with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale "
               "creamy skin, small mouth, wearing her indoor clothes without any coat: a loose cream cotton shirt "
               "with a small rounded flat collar and extremely long sleeves, dark mocha brown wool shorts, charcoal "
               "gray tights and faded brown boots, the same outfit in every drawing"),
    ),
    "putor": dict(
        name="푸토르", seed=12200, color="antique brass",
        block=("Putor, an elderly dwarf healer in his sixties, very short (about the height of a child) with a plump "
               "round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips "
               "peeking out of it, a long fluffy white beard dusted with pale green herb powder at the tips, bushy "
               "white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses (lenses shaped "
               "like half circles with flat tops) perched on the tip of his nose, no hat, a plain dusty antique-brass "
               "travel coat with a few small pale green herb-powder stains, an ink-black vest, a parchment-colored "
               "shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with "
               "many small compartments of clinking glass vials, carried on a shoulder strap in front of his belly, "
               "an empty small leather flint case with a little paper tag at his belt"
               + sig("a round silhouette half hidden behind the huge medicine bag, pointed ear tips, half-moon glasses "
                     "that he wears in every drawing, and a long white beard tipped with green herb powder that "
                     "bristles when he is scared and droops when he is relieved")),
    ),
    "quillins_hood": dict(
        name="퀼린스 (두건, 1~12장)", seed=12300, color="ink black",
        block=("Quillins, a tall thin man with angular shoulders, wrapped in a worn ink-black hooded cloak, "
               "the deep hood hides his whole face in complete shadow with no visible features, "
               "black leather gloves, faded fur trim and bone toggles on the cloak, the hem dragging on the ground, "
               "a glimpse of an old dark indigo coat underneath"
               + sig("a faceless ink-black silhouette, the inside of the hood is pure black shadow like spreading "
                     "ink with no eyes, nose or mouth, only the black-gloved hands stand out")),
    ),
    "quillins_reveal": dict(
        name="퀼린스 (정체 공개, 13장 이후)", seed=12350, color="dark indigo",
        # 나이를 한 번만 적으면 모델이 20~30대로 그려서, 늙고 수척한 인상을 여러 단서로 겹쳐 적는다
        block=("Quillins, an old man in his late fifties, clearly aged, tall and thin with angular shoulders, his "
               "hood pushed back off his head and hanging behind his neck, a long gaunt deeply lined face with sunken "
               "cheeks and hollow tired eyes, black hair heavily streaked with white, dark gray eyes with a black "
               "tint, patches of bluish-black decayed skin on his neck and jaw, cracked like dry mud with small white "
               "salt crystals in the cracks, an old dark indigo long chieftain coat with a small round coral-pink "
               "chieftain's seal pinned at the chest, a worn ink-black cloak on his shoulders, black leather gloves"
               + sig("an aged gaunt face, small white salt crystals in the cracks of the bluish-black decayed skin, "
                     "and black leather gloves that hide his sick hands")),
    ),
    "james": dict(
        name="제임스 그린", seed=12400, color="slate blue",
        # r1 에서 10대처럼 그려지고, 시그니처의 '딸' 언급 때문에 아이가 끼어들어 나이 단서를 겹치고 딸 언급을 뺐다
        block=("James, a gentle father in his early forties with the clearly adult face of a forty-year-old man, not "
               "a young man: a long face with high cheekbones, faint lines on his forehead and around his eyes and "
               "mouth, slightly tired kind eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, "
               "messy unruly brown hair with three stray strands sticking out at the top like little cowlicks, "
               "a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, "
               "sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber "
               "boots, a thin silver watch chain"
               + sig("a very tall thin straight build with long limbs, a kind adult face with laugh lines, and three "
                     "stray strands of hair sticking out from his messy brown hair")),
    ),
    "beth": dict(
        name="베스 그린", seed=12500, color="deep forest green",
        block=("Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight "
               "posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint "
               "lines at the corners of her eyes and straight eyebrows, "
               "dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, "
               "a natural linen apron with a small notebook and a pencil in its front pocket, "
               "a small amber brooch on her chest"
               + sig("a tall straight upright silhouette drawn with thin lines, the long wavy hair simplified into "
                     "gentle wave lines, and a small amber brooch that matches the faint amber glint in her eyes")),
    ),
    "taoba": dict(
        name="타오바", seed=12600, color="sage green",
        block=("Taoba, a jolly stocky gardener in his mid-fifties, medium height with a big round pot belly, "
               "round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, "
               "curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big "
               "bush-like shape around his face, a sage-green linen shirt with rolled sleeves, brown trousers with "
               "suspenders, a tan leather work apron whose labeled pockets are full of small garden tools, pruning "
               "shears and a magnifying glass"
               + sig("his hair and beard are drawn as one big round bush-like mass around his face, on a big round "
                     "pot-bellied body")),
    ),
    "ilia": dict(
        name="일리아", seed=12700, color="powder blue",
        block=("Ilia, a slim young woman in her mid-twenties, medium height, upright posture, "
               "a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, "
               "clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, "
               "a practical apron, a folding notebook and small garden scissors hanging at her waist"
               + sig("a straight upright posture and a brown ponytail tied with a powder-blue ribbon, the ponytail "
                     "stands up when she is angry and droops softly when she is gentle")),
    ),
    "iloke": dict(
        name="일로케", seed=12800, color="leather brown",
        block=("Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, "
               "neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, "
               "a deep forest-green work vest over a cream linen shirt with rolled sleeves, "
               "brown leather work gloves and a brown leather belt, plain practical clothes, "
               "a folded umbrella hanging from his belt"
               + sig("a big broad rectangular body shape, neat short hair, brown leather accents, and gloved hands "
                     "that always offer something first")),
    ),
    "iluki": dict(
        name="일루키", seed=12900, color="mustard yellow",
        block=("Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, "
               "short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, "
               "big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves "
               "pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, "
               "a little toy frog peeking out of one pocket"
               + sig("a thin body with big gestures, a sharp pointed chin, curly chestnut hair, freckles only "
                     "on the nose and upper cheeks, and the mustard-yellow sweater that catches the eye first")),
    ),
}

L, P, S = (1536, 1024), (1024, 1536), (1024, 1024)


def turnaround(c, pose="relaxed neutral standing pose"):
    return dict(kind="턴어라운드", size=L, text=(
        f"Character model sheet: the same single character drawn three times side by side, front view, side view "
        f"and back view, full body from head to toe, {pose}, identical outfit and proportions "
        f"in all three views, evenly spaced. {CHAR[c]['block']}. {SHEET_BG} {STYLE}"))


def expressions(c, emotions, same="Same hairstyle, outfit and accessories in every portrait."):
    # 니키 표정 시트는 r2 결과를 쓰므로 그때 문장("Same hairstyle and outfit in every portrait.")을 그대로 둔다
    return dict(kind="표정 시트", size=L, text=(
        f"Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of "
        f"two rows and three columns, each showing a different emotion: {emotions}. {same} "
        f"{CHAR[c]['block']}. {SHEET_BG} {STYLE}"))


def keypose(c, action, bg):
    return dict(kind="대표 포즈", size=P, text=(
        f"Full-body character key art of a single character, {action}. {CHAR[c]['block']}. "
        f"Soft simple background: {bg}. {STYLE}"))


def scene(c, what, size=L):
    return dict(kind="장면", size=size, text=f"Animation film key frame, {what}. {CHAR[c]['block']}. {STYLE}")


def special(c, kind, text, size=L):
    return dict(kind=kind, size=size, text=f"{text} {CHAR[c]['block']}. {STYLE}")


SHOTS = {
    "niki": [
        turnaround("niki", "standing with her arms hanging straight down at her sides, the floppy cuffs of her "
                   "extremely long cream sleeves sticking out from under the cape and dangling a hand's length below "
                   "her wrists, closed and empty-looking, so that no hands come out of the sleeves in any view"),
        keypose("niki", "standing shyly with her shoulders curled inward and her gaze dropped to the tips of her "
                "boots, both floppy sleeve ends pressed together in front of her mouth and chin so that her hands "
                "stay completely hidden inside the extremely long cream sleeves, an old brass compass peeking out of "
                "the inner pocket of her open cape coat", "a pale cream wash with a faint wine-red vignette"),
        expressions("niki", "shy with eyes downcast behind her bangs and the long sleeve cuffs raised to cover her "
                    "mouth; nervous with a small wobbly smile and eyebrows tilted up; observant with calm sharp eyes "
                    "glancing sideways; teasing with a tiny lopsided smirk and one eye half closed; scared but "
                    "determined with wide eyes, knitted eyebrows and lips pressed tight; crying with relief, tears "
                    "streaming down while she wipes her eyes with a sleeve cuff",
                    same="Same hairstyle and outfit in every portrait."),
        scene("niki", "a small girl kneeling in a misty deep-green forest at dusk in front of a wilted sprout, gently "
              "cupping the sprout between the two floppy ends of her extremely long cream sleeves without taking her "
              "hands out, soft particles of sprout green, aqua and silver light glowing through the sleeve fabric and "
              "drifting onto the plant, quiet emotional moment, the wine-red coat contrasting with the green forest, "
              "painted forest background"),
        dict(special("niki_indoor", "성장 시트 (소매)", "Character growth sheet: three waist-up portraits of the same "
                     "girl side by side, telling her growth through the length of her sleeves: on the left, timid "
                     "with her head down, the extremely long cream sleeves dangling well past her hands so that no "
                     "hands are visible at all; in the middle, her gaze lifted a little, holding the sleeve ends "
                     "together in front of her chest with only the very tips of her fingers peeking out; on the "
                     "right, head raised with a brave small smile and her bangs tucked behind one ear, sleeves rolled "
                     "up to her elbows, bare hands holding a small envelope. Plain warm off-white paper background "
                     "without any lettering."), char="niki_indoor"),
    ],
    "putor": [
        turnaround("putor"),
        # 시트 3-2 버릇: '케이스를 가슴에 안고 뛰며' 의 케이스는 빈 부싯돌 케이스. 큰 가방은 몸의 절반을 가린다.
        keypose("putor", "hurrying forward with short anxious steps, hugging the small empty leather flint case to "
                "his chest with both hands, the huge medicine bag bouncing on its strap and covering half of his round "
                "body, glass vials jingling, his white beard bristling with nervousness",
                "a dusty antique-brass and parchment wash"),
        expressions("putor", "worried with a deep frown and his beard drooping; fussy scolding with a raised stubby "
                    "finger and puffed cheeks; frightened with wide eyes and his white beard bristling straight out "
                    "like a brush; relieved with a soft smile and the beard hanging limp and curved; muttering herb "
                    "names like a spell with his eyes squeezed shut; peering kindly over his half-moon glasses with "
                    "his head tilted"),
        # 두 인물이 비슷하게 묘사되면 모델이 한 사람으로 합쳐 버려서, 환자는 성별·머리·옷 색이 확연히 다르게 적는다
        scene("putor", "two people on a forest path: on the right, a tall young woman traveler with a long red braid "
              "and a blue dress lies on the ground with her leg wrapped in a white bandage; on the left, the small "
              "round dwarf healer kneels beside her and sprinkles green herb powder from a glass vial onto the "
              "bandage with trembling but steady hands, his medicine bag open beside him, brave despite his fear, "
              "cool blue-gray forest with warm light on the two of them"),
        special("putor", "소품 시트", "Prop design sheet for a dwarf healer laid out neatly: a huge boxy worn leather "
                "medicine bag opened to show rows of small compartments with glass vials and herb pouches, a small "
                "empty leather flint case with a tiny blank paper tag, spare half-moon reading glasses, an "
                "antique-brass healer badge, a scrap of coarse filter cloth, small bundles of dried herbs, with the "
                "healer himself standing right next to the bag for scale, the bag almost as big as he is. Plain warm "
                "off-white paper background without any lettering."),
    ],
    "quillins": [
        dict(turnaround("quillins_hood"), char="quillins_hood"),
        dict(scene("quillins_hood", "a faceless dark silhouette standing on a rocky shore at night, the black "
                   "hooded cloak drawn like spreading ink-wash smudges, a low camera angle, cold blue-gray "
                   "moonlight, the cloak edge dragging over wet stones, mysterious and frightening without gore",
                   size=P), char="quillins_hood"),
        dict(special("quillins_reveal", "정체 공개 초상", "Bust portrait of the unhooded man looking down with "
                     "tired sorrowful eyes, the hood resting on his shoulders, dim blue-gray light with a faint "
                     "warm glint from the coral-pink chieftain's seal.", size=P), char="quillins_reveal"),
        dict(scene("quillins_reveal", "the gaunt man kneeling on wet sand at the edge of the sea at sunrise, gently "
                   "whispering to a young gray seal pup with a bandaged flipper lying in front of him, his only warm "
                   "moment, softer colors and warm light on his face"),
             char="quillins_reveal"),
        dict(special("quillins_reveal", "손 클로즈업", "Extreme close-up of two hands only, filling the whole "
                     "frame: a black-gloved right hand slowly pulls the black leather glove off the left hand, "
                     "revealing bluish-black decayed skin cracked like dry mud with small white salt crystals in the "
                     "cracks; only the hands and the dark indigo coat cuffs are visible, no face in the picture, "
                     "quiet and sad mood, not gory.", size=S),
             char="quillins_reveal"),
    ],
    "james": [
        turnaround("james"),
        keypose("james", "crouching down low on one knee and smiling warmly straight at the viewer at eye level, "
                "one hand resting on his knee, a metal watering can on the ground beside him",
                "a soft slate-blue and cream wash"),
        # 블록이 긴 팔다리·장화를 강조해서 전신이 섞여 나와, 가슴 위로만 자르라고 따로 적는다
        expressions("james", "warm smile with crinkled eye lines; sheepish laugh while scratching the back of his "
                    "head after a clumsy mistake; patiently waiting with a calm gentle gaze; worried with raised "
                    "eyebrows; telling a gentle joke with one eyebrow up and a playful grin; quiet sadness with "
                    "downcast eyes and a faint smile",
                    same="Same hairstyle, outfit and accessories in every portrait. Every portrait is cropped at the "
                         "chest, so no legs, boots or full-body figures appear anywhere on the sheet."),
        scene("james", "the tall gentle father watering rows of plants inside a sunlit glass greenhouse, warm "
              "light streaming through foggy glass panes, steam and green leaves, peaceful morning"),
        # 'ducking' 이라고 쓰면 오리를 그려서 동작을 풀어 쓴다
        scene("james", "the very tall lanky father bending his long neck to pass under a low wooden doorframe of a "
              "cozy cottage and bumping his forehead lightly on the frame, rubbing his forehead and laughing at "
              "himself, warm interior light, gentle comedy", size=P),
    ],
    "beth": [
        turnaround("beth"),
        keypose("beth", "standing upright and calmly pouring tea from a ceramic teapot with precise graceful "
                "hands, a small notebook tucked in her apron pocket", "a soft deep-forest-green and cream wash"),
        expressions("beth", "calm neutral composure with straight eyebrows; a gentle subtle smile; firm determined "
                    "look while speaking a short encouraging line; focused downward gaze as if writing in her "
                    "notebook; a secretive sideways glance with a faint amber glint in her eyes; quiet worry with "
                    "lips pressed together"),
        scene("beth", "the calm mother checking seedlings in a greenhouse at evening, the plants subtly leaning "
              "toward her, a barely visible faint blue-green glimmer passing over a leaf near her fingertip, "
              "warm lamp light, quiet mysterious mood"),
        scene("beth", "the mother standing protectively with one arm spread out in front of her, strong wind, her "
              "loosely tied wavy black hair coming loose and flowing dramatically for the first time, a stormy "
              "dark-green background, intense determined eyes", size=P),
    ],
    "taoba": [
        turnaround("taoba"),
        keypose("taoba", "laughing heartily with his arms open wide, wearing a worn straw hat, a tiny seedling pot "
                "held very gently in one big hand", "a soft sage-green and dew-glass wash"),
        expressions("taoba", "booming open-mouthed laugh with his eyes shut into happy curves; whispering softly to "
                    "a sick plant with gentle eyes; gentle concern with raised bushy eyebrows; surprised with wide "
                    "round eyes and an open mouth inside his beard; telling a joke with a wink; serious protective "
                    "look with furrowed brows"),
        scene("taoba", "the round gardener kneeling inside his overgrown glass greenhouse full of potted plants "
              "with small wooden name tags, a small mist sprayer and dewy glass, examining a tiny seedling "
              "with surprisingly delicate fingers, warm green light"),
        scene("taoba", "the round gardener caught and tangled in thick dark creeping vines inside a dim greenhouse, "
              "struggling but still grinning bravely, dramatic but not violent, cool shadows with warm highlights",
              size=P),
    ],
    "ilia": [
        turnaround("ilia"),
        keypose("ilia", "standing tall with one hand on her hip and the other holding an open folding notebook, "
                "giving brisk instructions, then glancing back with a warm smile",
                "a soft powder-blue and sage-green wash"),
        expressions("ilia", "firm scolding with a raised finger and her ponytail sticking straight up; warm "
                    "big-sister smile with the ponytail hanging softly; confident and focused with sharp eyes; "
                    "exasperated sigh with closed eyes; gentle reassuring look with her head tilted as if asking are "
                    "you okay; laughing openly"),
        scene("ilia", f"inside a sunny greenhouse, the young woman kneels on the left and ties her own powder-blue "
              f"hair ribbon into the black bob hair of {NIKI_GUEST}, who stands on the right, tender big-sister "
              f"moment, warm light"),
        scene("ilia", "the young woman walking briskly between rows of seedlings in a greenhouse, checking a care "
              "schedule in her folding notebook with a pencil, garden scissors at her waist, busy morning light",
              size=P),
    ],
    "iloke": [
        turnaround("iloke"),
        keypose("iloke", "silently holding out a folded handkerchief with one gloved hand, the other hand holding "
                "a closed umbrella, a tiny warm smile only in his eyes", "a soft deep-forest-green and cream wash"),
        expressions("iloke", "calm stoic face; a tiny smile only in his eyes; quiet concern with slightly knitted "
                    "brows; slight embarrassment looking away with a faint blush; firm protective look; relaxed and "
                    "sleepy with half-closed eyes"),
        scene("iloke", f"rainy day on a garden path, the tall quiet young man on the left tilts his umbrella over "
              f"{NIKI_GUEST}, who walks on the right, his gloved hand lightly holding her arm over her sleeve, his "
              f"own shoulder getting wet, soft gray rain and green leaves, quiet kindness"),
        scene("iloke", "the tall young man walking one step ahead on a muddy garden path carrying two heavy clay "
              "flower pots, clearing the way, leather gloves, calm steady stride, morning mist", size=P),
    ],
    "iluki": [
        turnaround("iluki"),
        keypose("iluki", "in a dynamic exaggerated pose, leaning forward and winking while holding up a little toy "
                "frog toward the viewer to make someone laugh", "a soft mustard-yellow and cream wash"),
        expressions("iluki", "huge mischievous grin showing his teeth; exaggerated shocked face with bulging eyes and "
                    "a dropped jaw; pouting with puffed cheeks after being scolded; sneaky plotting look with narrowed "
                    "eyes; laughing so hard that tears gather at the corners of his eyes; a rare sincere gentle smile"),
        scene("iluki", f"in a greenhouse, the playful young man crouches on the left and shows a toy insect and a toy "
              f"frog from his stuffed pockets to {NIKI_GUEST}, who stands on the right and giggles behind her sleeve "
              f"ends, cheerful warm light"),
        scene("iluki", f"comedic moment in a greenhouse: on the left, {ILIA_GUEST}, stands with one hand on her hip, "
              f"scolding and confiscating a toy frog and toy insects; on the right, the playful young man pouts with "
              f"puffed cheeks and his empty pockets turned out, warm light"),
    ],
}

ORDER = ["niki", "putor", "quillins", "james", "beth", "taoba", "ilia", "iloke", "iluki"]

# 검토 후 고른 후보: 컷 이름 -> (회차, 시드). 비어 있으면 기본 시드(캐릭터 시드 + 컷 번호).
PICK = {}


def all_jobs():
    jobs = []
    for i, key in enumerate(ORDER, 1):
        for n, shot in enumerate(SHOTS[key], 1):
            ck = shot.get("char", key)
            shot_id = f"{key}_{n}"
            w, h = shot["size"]
            rnd, seed = PICK.get(shot_id, (None, CHAR[ck]["seed"] + n))
            jobs.append({"char": key, "n": n, "id": shot_id, "kind": shot["kind"], "dir": f"{i:02d}_{key}",
                         "base_seed": CHAR[ck]["seed"] + n, "seed": seed, "round": rnd,
                         "prefix": f"niki_compass/{i:02d}_{key}/{shot_id}", "w": w, "h": h,
                         "text": shot["text"], "negative": NEGATIVE})
    return jobs


def load_final():
    """final_picks.json (컷별 사용 파일 순서) + final_steps.json (PNG 에서 꺼낸 단계 정보)를 읽는다. 없으면 None."""
    picks_p, steps_p = OUT / "final_picks.json", OUT / "final_steps.json"
    if not (picks_p.exists() and steps_p.exists()):
        return None
    picks = json.loads(picks_p.read_text(encoding="utf-8"))
    steps = json.loads(steps_p.read_text(encoding="utf-8"))
    return picks, steps


def final_lines(shot_id, jobs_by_id, final):
    """한 컷의 최종본 설명 (생성 원본 시드, 편집 단계 지시문, 최종 파일)."""
    picks, steps = final
    entry = picks["picks"].get(shot_id)
    if not entry:
        return ["- 최종본: [TBD]", ""]
    chain = entry["chain"] if isinstance(entry, dict) else entry
    base_shot = entry.get("base_shot", shot_id) if isinstance(entry, dict) else shot_id
    out = [f"- 최종 파일: `final/{picks['dest'][shot_id]}_00001_.png`"]
    if base_shot != shot_id:
        out.append(f"- 참고: 위 문장으로는 원하는 배치가 나오지 않아 `{base_shot}` 결과에서 편집으로 만들었습니다.")
    for k, path in enumerate(chain):
        st = steps.get(path, {})
        if k == 0:
            src = jobs_by_id[base_shot]
            ok = st.get("hash") == fnv(src["text"])
            where = "위 프롬프트" if base_shot == shot_id else f"`{base_shot}` 프롬프트"
            out.append(f"- 1단계 생성: {where}, seed {st.get('seed')}, {st.get('w')}×{st.get('h')}"
                       + ("" if ok else " (주의: 저장된 프롬프트가 위 문장과 다름)") + f"  ")
            out.append(f"  - 파일: `{path}`")
        else:
            out.append(f"- {k + 1}단계 편집 (Qwen-Image-Edit-2511, seed {st.get('seed')}):")
            out.append(f"  - 지시문: {st.get('text')}")
            out.append(f"  - 파일: `{path}`")
    return out + [""]


def build():
    jobs = all_jobs()
    final = load_final()
    jobs_by_id = {j["id"]: j for j in jobs}
    md = ["# 니키와 이상한 나침반 · 등장인물 컨셉아트 프롬프트", "",
          "- 모델: Z-Image Turbo (`z_image_turbo_bf16`, 텍스트 인코더 `qwen_3_4b`/lumina2, VAE `ae`)",
          "- 설정: 8 steps, cfg 1, res_multistep / simple, AuraFlow shift 3",
          "- 그림체: 2000년대 초 일본 손그림 판타지 장편 애니메이션 계열을 특징으로 묘사 (작품명은 넣지 않음)",
          "", "## 공통 그림체 문장", "", f"> {STYLE}", "",
          "## 공통 부정 프롬프트", "", "cfg 1 에서는 쓰이지 않습니다. 피할 것은 긍정 문장 안에 적었습니다.", "",
          f"> {NEGATIVE}", ""]
    for i, key in enumerate(ORDER, 1):
        title = CHAR[key]["name"] if key in CHAR else "퀼린스"
        md += [f"## {i}. {title}", ""]
        for j in (x for x in jobs if x["char"] == key):
            md += [f"### {i}-{j['n']}. {j['kind']}  ({j['w']}×{j['h']}, 기본 seed {j['seed']})", "", "```", j["text"],
                   "```", ""]
            if final:
                md += final_lines(j["id"], jobs_by_id, final)
    (OUT / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "prompts_en.md").write_text("\n".join(md), encoding="utf-8")
    print(f"{len(jobs)} jobs")


def fnv(s):
    """FNV-1a 32bit (UTF-8). 페이지에서 다시 조립한 프롬프트가 원문과 같은지 확인하는 데 쓴다."""
    h = 0x811C9DC5
    for x in s.encode("utf-8"):
        h = ((h ^ x) * 0x01000193) & 0xFFFFFFFF
    return format(h, "x")


def emit_js(specs):
    """후보 생성용 제출 코드 (submit.js). spec = '<캐릭터|컷,...>:<시드 수>:<회차>'.

    시드는 기본 시드 + 1000*k, 파일은 <캐릭터 폴더>/<회차>/<컷>_s<시드>.
    붙여 넣는 코드를 줄이려고 그림체 문장·배경 문장·캐릭터 블록을 토큰으로 바꿔 싣고 페이지에서 되살린다.
    되살린 문장의 해시가 원문 해시와 하나라도 다르면 제출하지 않는다.
    """
    jobs_all = all_jobs()
    blocks = sorted(((k, v["block"]) for k, v in CHAR.items()), key=lambda kv: -len(kv[1]))
    texts, hashes, out, used = [], [], [], {}
    for spec in specs:
        targets, variants, rnd = spec.split(":")
        want = set(targets.split(","))
        for j in jobs_all:
            if j["char"] not in want and j["id"] not in want:
                continue
            t = j["text"].replace(STYLE, "§S").replace(SHEET_BG, "§G")
            for k, b in blocks:
                if b in t:
                    t = t.replace(b, "§B{" + k + "}")
                    used[k] = b
            texts.append(t)
            hashes.append(fnv(j["text"]))
            for k in range(int(variants)):
                seed = j["base_seed"] + 1000 * k
                out.append({"prefix": f"niki_compass/{j['dir']}/{rnd}/{j['id']}_s{seed}", "w": j["w"], "h": j["h"],
                            "seed": seed, "t": len(texts) - 1})
    js = "\n".join([
        f"const NEG={json.dumps(NEGATIVE)};",
        f"const ST={json.dumps(STYLE)};",
        f"const BG={json.dumps(SHEET_BG)};",
        f"const B={json.dumps(used, ensure_ascii=False, indent=0)};",
        f"const T={json.dumps(texts, ensure_ascii=False, indent=0)};",
        f"const H={json.dumps(hashes)};",
        "const fnv = s => { let h = 0x811c9dc5; for (const x of new TextEncoder().encode(s)) "
        "{ h ^= x; h = Math.imul(h, 0x01000193) >>> 0; } return h.toString(16); };",
        "const X = T.map(t => t.split('§S').join(ST).split('§G').join(BG).replace(/§B\\{(\\w+)\\}/g, (_, k) => B[k]));",
        "const bad = X.map((x, i) => fnv(x) === H[i] ? null : i).filter(i => i !== null);",
        "if (bad.length) throw new Error('prompt mismatch: ' + bad.join(','));",
        f"const jobs={json.dumps(out)}.map(j => ({{...j, text: X[j.t], negative: NEG}}));",
        "const r = await mgsZ.submit(jobs);",
        "window.mgsLast = r;",
        "r.map(x => `${x.status} #${x.number} ${x.prefix.split('/').slice(-3).join('/')} ${x.err ? JSON.stringify(x.err) : ''}`)",
    ]) + "\n"
    path = OUT / "submit.js"
    path.write_text(js, encoding="utf-8")
    print(f"{len(out)} jobs -> {path.name} ({len(js)} bytes)")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "js":
        build()
        emit_js(sys.argv[2:])
    else:
        build()
