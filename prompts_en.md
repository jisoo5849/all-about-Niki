# 니키와 이상한 나침반 · 등장인물 컨셉아트 프롬프트

- 모델: Z-Image Turbo (`z_image_turbo_bf16`, 텍스트 인코더 `qwen_3_4b`/lumina2, VAE `ae`)
- 설정: 8 steps, cfg 1, res_multistep / simple, AuraFlow shift 3
- 그림체: 2000년대 초 일본 손그림 판타지 장편 애니메이션 계열을 특징으로 묘사 (작품명은 넣지 않음)

## 공통 그림체 문장

> Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.

## 공통 부정 프롬프트

cfg 1 에서는 쓰이지 않습니다. 피할 것은 긍정 문장 안에 적었습니다.

> photorealistic, 3d render, cgi, glossy, plastic skin, text, letters, watermark, logo, signature, blurry, deformed hands, extra fingers, extra limbs, duplicate face, cropped feet

## 1. 니키 그린

### 1-1. 턴어라운드  (1536×1024, 기본 seed 12101)

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, standing with her arms hanging straight down at her sides, the floppy cuffs of her extremely long cream sleeves sticking out from under the cape and dangling a hand's length below her wrists, closed and empty-looking, so that no hands come out of the sleeves in any view, identical outfit and proportions in all three views, evenly spaced. Niki, a shy 12-year-old girl whose hands are always hidden inside her overly long sleeves, very small and thin for her age (much shorter than the adults), chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing a wine-red cape coat over a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights and faded brown boots. Signature design point: the cream shirt sleeves are far longer than her arms, the soft sleeve cuffs droop past her fingertips and completely cover both hands, so no fingers are visible. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/01_niki/niki_1_turnaround_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13101, 1536×1024  
  - 파일: `01_niki/r3/niki_1_s13101_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 101):
  - 지시문: Make the girl's cream shirt sleeves longer in all three views so that the soft sleeve cuffs hang down past her hands and completely cover both hands like closed sleeve ends; no hands or fingers are visible anywhere. Keep everything else exactly the same: the same girl, pose, wine-red cape, colors, background and hand-drawn animation style.
  - 파일: `01_niki/r4_edit/niki_1_from-r3-s13101_e101_00001_.png`

### 1-2. 대표 포즈  (1024×1536, 기본 seed 12102)

```
Full-body character key art of a single character, standing shyly with her shoulders curled inward and her gaze dropped to the tips of her boots, both floppy sleeve ends pressed together in front of her mouth and chin so that her hands stay completely hidden inside the extremely long cream sleeves, an old brass compass peeking out of the inner pocket of her open cape coat. Niki, a shy 12-year-old girl whose hands are always hidden inside her overly long sleeves, very small and thin for her age (much shorter than the adults), chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing a wine-red cape coat over a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights and faded brown boots. Signature design point: the cream shirt sleeves are far longer than her arms, the soft sleeve cuffs droop past her fingertips and completely cover both hands, so no fingers are visible. Soft simple background: a pale cream wash with a faint wine-red vignette. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/01_niki/niki_2_keypose_00001_.png`
- 1단계 생성: 위 프롬프트, seed 14102, 1024×1536  
  - 파일: `01_niki/r3/niki_2_s14102_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 101):
  - 지시문: Make her cream sleeves longer so the soft sleeve ends completely cover both of her hands where she presses them to her mouth; no fingers are visible. Keep everything else exactly the same: face, hair, wine-red cape coat, the compass in her pocket, colors, background and hand-drawn animation style.
  - 파일: `01_niki/r4_edit/niki_2_from-r3-s14102_e101_00001_.png`

### 1-3. 표정 시트  (1536×1024, 기본 seed 12103)

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: shy with eyes downcast behind her bangs and the long sleeve cuffs raised to cover her mouth; nervous with a small wobbly smile and eyebrows tilted up; observant with calm sharp eyes glancing sideways; teasing with a tiny lopsided smirk and one eye half closed; scared but determined with wide eyes, knitted eyebrows and lips pressed tight; crying with relief, tears streaming down while she wipes her eyes with a sleeve cuff. Same hairstyle and outfit in every portrait. Niki, a shy 12-year-old girl whose hands are always hidden inside her overly long sleeves, very small and thin for her age (much shorter than the adults), chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing a wine-red cape coat over a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights and faded brown boots. Signature design point: the cream shirt sleeves are far longer than her arms, the soft sleeve cuffs droop past her fingertips and completely cover both hands, so no fingers are visible. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/01_niki/niki_3_expressions_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12103, 1536×1024  
  - 파일: `01_niki/r2/niki_3_s12103_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 505):
  - 지시문: Change the girl's hair color to jet black in all six portraits, the same jet-black bob in every portrait. Keep everything else exactly the same: faces, expressions, the long cream sleeves covering her hands, the wine-red cape, colors, background and hand-drawn animation style.
  - 파일: `01_niki/r5_edit/niki_3_from-r2-s12103_e505_00001_.png`
- 3단계 편집 (Qwen-Image-Edit-2511, seed 808):
  - 지시문: Change only two portraits. Top-right portrait: give her a tiny teasing smile with one eye slightly narrowed, as if she is making a small joke. Bottom-left portrait: give her calm, sharp, observant eyes glancing to the side with her mouth closed. Keep the other four portraits exactly the same, and keep the jet-black hair, the long cream sleeves covering her hands, the wine-red cape, colors, background and hand-drawn animation style exactly the same.
  - 파일: `01_niki/r6_edit/niki_3_from-r5-e505_e808_00001_.png`

### 1-4. 장면  (1536×1024, 기본 seed 12104)

```
Animation film key frame, a small girl kneeling in a misty deep-green forest at dusk in front of a wilted sprout, gently cupping the sprout between the two floppy ends of her extremely long cream sleeves without taking her hands out, soft particles of sprout green, aqua and silver light glowing through the sleeve fabric and drifting onto the plant, quiet emotional moment, the wine-red coat contrasting with the green forest, painted forest background. Niki, a shy 12-year-old girl whose hands are always hidden inside her overly long sleeves, very small and thin for her age (much shorter than the adults), chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing a wine-red cape coat over a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights and faded brown boots. Signature design point: the cream shirt sleeves are far longer than her arms, the soft sleeve cuffs droop past her fingertips and completely cover both hands, so no fingers are visible. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/01_niki/niki_4_forest_magic_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13104, 1536×1024  
  - 파일: `01_niki/r3/niki_4_s13104_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 101):
  - 지시문: Make her long cream sleeves cover both of her hands completely, so she cups the space above the sprout with the soft closed sleeve ends instead of bare hands, and faint sprout-green, aqua and silver light seeps out from the sleeve ends. No fingers are visible. Keep everything else exactly the same: the girl, her pose, the forest, colors and hand-drawn animation style.
  - 파일: `01_niki/r4_edit/niki_4_from-r3-s13104_e101_00001_.png`

### 1-5. 성장 시트 (소매)  (1536×1024, 기본 seed 12155)

```
Character growth sheet: three waist-up portraits of the same girl side by side, telling her growth through the length of her sleeves: on the left, timid with her head down, the extremely long cream sleeves dangling well past her hands so that no hands are visible at all; in the middle, her gaze lifted a little, holding the sleeve ends together in front of her chest with only the very tips of her fingers peeking out; on the right, head raised with a brave small smile and her bangs tucked behind one ear, sleeves rolled up to her elbows, bare hands holding a small envelope. Plain warm off-white paper background without any lettering. Niki, a shy 12-year-old girl, very small and thin for her age, chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing her indoor clothes without any coat: a loose cream cotton shirt with a small rounded flat collar and extremely long sleeves, dark mocha brown wool shorts, charcoal gray tights and faded brown boots, the same outfit in every drawing. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/01_niki/niki_5_sleeve_growth_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12155, 1536×1024  
  - 파일: `01_niki/r3/niki_5_s12155_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 202):
  - 지시문: Edit only the sleeves. Left girl: make her sleeves much longer so they hang past her hands and completely hide both hands. Middle girl: make her sleeves longer so they cover her hands, leaving only the tips of her fingers peeking out. Right girl: keep her sleeves rolled up and her bare hands holding the envelope. Keep everything else exactly the same: faces, hair, clothes, colors, background and hand-drawn animation style.
  - 파일: `01_niki/r4_edit/niki_5_from-r3-s12155_e202_00001_.png`
- 3단계 편집 (Qwen-Image-Edit-2511, seed 909):
  - 지시문: Edit only the middle girl. Pull her cream sleeves further down over her hands, so the sleeve cuffs cover her hands up to the first knuckles and only her small fingertips peek out from under the cuffs. Do not change the left girl or the right girl. Keep everything else exactly the same: faces, hair, clothes, colors, background and hand-drawn animation style.
  - 파일: `01_niki/r6_edit/niki_5_from-r4-e202_e909_00001_.png`

## 2. 푸토르

### 2-1. 턴어라운드  (1536×1024, 기본 seed 12201)

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. Putor, an elderly dwarf healer in his sixties, very short (about the height of a child) with a plump round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out of it, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses (lenses shaped like half circles with flat tops) perched on the tip of his nose, no hat, a plain dusty antique-brass travel coat with a few small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with many small compartments of clinking glass vials, carried on a shoulder strap in front of his belly, an empty small leather flint case with a little paper tag at his belt. Signature design point: a round silhouette half hidden behind the huge medicine bag, pointed ear tips, half-moon glasses that he wears in every drawing, and a long white beard tipped with green herb powder that bristles when he is scared and droops when he is relieved. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/02_putor/putor_1_turnaround_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12201, 1536×1024  
  - 파일: `02_putor/r2/putor_1_s12201_00001_.png`

### 2-2. 대표 포즈  (1024×1536, 기본 seed 12202)

```
Full-body character key art of a single character, hurrying forward with short anxious steps, hugging the small empty leather flint case to his chest with both hands, the huge medicine bag bouncing on its strap and covering half of his round body, glass vials jingling, his white beard bristling with nervousness. Putor, an elderly dwarf healer in his sixties, very short (about the height of a child) with a plump round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out of it, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses (lenses shaped like half circles with flat tops) perched on the tip of his nose, no hat, a plain dusty antique-brass travel coat with a few small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with many small compartments of clinking glass vials, carried on a shoulder strap in front of his belly, an empty small leather flint case with a little paper tag at his belt. Signature design point: a round silhouette half hidden behind the huge medicine bag, pointed ear tips, half-moon glasses that he wears in every drawing, and a long white beard tipped with green herb powder that bristles when he is scared and droops when he is relieved. Soft simple background: a dusty antique-brass and parchment wash. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/02_putor/putor_2_keypose_00001_.png`
- 1단계 생성: 위 프롬프트, seed 14202, 1024×1536  
  - 파일: `02_putor/r3/putor_2_s14202_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 111):
  - 지시문: Remove the faint dark shadow shaped like a person in the background behind the bag at the top left, and fill that area with the same plain dusty parchment wash as the rest of the background. Keep everything else exactly the same: the dwarf healer, his pose, the bag, the flint case, colors and hand-drawn animation style.
  - 파일: `02_putor/edit/putor_2_from-r3-s14202_e111_00001_.png`

### 2-3. 표정 시트  (1536×1024, 기본 seed 12203)

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: worried with a deep frown and his beard drooping; fussy scolding with a raised stubby finger and puffed cheeks; frightened with wide eyes and his white beard bristling straight out like a brush; relieved with a soft smile and the beard hanging limp and curved; muttering herb names like a spell with his eyes squeezed shut; peering kindly over his half-moon glasses with his head tilted. Same hairstyle, outfit and accessories in every portrait. Putor, an elderly dwarf healer in his sixties, very short (about the height of a child) with a plump round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out of it, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses (lenses shaped like half circles with flat tops) perched on the tip of his nose, no hat, a plain dusty antique-brass travel coat with a few small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with many small compartments of clinking glass vials, carried on a shoulder strap in front of his belly, an empty small leather flint case with a little paper tag at his belt. Signature design point: a round silhouette half hidden behind the huge medicine bag, pointed ear tips, half-moon glasses that he wears in every drawing, and a long white beard tipped with green herb powder that bristles when he is scared and droops when he is relieved. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/02_putor/putor_3_expressions_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12203, 1536×1024  
  - 파일: `02_putor/r2/putor_3_s12203_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 555):
  - 지시문: Add his small round glasses perched on the tip of his nose to every portrait where they are missing, the same glasses as in the other portraits, so he wears them in all six portraits. Keep everything else exactly the same: expressions, hair, beard, clothes, colors, background and hand-drawn animation style.
  - 파일: `02_putor/edit/putor_3_from-r2-s12203_e555_00001_.png`

### 2-4. 장면  (1536×1024, 기본 seed 12204)

```
Animation film key frame, two people on a forest path: on the right, a tall young woman traveler with a long red braid and a blue dress lies on the ground with her leg wrapped in a white bandage; on the left, the small round dwarf healer kneels beside her and sprinkles green herb powder from a glass vial onto the bandage with trembling but steady hands, his medicine bag open beside him, brave despite his fear, cool blue-gray forest with warm light on the two of them. Putor, an elderly dwarf healer in his sixties, very short (about the height of a child) with a plump round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out of it, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses (lenses shaped like half circles with flat tops) perched on the tip of his nose, no hat, a plain dusty antique-brass travel coat with a few small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with many small compartments of clinking glass vials, carried on a shoulder strap in front of his belly, an empty small leather flint case with a little paper tag at his belt. Signature design point: a round silhouette half hidden behind the huge medicine bag, pointed ear tips, half-moon glasses that he wears in every drawing, and a long white beard tipped with green herb powder that bristles when he is scared and droops when he is relieved. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/02_putor/putor_4_healing_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13204, 1536×1024  
  - 파일: `02_putor/r3/putor_4_s13204_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 111):
  - 지시문: Remove the faint dark shadow shaped like a person standing in the forest background at the top left, and fill that area with the same forest trees and leaves. Keep everything else exactly the same: the dwarf healer, the young woman with the bandaged leg, their poses, colors and hand-drawn animation style.
  - 파일: `02_putor/edit/putor_4_from-r3-s13204_e111_00001_.png`

### 2-5. 소품 시트  (1536×1024, 기본 seed 12205)

```
Prop design sheet for a dwarf healer laid out neatly: a huge boxy worn leather medicine bag opened to show rows of small compartments with glass vials and herb pouches, a small empty leather flint case with a tiny blank paper tag, spare half-moon reading glasses, an antique-brass healer badge, a scrap of coarse filter cloth, small bundles of dried herbs, with the healer himself standing right next to the bag for scale, the bag almost as big as he is. Plain warm off-white paper background without any lettering. Putor, an elderly dwarf healer in his sixties, very short (about the height of a child) with a plump round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out of it, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses (lenses shaped like half circles with flat tops) perched on the tip of his nose, no hat, a plain dusty antique-brass travel coat with a few small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with many small compartments of clinking glass vials, carried on a shoulder strap in front of his belly, an empty small leather flint case with a little paper tag at his belt. Signature design point: a round silhouette half hidden behind the huge medicine bag, pointed ear tips, half-moon glasses that he wears in every drawing, and a long white beard tipped with green herb powder that bristles when he is scared and droops when he is relieved. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/02_putor/putor_5_props_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12205, 1536×1024  
  - 파일: `02_putor/r2/putor_5_s12205_00001_.png`

## 3. 퀼린스

### 3-1. 턴어라운드  (1536×1024, 기본 seed 12301)

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. Quillins, a tall thin man with angular shoulders, wrapped in a worn ink-black hooded cloak, the deep hood hides his whole face in complete shadow with no visible features, black leather gloves, faded fur trim and bone toggles on the cloak, the hem dragging on the ground, a glimpse of an old dark indigo coat underneath. Signature design point: a faceless ink-black silhouette, the inside of the hood is pure black shadow like spreading ink with no eyes, nose or mouth, only the black-gloved hands stand out. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/03_quillins/quillins_1_hooded_turnaround_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12301, 1536×1024  
  - 파일: `03_quillins/r1/quillins_1_s12301_00001_.png`

### 3-2. 장면  (1024×1536, 기본 seed 12302)

```
Animation film key frame, a faceless dark silhouette standing on a rocky shore at night, the black hooded cloak drawn like spreading ink-wash smudges, a low camera angle, cold blue-gray moonlight, the cloak edge dragging over wet stones, mysterious and frightening without gore. Quillins, a tall thin man with angular shoulders, wrapped in a worn ink-black hooded cloak, the deep hood hides his whole face in complete shadow with no visible features, black leather gloves, faded fur trim and bone toggles on the cloak, the hem dragging on the ground, a glimpse of an old dark indigo coat underneath. Signature design point: a faceless ink-black silhouette, the inside of the hood is pure black shadow like spreading ink with no eyes, nose or mouth, only the black-gloved hands stand out. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/03_quillins/quillins_2_night_shore_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13302, 1024×1536  
  - 파일: `03_quillins/r1/quillins_2_s13302_00001_.png`

### 3-3. 정체 공개 초상  (1024×1536, 기본 seed 12353)

```
Bust portrait of the unhooded man looking down with tired sorrowful eyes, the hood resting on his shoulders, dim blue-gray light with a faint warm glint from the coral-pink chieftain's seal. Quillins, an old man in his late fifties, clearly aged, tall and thin with angular shoulders, his hood pushed back off his head and hanging behind his neck, a long gaunt deeply lined face with sunken cheeks and hollow tired eyes, black hair heavily streaked with white, dark gray eyes with a black tint, patches of bluish-black decayed skin on his neck and jaw, cracked like dry mud with small white salt crystals in the cracks, an old dark indigo long chieftain coat with a small round coral-pink chieftain's seal pinned at the chest, a worn ink-black cloak on his shoulders, black leather gloves. Signature design point: an aged gaunt face, small white salt crystals in the cracks of the bluish-black decayed skin, and black leather gloves that hide his sick hands. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/03_quillins/quillins_3_reveal_portrait_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12353, 1024×1536  
  - 파일: `03_quillins/r2/quillins_3_s12353_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 222):
  - 지시문: Lower his hood so it rests on his shoulders and his head is uncovered, showing his black hair streaked with white. Keep everything else exactly the same: his aged face, the decayed skin patch, the coral-pink seal, the cloak, the gloves, colors, lighting and hand-drawn animation style.
  - 파일: `03_quillins/edit/quillins_3_from-r2-s12353_e222_00001_.png`

### 3-4. 장면  (1536×1024, 기본 seed 12354)

```
Animation film key frame, the gaunt man kneeling on wet sand at the edge of the sea at sunrise, gently whispering to a young gray seal pup with a bandaged flipper lying in front of him, his only warm moment, softer colors and warm light on his face. Quillins, an old man in his late fifties, clearly aged, tall and thin with angular shoulders, his hood pushed back off his head and hanging behind his neck, a long gaunt deeply lined face with sunken cheeks and hollow tired eyes, black hair heavily streaked with white, dark gray eyes with a black tint, patches of bluish-black decayed skin on his neck and jaw, cracked like dry mud with small white salt crystals in the cracks, an old dark indigo long chieftain coat with a small round coral-pink chieftain's seal pinned at the chest, a worn ink-black cloak on his shoulders, black leather gloves. Signature design point: an aged gaunt face, small white salt crystals in the cracks of the bluish-black decayed skin, and black leather gloves that hide his sick hands. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/03_quillins/quillins_4_seal_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13354, 1536×1024  
  - 파일: `03_quillins/r2/quillins_4_s13354_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 222):
  - 지시문: Change only his hair color: make his hair black, streaked with white. Keep everything else exactly the same: his aged face, pose, the seal pup, the beach at sunrise, colors and hand-drawn animation style.
  - 파일: `03_quillins/edit/quillins_4_from-r2-s13354_e222_00001_.png`
- 3단계 편집 (Qwen-Image-Edit-2511, seed 333):
  - 지시문: Add a few clear white streaks to his black hair at the front and the temples, like an older man's graying hair. Keep everything else exactly the same: his face, pose, the seal pup, the beach at sunrise, colors and hand-drawn animation style.
  - 파일: `03_quillins/edit/quillins_4_from-edit-e222_e333_00001_.png`

### 3-5. 손 클로즈업  (1024×1024, 기본 seed 12355)

```
Extreme close-up of two hands only, filling the whole frame: a black-gloved right hand slowly pulls the black leather glove off the left hand, revealing bluish-black decayed skin cracked like dry mud with small white salt crystals in the cracks; only the hands and the dark indigo coat cuffs are visible, no face in the picture, quiet and sad mood, not gory. Quillins, an old man in his late fifties, clearly aged, tall and thin with angular shoulders, his hood pushed back off his head and hanging behind his neck, a long gaunt deeply lined face with sunken cheeks and hollow tired eyes, black hair heavily streaked with white, dark gray eyes with a black tint, patches of bluish-black decayed skin on his neck and jaw, cracked like dry mud with small white salt crystals in the cracks, an old dark indigo long chieftain coat with a small round coral-pink chieftain's seal pinned at the chest, a worn ink-black cloak on his shoulders, black leather gloves. Signature design point: an aged gaunt face, small white salt crystals in the cracks of the bluish-black decayed skin, and black leather gloves that hide his sick hands. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/03_quillins/quillins_5_glove_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13355, 1024×1024  
  - 파일: `03_quillins/r2/quillins_5_s13355_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 222):
  - 지시문: Change only his hair color: make his hair black, streaked with white. Keep everything else exactly the same: his aged face, the gloves, the decayed hand with salt crystals, colors and hand-drawn animation style.
  - 파일: `03_quillins/edit/quillins_5_from-r2-s13355_e222_00001_.png`

## 4. 제임스 그린

### 4-1. 턴어라운드  (1536×1024, 기본 seed 12401)

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. James, a gentle father in his early forties with the clearly adult face of a forty-year-old man, not a young man: a long face with high cheekbones, faint lines on his forehead and around his eyes and mouth, slightly tired kind eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind adult face with laugh lines, and three stray strands of hair sticking out from his messy brown hair. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/04_james/james_1_turnaround_00001_.png`
- 1단계 생성: 위 프롬프트, seed 14401, 1536×1024  
  - 파일: `04_james/r2/james_1_s14401_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 282):
  - 지시문: Make the man look about forty years old instead of a teenager in all three views: a slightly longer adult face with a firmer jaw and subtle laugh lines at the corners of his eyes, a calm kind expression, no heavy wrinkles and no tired look. Keep his messy brown hair with the three stray strands, his clothes, poses, tall lanky body, colors, background and hand-drawn animation style exactly the same.
  - 파일: `04_james/edit2/james_1_from-r2-s14401_e282_00001_.png`

### 4-2. 대표 포즈  (1024×1536, 기본 seed 12402)

```
Full-body character key art of a single character, crouching down low on one knee and smiling warmly straight at the viewer at eye level, one hand resting on his knee, a metal watering can on the ground beside him. James, a gentle father in his early forties with the clearly adult face of a forty-year-old man, not a young man: a long face with high cheekbones, faint lines on his forehead and around his eyes and mouth, slightly tired kind eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind adult face with laugh lines, and three stray strands of hair sticking out from his messy brown hair. Soft simple background: a soft slate-blue and cream wash. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/04_james/james_2_keypose_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13402, 1024×1536  
  - 파일: `04_james/r2/james_2_s13402_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 171):
  - 지시문: Make the man look about forty years old instead of a teenager: a slightly longer adult face with a firmer jaw and subtle laugh lines at the corners of his eyes. Keep his facial expression exactly the same, with no heavy wrinkles and no tired look. Keep his messy brown hair with the three stray strands, his clothes, pose, tall lanky body, colors, background and hand-drawn animation style exactly the same.
  - 파일: `04_james/edit2/james_2_from-r2-s13402_e171_00001_.png`

### 4-3. 표정 시트  (1536×1024, 기본 seed 12403)

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: warm smile with crinkled eye lines; sheepish laugh while scratching the back of his head after a clumsy mistake; patiently waiting with a calm gentle gaze; worried with raised eyebrows; telling a gentle joke with one eyebrow up and a playful grin; quiet sadness with downcast eyes and a faint smile. Same hairstyle, outfit and accessories in every portrait. Every portrait is cropped at the chest, so no legs, boots or full-body figures appear anywhere on the sheet. James, a gentle father in his early forties with the clearly adult face of a forty-year-old man, not a young man: a long face with high cheekbones, faint lines on his forehead and around his eyes and mouth, slightly tired kind eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind adult face with laugh lines, and three stray strands of hair sticking out from his messy brown hair. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/04_james/james_3_expressions_00001_.png`
- 참고: 위 문장으로는 원하는 배치가 나오지 않아 `james_1` 결과에서 편집으로 만들었습니다.
- 1단계 생성: `james_1` 프롬프트, seed 14401, 1536×1024  
  - 파일: `04_james/r2/james_1_s14401_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 282):
  - 지시문: Make the man look about forty years old instead of a teenager in all three views: a slightly longer adult face with a firmer jaw and subtle laugh lines at the corners of his eyes, a calm kind expression, no heavy wrinkles and no tired look. Keep his messy brown hair with the three stray strands, his clothes, poses, tall lanky body, colors, background and hand-drawn animation style exactly the same.
  - 파일: `04_james/edit2/james_1_from-r2-s14401_e282_00001_.png`
- 3단계 편집 (Qwen-Image-Edit-2511, seed 494):
  - 지시문: Turn this character sheet into an expression sheet of the same man: six head-and-shoulders portraits of him arranged in a neat grid of two rows and three columns on the same plain warm off-white paper background, each cropped at the chest, each showing a different emotion: warm smile with crinkled eye lines; sheepish laugh while scratching the back of his head; patiently waiting with a calm gentle gaze; worried with raised eyebrows; telling a gentle joke with one eyebrow up and a playful grin; quiet sadness with downcast eyes and a faint smile. Keep his face and age, his messy brown hair with the three stray strands, his slate-blue cardigan and cream shirt, and the hand-drawn animation style exactly the same. No full-body figures, no legs and no boots.
  - 파일: `04_james/edit2/james_3_from-james1-edit2-e282_e494_00001_.png`

### 4-4. 장면  (1536×1024, 기본 seed 12404)

```
Animation film key frame, the tall gentle father watering rows of plants inside a sunlit glass greenhouse, warm light streaming through foggy glass panes, steam and green leaves, peaceful morning. James, a gentle father in his early forties with the clearly adult face of a forty-year-old man, not a young man: a long face with high cheekbones, faint lines on his forehead and around his eyes and mouth, slightly tired kind eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind adult face with laugh lines, and three stray strands of hair sticking out from his messy brown hair. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/04_james/james_4_greenhouse_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12404, 1536×1024  
  - 파일: `04_james/r2/james_4_s12404_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 282):
  - 지시문: Make the man look about forty years old instead of a teenager: a slightly longer adult face with a firmer jaw and subtle laugh lines at the corners of his eyes. Keep his facial expression exactly the same, with no heavy wrinkles and no tired look. Keep his messy brown hair with the three stray strands, his clothes, pose, tall lanky body, colors, background and hand-drawn animation style exactly the same.
  - 파일: `04_james/edit2/james_4_from-r2-s12404_e282_00001_.png`

### 4-5. 장면  (1024×1536, 기본 seed 12405)

```
Animation film key frame, the very tall lanky father bending his long neck to pass under a low wooden doorframe of a cozy cottage and bumping his forehead lightly on the frame, rubbing his forehead and laughing at himself, warm interior light, gentle comedy. James, a gentle father in his early forties with the clearly adult face of a forty-year-old man, not a young man: a long face with high cheekbones, faint lines on his forehead and around his eyes and mouth, slightly tired kind eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind adult face with laugh lines, and three stray strands of hair sticking out from his messy brown hair. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/04_james/james_5_doorframe_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12405, 1024×1536  
  - 파일: `04_james/r2/james_5_s12405_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 282):
  - 지시문: Make the man look about forty years old instead of a teenager: a slightly longer adult face with a firmer jaw and subtle laugh lines at the corners of his eyes. Keep his facial expression exactly the same, with no heavy wrinkles and no tired look. Keep his messy brown hair with the three stray strands, his clothes, pose, tall lanky body, colors, background and hand-drawn animation style exactly the same.
  - 파일: `04_james/edit2/james_5_from-r2-s12405_e282_00001_.png`

## 5. 베스 그린

### 5-1. 턴어라운드  (1536×1024, 기본 seed 12501)

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest. Signature design point: a tall straight upright silhouette drawn with thin lines, the long wavy hair simplified into gentle wave lines, and a small amber brooch that matches the faint amber glint in her eyes. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/05_beth/beth_1_turnaround_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13501, 1536×1024  
  - 파일: `05_beth/r1/beth_1_s13501_00001_.png`

### 5-2. 대표 포즈  (1024×1536, 기본 seed 12502)

```
Full-body character key art of a single character, standing upright and calmly pouring tea from a ceramic teapot with precise graceful hands, a small notebook tucked in her apron pocket. Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest. Signature design point: a tall straight upright silhouette drawn with thin lines, the long wavy hair simplified into gentle wave lines, and a small amber brooch that matches the faint amber glint in her eyes. Soft simple background: a soft deep-forest-green and cream wash. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/05_beth/beth_2_tea_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13502, 1024×1536  
  - 파일: `05_beth/r1/beth_2_s13502_00001_.png`

### 5-3. 표정 시트  (1536×1024, 기본 seed 12503)

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: calm neutral composure with straight eyebrows; a gentle subtle smile; firm determined look while speaking a short encouraging line; focused downward gaze as if writing in her notebook; a secretive sideways glance with a faint amber glint in her eyes; quiet worry with lips pressed together. Same hairstyle, outfit and accessories in every portrait. Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest. Signature design point: a tall straight upright silhouette drawn with thin lines, the long wavy hair simplified into gentle wave lines, and a small amber brooch that matches the faint amber glint in her eyes. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/05_beth/beth_3_expressions_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13503, 1536×1024  
  - 파일: `05_beth/r1/beth_3_s13503_00001_.png`

### 5-4. 장면  (1536×1024, 기본 seed 12504)

```
Animation film key frame, the calm mother checking seedlings in a greenhouse at evening, the plants subtly leaning toward her, a barely visible faint blue-green glimmer passing over a leaf near her fingertip, warm lamp light, quiet mysterious mood. Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest. Signature design point: a tall straight upright silhouette drawn with thin lines, the long wavy hair simplified into gentle wave lines, and a small amber brooch that matches the faint amber glint in her eyes. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/05_beth/beth_4_greenhouse_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12504, 1536×1024  
  - 파일: `05_beth/r1/beth_4_s12504_00001_.png`

### 5-5. 장면  (1024×1536, 기본 seed 12505)

```
Animation film key frame, the mother standing protectively with one arm spread out in front of her, strong wind, her loosely tied wavy black hair coming loose and flowing dramatically for the first time, a stormy dark-green background, intense determined eyes. Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest. Signature design point: a tall straight upright silhouette drawn with thin lines, the long wavy hair simplified into gentle wave lines, and a small amber brooch that matches the faint amber glint in her eyes. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/05_beth/beth_5_protect_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12505, 1024×1536  
  - 파일: `05_beth/r1/beth_5_s12505_00001_.png`

## 6. 타오바

### 6-1. 턴어라운드  (1536×1024, 기본 seed 12601)

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. Taoba, a jolly stocky gardener in his mid-fifties, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big bush-like shape around his face, a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass. Signature design point: his hair and beard are drawn as one big round bush-like mass around his face, on a big round pot-bellied body. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/06_taoba/taoba_1_turnaround_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12601, 1536×1024  
  - 파일: `06_taoba/r1/taoba_1_s12601_00001_.png`

### 6-2. 대표 포즈  (1024×1536, 기본 seed 12602)

```
Full-body character key art of a single character, laughing heartily with his arms open wide, wearing a worn straw hat, a tiny seedling pot held very gently in one big hand. Taoba, a jolly stocky gardener in his mid-fifties, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big bush-like shape around his face, a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass. Signature design point: his hair and beard are drawn as one big round bush-like mass around his face, on a big round pot-bellied body. Soft simple background: a soft sage-green and dew-glass wash. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/06_taoba/taoba_2_keypose_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12602, 1024×1536  
  - 파일: `06_taoba/r1/taoba_2_s12602_00001_.png`

### 6-3. 표정 시트  (1536×1024, 기본 seed 12603)

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: booming open-mouthed laugh with his eyes shut into happy curves; whispering softly to a sick plant with gentle eyes; gentle concern with raised bushy eyebrows; surprised with wide round eyes and an open mouth inside his beard; telling a joke with a wink; serious protective look with furrowed brows. Same hairstyle, outfit and accessories in every portrait. Taoba, a jolly stocky gardener in his mid-fifties, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big bush-like shape around his face, a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass. Signature design point: his hair and beard are drawn as one big round bush-like mass around his face, on a big round pot-bellied body. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/06_taoba/taoba_3_expressions_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12603, 1536×1024  
  - 파일: `06_taoba/r1/taoba_3_s12603_00001_.png`

### 6-4. 장면  (1536×1024, 기본 seed 12604)

```
Animation film key frame, the round gardener kneeling inside his overgrown glass greenhouse full of potted plants with small wooden name tags, a small mist sprayer and dewy glass, examining a tiny seedling with surprisingly delicate fingers, warm green light. Taoba, a jolly stocky gardener in his mid-fifties, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big bush-like shape around his face, a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass. Signature design point: his hair and beard are drawn as one big round bush-like mass around his face, on a big round pot-bellied body. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/06_taoba/taoba_4_greenhouse_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12604, 1536×1024  
  - 파일: `06_taoba/r1/taoba_4_s12604_00001_.png`

### 6-5. 장면  (1024×1536, 기본 seed 12605)

```
Animation film key frame, the round gardener caught and tangled in thick dark creeping vines inside a dim greenhouse, struggling but still grinning bravely, dramatic but not violent, cool shadows with warm highlights. Taoba, a jolly stocky gardener in his mid-fifties, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big bush-like shape around his face, a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass. Signature design point: his hair and beard are drawn as one big round bush-like mass around his face, on a big round pot-bellied body. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/06_taoba/taoba_5_vines_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12605, 1024×1536  
  - 파일: `06_taoba/r1/taoba_5_s12605_00001_.png`

## 7. 일리아

### 7-1. 턴어라운드  (1536×1024, 기본 seed 12701)

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. Ilia, a slim young woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, a practical apron, a folding notebook and small garden scissors hanging at her waist. Signature design point: a straight upright posture and a brown ponytail tied with a powder-blue ribbon, the ponytail stands up when she is angry and droops softly when she is gentle. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/07_ilia/ilia_1_turnaround_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12701, 1536×1024  
  - 파일: `07_ilia/r1/ilia_1_s12701_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 131):
  - 지시문: Change only the color of the young woman's hair ribbon to a light powder blue in every view. Keep everything else exactly the same: her face, brown ponytail, clothes, pose, colors, background and hand-drawn animation style.
  - 파일: `07_ilia/edit/ilia_1_from-r1-s12701_e131_00001_.png`

### 7-2. 대표 포즈  (1024×1536, 기본 seed 12702)

```
Full-body character key art of a single character, standing tall with one hand on her hip and the other holding an open folding notebook, giving brisk instructions, then glancing back with a warm smile. Ilia, a slim young woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, a practical apron, a folding notebook and small garden scissors hanging at her waist. Signature design point: a straight upright posture and a brown ponytail tied with a powder-blue ribbon, the ponytail stands up when she is angry and droops softly when she is gentle. Soft simple background: a soft powder-blue and sage-green wash. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/07_ilia/ilia_2_keypose_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12702, 1024×1536  
  - 파일: `07_ilia/r1/ilia_2_s12702_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 353):
  - 지시문: Change only the color of her small hair ribbon to a light powder blue. Keep the single figure and the composition exactly the same, and keep her face, brown ponytail, clothes, pose, colors, background and hand-drawn animation style unchanged.
  - 파일: `07_ilia/edit2/ilia_2_from-r1-s12702_e353_00001_.png`

### 7-3. 표정 시트  (1536×1024, 기본 seed 12703)

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: firm scolding with a raised finger and her ponytail sticking straight up; warm big-sister smile with the ponytail hanging softly; confident and focused with sharp eyes; exasperated sigh with closed eyes; gentle reassuring look with her head tilted as if asking are you okay; laughing openly. Same hairstyle, outfit and accessories in every portrait. Ilia, a slim young woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, a practical apron, a folding notebook and small garden scissors hanging at her waist. Signature design point: a straight upright posture and a brown ponytail tied with a powder-blue ribbon, the ponytail stands up when she is angry and droops softly when she is gentle. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/07_ilia/ilia_3_expressions_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13703, 1536×1024  
  - 파일: `07_ilia/r1/ilia_3_s13703_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 131):
  - 지시문: Change only the color of the young woman's hair ribbon to a light powder blue in every view. Keep everything else exactly the same: her face, brown ponytail, clothes, pose, colors, background and hand-drawn animation style.
  - 파일: `07_ilia/edit/ilia_3_from-r1-s13703_e131_00001_.png`

### 7-4. 장면  (1536×1024, 기본 seed 12704)

```
Animation film key frame, inside a sunny greenhouse, the young woman kneels on the left and ties her own powder-blue hair ribbon into the black bob hair of a small shy 12-year-old girl with a jet-black bob in a wine-red cape coat, the floppy ends of her extremely long cream sleeves dangling over her hands so that her hands stay hidden, who stands on the right, tender big-sister moment, warm light. Ilia, a slim young woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, a practical apron, a folding notebook and small garden scissors hanging at her waist. Signature design point: a straight upright posture and a brown ponytail tied with a powder-blue ribbon, the ponytail stands up when she is angry and droops softly when she is gentle. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/07_ilia/ilia_4_ribbon_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13704, 1536×1024  
  - 파일: `07_ilia/r1/ilia_4_s13704_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 131):
  - 지시문: Make the young woman's own hair ribbon light powder blue. Move the light powder-blue ribbon she is tying from the small girl's collar into the small girl's black bob hair, as a small bow at the side of her head, with the young woman's hands tying it there. Keep the small girl's long cream sleeves covering her hands. Keep everything else exactly the same: faces, clothes, the greenhouse, colors and hand-drawn animation style.
  - 파일: `07_ilia/edit/ilia_4_from-r1-s13704_e131_00001_.png`

### 7-5. 장면  (1024×1536, 기본 seed 12705)

```
Animation film key frame, the young woman walking briskly between rows of seedlings in a greenhouse, checking a care schedule in her folding notebook with a pencil, garden scissors at her waist, busy morning light. Ilia, a slim young woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, a practical apron, a folding notebook and small garden scissors hanging at her waist. Signature design point: a straight upright posture and a brown ponytail tied with a powder-blue ribbon, the ponytail stands up when she is angry and droops softly when she is gentle. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/07_ilia/ilia_5_greenhouse_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12705, 1024×1536  
  - 파일: `07_ilia/r1/ilia_5_s12705_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 131):
  - 지시문: Change only the color of the young woman's hair ribbon to a light powder blue in every view. Keep everything else exactly the same: her face, brown ponytail, clothes, pose, colors, background and hand-drawn animation style.
  - 파일: `07_ilia/edit/ilia_5_from-r1-s12705_e131_00001_.png`

## 8. 일로케

### 8-1. 턴어라운드  (1536×1024, 기본 seed 12801)

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt. Signature design point: a big broad rectangular body shape, neat short hair, brown leather accents, and gloved hands that always offer something first. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/08_iloke/iloke_1_turnaround_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13801, 1536×1024  
  - 파일: `08_iloke/r1/iloke_1_s13801_00001_.png`

### 8-2. 대표 포즈  (1024×1536, 기본 seed 12802)

```
Full-body character key art of a single character, silently holding out a folded handkerchief with one gloved hand, the other hand holding a closed umbrella, a tiny warm smile only in his eyes. Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt. Signature design point: a big broad rectangular body shape, neat short hair, brown leather accents, and gloved hands that always offer something first. Soft simple background: a soft deep-forest-green and cream wash. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/08_iloke/iloke_2_handkerchief_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12802, 1024×1536  
  - 파일: `08_iloke/r1/iloke_2_s12802_00001_.png`

### 8-3. 표정 시트  (1536×1024, 기본 seed 12803)

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: calm stoic face; a tiny smile only in his eyes; quiet concern with slightly knitted brows; slight embarrassment looking away with a faint blush; firm protective look; relaxed and sleepy with half-closed eyes. Same hairstyle, outfit and accessories in every portrait. Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt. Signature design point: a big broad rectangular body shape, neat short hair, brown leather accents, and gloved hands that always offer something first. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/08_iloke/iloke_3_expressions_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13803, 1536×1024  
  - 파일: `08_iloke/r1/iloke_3_s13803_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 141):
  - 지시문: Give the six portraits clearly different expressions while keeping them quiet and subtle. Top-left: calm stoic face. Top-middle: a tiny smile only in his eyes, with gently curved eyes. Top-right: quiet concern with slightly knitted brows. Bottom-left: slight embarrassment, looking away to the side with a faint blush. Bottom-middle: a firm protective look with a set jaw and steady eyes. Bottom-right: relaxed and sleepy with half-closed eyes. Keep his hair, clothes, gloves, layout, colors, background and hand-drawn animation style exactly the same.
  - 파일: `08_iloke/edit/iloke_3_from-r1-s13803_e141_00001_.png`

### 8-4. 장면  (1536×1024, 기본 seed 12804)

```
Animation film key frame, rainy day on a garden path, the tall quiet young man on the left tilts his umbrella over a small shy 12-year-old girl with a jet-black bob in a wine-red cape coat, the floppy ends of her extremely long cream sleeves dangling over her hands so that her hands stay hidden, who walks on the right, his gloved hand lightly holding her arm over her sleeve, his own shoulder getting wet, soft gray rain and green leaves, quiet kindness. Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt. Signature design point: a big broad rectangular body shape, neat short hair, brown leather accents, and gloved hands that always offer something first. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/08_iloke/iloke_4_umbrella_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13804, 1536×1024  
  - 파일: `08_iloke/r1/iloke_4_s13804_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 141):
  - 지시문: Make the small girl's cream sleeves longer so they completely cover her hands, so that no fingers are visible, and the young man's gloved hand holds her arm over her sleeve. Keep everything else exactly the same: both faces, the umbrella, the rain, colors and hand-drawn animation style.
  - 파일: `08_iloke/edit/iloke_4_from-r1-s13804_e141_00001_.png`

### 8-5. 장면  (1024×1536, 기본 seed 12805)

```
Animation film key frame, the tall young man walking one step ahead on a muddy garden path carrying two heavy clay flower pots, clearing the way, leather gloves, calm steady stride, morning mist. Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt. Signature design point: a big broad rectangular body shape, neat short hair, brown leather accents, and gloved hands that always offer something first. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/08_iloke/iloke_5_pots_00001_.png`
- 1단계 생성: 위 프롬프트, seed 13805, 1024×1536  
  - 파일: `08_iloke/r1/iloke_5_s13805_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 141):
  - 지시문: Remove the two extra clay pots behind his shoulders, so that he carries only the two clay pots in his gloved hands. Fill the removed area with the same garden background. Keep everything else exactly the same: his face, pose, clothes, colors and hand-drawn animation style.
  - 파일: `08_iloke/edit/iloke_5_from-r1-s13805_e141_00001_.png`

## 9. 일루키

### 9-1. 턴어라운드  (1536×1024, 기본 seed 12901)

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Signature design point: a thin body with big gestures, a sharp pointed chin, curly chestnut hair, freckles only on the nose and upper cheeks, and the mustard-yellow sweater that catches the eye first. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/09_iluki/iluki_1_turnaround_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12901, 1536×1024  
  - 파일: `09_iluki/r1/iluki_1_s12901_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 151):
  - 지시문: Push the young man's mustard-yellow sweater sleeves up to his elbows in all three views, showing his forearms, and add small freckles across his nose and upper cheeks. Keep everything else exactly the same: his curly chestnut hair, face, clothes, pose, the toy frog, colors, background and hand-drawn animation style.
  - 파일: `09_iluki/edit/iluki_1_from-r1-s12901_e151_00001_.png`
- 3단계 편집 (Qwen-Image-Edit-2511, seed 484):
  - 지시문: Roll the young man's mustard-yellow sweater sleeves up above his elbows in all three views, so that his bare forearms are clearly visible. Keep everything else exactly the same: his freckles, curly chestnut hair, face, clothes, pose, the toy frog, colors, background and hand-drawn animation style.
  - 파일: `09_iluki/edit2/iluki_1_from-edit-e151_e484_00001_.png`

### 9-2. 대표 포즈  (1024×1536, 기본 seed 12902)

```
Full-body character key art of a single character, in a dynamic exaggerated pose, leaning forward and winking while holding up a little toy frog toward the viewer to make someone laugh. Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Signature design point: a thin body with big gestures, a sharp pointed chin, curly chestnut hair, freckles only on the nose and upper cheeks, and the mustard-yellow sweater that catches the eye first. Soft simple background: a soft mustard-yellow and cream wash. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/09_iluki/iluki_2_keypose_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12902, 1024×1536  
  - 파일: `09_iluki/r1/iluki_2_s12902_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 151):
  - 지시문: Push his mustard-yellow sweater sleeves up to his elbows, showing his forearms, and add small freckles across his nose and upper cheeks. Keep everything else exactly the same: his wink, pose, the toy frog, clothes, colors, background and hand-drawn animation style.
  - 파일: `09_iluki/edit/iluki_2_from-r1-s12902_e151_00001_.png`
- 3단계 편집 (Qwen-Image-Edit-2511, seed 373):
  - 지시문: Roll his mustard-yellow sweater sleeves up above his elbows on both arms, so that his bare forearms are clearly visible. Keep the single figure and everything else exactly the same: his freckles, wink, pose, the toy frog, clothes, colors, background and hand-drawn animation style.
  - 파일: `09_iluki/edit2/iluki_2_from-edit-e151_e373_00001_.png`

### 9-3. 표정 시트  (1536×1024, 기본 seed 12903)

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: huge mischievous grin showing his teeth; exaggerated shocked face with bulging eyes and a dropped jaw; pouting with puffed cheeks after being scolded; sneaky plotting look with narrowed eyes; laughing so hard that tears gather at the corners of his eyes; a rare sincere gentle smile. Same hairstyle, outfit and accessories in every portrait. Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Signature design point: a thin body with big gestures, a sharp pointed chin, curly chestnut hair, freckles only on the nose and upper cheeks, and the mustard-yellow sweater that catches the eye first. Plain warm off-white paper background, clean design sheet layout without any lettering or captions. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/09_iluki/iluki_3_expressions_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12903, 1536×1024  
  - 파일: `09_iluki/r1/iluki_3_s12903_00001_.png`

### 9-4. 장면  (1536×1024, 기본 seed 12904)

```
Animation film key frame, in a greenhouse, the playful young man crouches on the left and shows a toy insect and a toy frog from his stuffed pockets to a small shy 12-year-old girl with a jet-black bob in a wine-red cape coat, the floppy ends of her extremely long cream sleeves dangling over her hands so that her hands stay hidden, who stands on the right and giggles behind her sleeve ends, cheerful warm light. Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Signature design point: a thin body with big gestures, a sharp pointed chin, curly chestnut hair, freckles only on the nose and upper cheeks, and the mustard-yellow sweater that catches the eye first. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/09_iluki/iluki_4_toys_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12904, 1536×1024  
  - 파일: `09_iluki/r1/iluki_4_s12904_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 151):
  - 지시문: Make the small girl's long cream sleeves cover her hands completely, so she giggles behind the soft sleeve ends with no fingers visible, and make her cape coat a deep wine red. Keep everything else exactly the same: both faces, the young man and his toys, the greenhouse, colors and hand-drawn animation style.
  - 파일: `09_iluki/edit/iluki_4_from-r1-s12904_e151_00001_.png`

### 9-5. 장면  (1536×1024, 기본 seed 12905)

```
Animation film key frame, comedic moment in a greenhouse: on the left, a slim young woman in her mid-twenties with a neat brown ponytail tied with a powder-blue ribbon, wearing a sage-green work jacket and an apron, stands with one hand on her hip, scolding and confiscating a toy frog and toy insects; on the right, the playful young man pouts with puffed cheeks and his empty pockets turned out, warm light. Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Signature design point: a thin body with big gestures, a sharp pointed chin, curly chestnut hair, freckles only on the nose and upper cheeks, and the mustard-yellow sweater that catches the eye first. Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.
```

- 최종 파일: `final/09_iluki/iluki_5_scolded_00001_.png`
- 1단계 생성: 위 프롬프트, seed 12905, 1536×1024  
  - 파일: `09_iluki/r1/iluki_5_s12905_00001_.png`
- 2단계 편집 (Qwen-Image-Edit-2511, seed 151):
  - 지시문: Make the young woman's hair brown instead of black, tied in a neat ponytail with a light powder-blue ribbon. Keep everything else exactly the same: her face, apron, the toy frog in her hand, the young man, the greenhouse, colors and hand-drawn animation style.
  - 파일: `09_iluki/edit/iluki_5_from-r1-s12905_e151_00001_.png`
