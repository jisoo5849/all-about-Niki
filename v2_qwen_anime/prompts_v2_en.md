# 니키와 이상한 나침반 · 컨셉아트 2차 프롬프트 (영문, 실제 입력)

- 생성 모델은 Qwen-Image-2512(30 steps, cfg 4, euler)이고, 편집은 Qwen-Image-Edit-2511(Lightning 4 steps)이다.
- 각 컷의 '확장 입력'을 허브의 프롬프트 확장 기능에 넣었고, 돌아온 '확장 프롬프트'로 그렸다.
- 실제 생성 프롬프트는 `그림체 머리말 + 확장 프롬프트 + 그림체 고정 문장` 순서다 (머리말·고정 문장은 아래 공통 문장).
- 모든 값은 최종 PNG 안의 실행 정보에서 꺼냈다 (`extract_v2.py`).

## 공통 문장

### 그림체 머리말 (r3 부터 앞에 붙임)

> Anime screencap, a single frame from a Japanese TV anime series, cel animation with flat simple colors and minimal soft shading, thin clean black outlines, anime-style faces with large eyes, a small simple nose and smooth simplified skin.

### 그림체 고정 문장 (확장 기능이 끝에 그대로 붙임)

> Modern Japanese theatrical anime film style of the late 2010s: crisp clean line art with thin even dark lines, polished digital cel shading with two crisp shadow tones and a bright rim light along the edges, large expressive eyes with layered sparkling highlights, glossy light-catching hair strands, luminous highly detailed painted backgrounds with dramatic sky light, glowing light particles and soft lens bloom, vivid saturated colors with cool blue-violet shadows, cinematic depth of field, original character design.

### 공통 부정 프롬프트

> photorealistic, 3d render, cgi, watercolor, gouache, rough sketch, pencil texture, muted faded colors, text, letters, watermark, logo, signature, blurry, deformed hands, extra fingers, extra arms, extra legs, extra limbs, missing neck, floating head, duplicate face, merged bodies, cropped feet

## 01_niki

### niki_1 · `final/01_niki/niki_1_turnaround.png`

- 생성: 시드 12101, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/01_niki/r3/niki_1_s12101_00001_.png`

**확장 입력 (요청)**

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, standing with her arms hanging straight down at her sides, the floppy cuffs of her extremely long cream sleeves sticking out from under the cape and dangling a hand's length below her wrists, closed and empty-looking, so that no hands come out of the sleeves in any view, identical outfit and proportions in all three views, evenly spaced. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Niki, a shy 12-year-old girl whose hands are always hidden inside her overly long sleeves, very small and thin for her age (much shorter than the adults), chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing a wine-red cape coat over a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights and faded brown boots. Signature design point: the cream shirt sleeves are far longer than her arms, the soft sleeve cuffs droop past her fingertips and completely cover both hands, so no fingers are visible
```

**확장 프롬프트**

```
Character model sheet featuring Niki, a shy 12-year-old girl, drawn three times side by side in front, side, and back views, full body from head to toe, standing with arms hanging straight down at her sides, identical outfit and proportions in all three views, evenly spaced, plain light gray studio background with a soft white glow, clean design sheet layout, Niki has chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing a wine-red cape coat over a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights and faded brown boots, the cream shirt sleeves are far longer than her arms, the soft sleeve cuffs droop past the wrists and completely cover the extremities, oversized sleeves hanging well past the wrists, the cuffs closed and drooping, clean plain background.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, visible hands, fingers, bare hands, hands outside the sleeves`

**편집 지시 (시드 101)**

```
Make the girl's cream shirt sleeves longer in all three views so that the soft sleeve cuffs hang down past her hands and completely cover both hands like closed sleeve ends; no hands or fingers are visible anywhere. Keep everything else exactly the same: the same girl, pose, wine-red cape, colors, background and anime style.
```

### niki_2 · `final/01_niki/niki_2_keypose.png`

- 생성: 시드 12102, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/01_niki/r3/niki_2_s12102_00001_.png`

**확장 입력 (요청)**

```
Full-body character key art of a single character, standing shyly with her shoulders curled inward and her gaze dropped to the tips of her boots, both floppy sleeve ends pressed together in front of her mouth and chin so that her hands stay completely hidden inside the extremely long cream sleeves, an old brass compass peeking out of the inner pocket of her open cape coat. the character described in the must-keep details. Soft simple background: a pale cream wash with a faint wine-red vignette.
```

**확장 입력 (꼭 지킬 특징)**

```
Niki, a shy 12-year-old girl whose hands are always hidden inside her overly long sleeves, very small and thin for her age (much shorter than the adults), chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing a wine-red cape coat over a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights and faded brown boots. Signature design point: the cream shirt sleeves are far longer than her arms, the soft sleeve cuffs droop past her fingertips and completely cover both hands, so no fingers are visible
```

**확장 프롬프트**

```
Full-body character key art of Niki, a shy 12-year-old girl, standing with shoulders curled inward and gaze dropped to the tips of her boots. Both floppy sleeve ends pressed together in front of her mouth and chin, the cream shirt sleeves are far longer than her arms, soft sleeve cuffs droop past her fingertips, no fingers are visible, hands stay completely hidden. An old brass compass peeks out of the inner pocket of her open wine-red cape coat. She wears a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights, and faded brown boots. Her chin-length straight jet-black bob has short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth. Soft simple background with a pale cream wash and a faint wine-red vignette. Soft diffused lighting, eye-level camera shot, clean plain backdrop, smooth fabric textures, matte brass, glossy hair strands.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, visible hands, fingers, bare hands, hands outside the sleeves`

**편집 지시 (시드 101)**

```
Make her cream sleeves longer so the soft sleeve ends completely cover both of her hands where she presses them to her mouth; no fingers are visible. Keep everything else exactly the same: face, hair, wine-red cape coat, the compass, colors, background and anime style.
```

### niki_3 · `final/01_niki/niki_3_expressions.png`

- 생성: 시드 13103, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/01_niki/r4/niki_3_s13103_00001_.png`

**확장 입력 (요청)**

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: shy with eyes downcast behind her bangs and the long sleeve cuffs raised to cover her mouth; nervous with a small wobbly smile and eyebrows tilted up; observant with calm sharp eyes glancing sideways; teasing with a tiny lopsided smirk and one eye half closed; scared but determined with wide eyes, knitted eyebrows and lips pressed tight; crying with relief, tears streaming down while she wipes her eyes with a sleeve cuff. Same hairstyle and outfit in every portrait. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Niki, a shy 12-year-old girl whose hands are always hidden inside her overly long sleeves, very small and thin for her age (much shorter than the adults), chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing a wine-red cape coat over a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights and faded brown boots. Signature design point: the cream shirt sleeves are far longer than her arms, the soft sleeve cuffs droop past her fingertips and completely cover both hands, so no fingers are visible
```

**확장 프롬프트**

```
Expression sheet, six head-and-shoulders portraits of Niki arranged in a neat grid of two rows and three columns, same character in every panel, chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing a wine-red cape coat over a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights, faded brown boots, oversized cream shirt sleeves hanging well past the wrists, the cuffs closed and drooping, covering the lower arms completely, shy with eyes downcast behind her bangs and the long sleeve cuffs raised to cover her mouth, nervous with a small wobbly smile and eyebrows tilted up, observant with calm sharp eyes glancing sideways, teasing with a tiny lopsided smirk and one eye half closed, scared but determined with wide eyes, knitted eyebrows and lips pressed tight, crying with relief, tears streaming down while she wipes her eyes with a sleeve cuff, plain light gray studio background with a soft white glow, clean design sheet layout with a clean plain background, soft diffused studio lighting, frontal medium close-up shot, flat even focus, smooth matte skin texture, soft wool fabric texture on shorts, glossy hair strands.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, visible hands, fingers, bare hands, hands outside the sleeves`

### niki_4 · `final/01_niki/niki_4_forest_magic.png`

- 생성: 시드 12104, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/01_niki/r3/niki_4_s12104_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, a small girl kneeling in a misty deep-green forest at dusk in front of a wilted sprout, gently cupping the sprout between the two floppy ends of her extremely long cream sleeves without taking her hands out, soft particles of sprout green, aqua and silver light glowing through the sleeve fabric and drifting onto the plant, quiet emotional moment, the wine-red coat contrasting with the green forest, painted forest background. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Niki, a shy 12-year-old girl whose hands are always hidden inside her overly long sleeves, very small and thin for her age (much shorter than the adults), chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing a wine-red cape coat over a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights and faded brown boots. Signature design point: the cream shirt sleeves are far longer than her arms, the soft sleeve cuffs droop past her fingertips and completely cover both hands, so no fingers are visible
```

**확장 프롬프트**

```
Niki, a shy 12-year-old girl, kneeling in a misty deep-green forest at dusk, wearing a wine-red cape coat over a cream round-collar shirt, dark mocha brown wool shorts, charcoal gray tights, and faded brown boots, with chin-length straight jet-black bob and short side-swept bangs half covering her very dark eyes with a faint sky-blue glint, pale creamy skin, and a small mouth, gently cupping the sprout between the two floppy ends of her extremely long cream sleeves, the soft sleeve cuffs drooping past the wrists and completely covering the hands so no fingers are visible, soft particles of sprout green, aqua, and silver light glowing through the sleeve fabric and drifting onto the plant, quiet emotional moment, the wine-red coat contrasting with the green forest, painted forest background, low-angle medium shot, soft diffused dusk lighting, misty atmosphere, textured wool and fabric details, clean line art, polished digital cel shading, luminous painted background.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, visible hands, fingers, bare hands, hands outside the sleeves`

**편집 지시 (시드 101)**

```
Make her long cream sleeves cover both of her hands completely, so she cups the space above the sprout with the soft closed sleeve ends instead of bare hands, and faint sprout-green, aqua and silver light seeps out from the sleeve ends. No fingers are visible. Keep everything else exactly the same: the girl, her pose, the forest, colors and anime style.
```

### niki_5 · `final/01_niki/niki_5_sleeve_growth.png`

- 생성: 시드 12155, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/01_niki/r3/niki_5_s12155_00001_.png`

**확장 입력 (요청)**

```
Character growth sheet: three waist-up portraits of the same girl side by side, telling her growth through the length of her sleeves: on the left, timid with her head down, the extremely long cream sleeves dangling well past her hands so that no hands are visible at all; in the middle, her gaze lifted a little, holding the sleeve ends together in front of her chest with only the very tips of her fingers peeking out; on the right, head raised with a brave small smile and her bangs tucked behind one ear, sleeves rolled up to her elbows, bare hands holding a small envelope. Plain light gray studio background with a soft white glow, without any lettering. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Niki, a shy 12-year-old girl, very small and thin for her age, chin-length straight jet-black bob with short side-swept bangs half covering her eyes, very dark eyes with a faint sky-blue glint, pale creamy skin, small mouth, wearing her indoor clothes without any coat: a loose cream cotton shirt with a small rounded flat collar and extremely long sleeves, dark mocha brown wool shorts, charcoal gray tights and faded brown boots, the same outfit in every drawing
```

**확장 프롬프트**

```
Three waist-up portraits of Niki, a shy 12-year-old girl, arranged side by side on a plain light gray studio background with a soft white glow. Niki is very small and thin, with chin-length straight jet-black bob hair, short side-swept bangs, very dark eyes with a faint sky-blue glint, pale creamy skin, and a small mouth. She wears a loose cream cotton shirt with a small rounded flat collar, dark mocha brown wool shorts, charcoal gray tights, and faded brown boots. On the left, Niki has her head down, timid, with extremely long sleeves dangling well past the wrists, the cuffs closed and drooping so the hands are hidden. In the middle, Niki has her gaze lifted slightly, holding the sleeve ends together in front of her chest, with only the very tips of her fingers peeking out from the cuffs. On the right, Niki has her head raised with a brave small smile, her bangs tucked behind one ear, and sleeves rolled up to her elbows, bare hands holding a small envelope. The lighting is soft and even, highlighting the textures of the cotton shirt and wool shorts.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

**편집 지시 (시드 101)**

```
Edit only the sleeves. Left girl: make her sleeves much longer so they hang past her hands and completely hide both hands. Middle girl: make her sleeves longer so they cover her hands, leaving only the tips of her fingers peeking out. Right girl: keep her sleeves rolled up and her bare hands holding the envelope. Keep everything else exactly the same: faces, hair, clothes, colors, background and anime style.
```

## 02_putor

### putor_1 · `final/02_putor/putor_1_turnaround.png`

- 생성: 시드 12201, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/02_putor/r3/putor_1_s12201_00001_.png`

**확장 입력 (요청)**

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Putor, an elderly dwarf healer in his sixties, very short (about the height of a child) with a plump round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out of it, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses (lenses shaped like half circles with flat tops) perched on the tip of his nose, no hat, a plain dusty antique-brass travel coat with a few small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with many small compartments of clinking glass vials, carried on a shoulder strap in front of his belly, an empty small leather flint case with a little paper tag at his belt. Signature design point: a round figure half hidden behind the huge medicine bag, pointed ear tips, half-moon glasses that he wears in every drawing, and a long white beard tipped with green herb powder that bristles when he is scared and droops when he is relieved
```

**확장 프롬프트**

```
Character model sheet, three identical figures of Putor an elderly dwarf healer arranged side by side, front view, side view, and back view, full body from head to toe, relaxed neutral standing pose, evenly spaced, plain light gray studio background with a soft white glow, clean design sheet layout, Putor is very short about the height of a child with a plump round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses perched on the tip of his nose, a plain dusty antique-brass travel coat with small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with many small compartments of clinking glass vials carried on a shoulder strap in front of his belly, an empty small leather flint case with a little paper tag at his belt, crisp clean line art, polished digital cel shading, large expressive eyes, glossy light-catching hair strands, vivid saturated colors, cool blue-violet shadows.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### putor_2 · `final/02_putor/putor_2_keypose.png`

- 생성: 시드 12202, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/02_putor/r3/putor_2_s12202_00001_.png`

**확장 입력 (요청)**

```
Full-body character key art of a single character, hurrying forward with short anxious steps, hugging the small empty leather flint case to his chest with both hands, the huge medicine bag bouncing on its strap and covering half of his round body, glass vials jingling, his white beard bristling with nervousness. the character described in the must-keep details. Soft simple background: a dusty antique-brass and parchment wash.
```

**확장 입력 (꼭 지킬 특징)**

```
Putor, an elderly dwarf healer in his sixties, very short (about the height of a child) with a plump round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out of it, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses (lenses shaped like half circles with flat tops) perched on the tip of his nose, no hat, a plain dusty antique-brass travel coat with a few small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with many small compartments of clinking glass vials, carried on a shoulder strap in front of his belly, an empty small leather flint case with a little paper tag at his belt. Signature design point: a round figure half hidden behind the huge medicine bag, pointed ear tips, half-moon glasses that he wears in every drawing, and a long white beard tipped with green herb powder that bristles when he is scared and droops when he is relieved
```

**확장 프롬프트**

```
Full-body character key art of Putor, an elderly dwarf healer in his sixties, very short with a plump round body and round sloping shoulders, hurrying forward with short anxious steps, hugging the small empty leather flint case to his chest with both hands, a huge boxy brown leather medicine bag bouncing on its strap and covering half of his round body, glass vials jingling inside many small compartments, his long fluffy white beard bristling with nervousness, dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses perched on the tip of his nose, a plain dusty antique-brass travel coat with pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a little paper tag at his belt, soft simple background of a dusty antique-brass and parchment wash, dramatic sky light, glowing light particles, soft lens bloom, cinematic depth of field, crisp clean line art, polished digital cel shading, bright rim light, large expressive eyes, glossy hair strands, vivid saturated colors, cool blue-violet shadows.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### putor_3 · `final/02_putor/putor_3_expressions.png`

- 생성: 시드 12203, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/02_putor/r3/putor_3_s12203_00001_.png`

**확장 입력 (요청)**

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: worried with a deep frown and his beard drooping; fussy scolding with a raised stubby finger and puffed cheeks; frightened with wide eyes and his white beard bristling straight out like a brush; relieved with a soft smile and the beard hanging limp and curved; muttering herb names like a spell with his eyes squeezed shut; peering kindly over his half-moon glasses with his head tilted. Same hairstyle, outfit and accessories in every portrait. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Putor, an elderly dwarf healer in his sixties, very short (about the height of a child) with a plump round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out of it, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses (lenses shaped like half circles with flat tops) perched on the tip of his nose, no hat, a plain dusty antique-brass travel coat with a few small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with many small compartments of clinking glass vials, carried on a shoulder strap in front of his belly, an empty small leather flint case with a little paper tag at his belt. Signature design point: a round figure half hidden behind the huge medicine bag, pointed ear tips, half-moon glasses that he wears in every drawing, and a long white beard tipped with green herb powder that bristles when he is scared and droops when he is relieved
```

**확장 프롬프트**

```
Expression sheet, six head-and-shoulders portraits of Putor, an elderly dwarf healer, arranged in a neat grid of two rows and three columns, plain light gray studio background with a soft white glow, clean design sheet layout, crisp clean line art, Putor has a plump round body, round sloping shoulders, fluffy white hair with pointed ear tips, long fluffy white beard dusted with pale green herb powder, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses, dusty antique-brass travel coat, ink-black vest, parchment-colored shirt, small antique-brass healer badge, huge boxy brown leather medicine bag, empty small leather flint case, worried expression with deep frown and drooping beard, fussy scolding with raised stubby finger and puffed cheeks, frightened with wide eyes and bristling white beard, relieved with soft smile and limp curved beard, muttering with eyes squeezed shut, peering kindly with head tilted, same hairstyle and outfit in every portrait, soft white glow, clean design sheet layout.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### putor_4 · `final/02_putor/putor_4_healing.png`

- 생성: 시드 12204, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/02_putor/r3/putor_4_s12204_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, two people on a forest path: on the right, a tall young woman traveler with a long red braid and a blue dress lies on the ground with her leg wrapped in a white bandage; on the left, the small round dwarf healer kneels beside her and sprinkles green herb powder from a glass vial onto the bandage with trembling but steady hands, his medicine bag open beside him, brave despite his fear, cool blue-gray forest with warm light on the two of them. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Putor, an elderly dwarf healer in his sixties, very short (about the height of a child) with a plump round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out of it, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses (lenses shaped like half circles with flat tops) perched on the tip of his nose, no hat, a plain dusty antique-brass travel coat with a few small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with many small compartments of clinking glass vials, carried on a shoulder strap in front of his belly, an empty small leather flint case with a little paper tag at his belt. Signature design point: a round figure half hidden behind the huge medicine bag, pointed ear tips, half-moon glasses that he wears in every drawing, and a long white beard tipped with green herb powder that bristles when he is scared and droops when he is relieved
```

**확장 프롬프트**

```
Two figures on a forest path in a cool blue-gray forest with warm light illuminating the center. On the right, a tall young woman traveler with a long red braid and a blue dress lies on the ground, her leg wrapped in a white bandage. On the left, Putor, an elderly dwarf healer in his sixties, kneels beside her. He is very short with a plump round body, round sloping shoulders, and a full head of fluffy white hair with pointed ear tips peeking out. He has a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, a round rosy nose, and short thick fingers. Small half-moon reading glasses perch on the tip of his nose. He wears a plain dusty antique-brass travel coat with small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, and a small antique-brass healer badge on his chest. A huge boxy brown leather medicine bag with many small compartments of clinking glass vials rests on his belly, open beside him. He sprinkles green herb powder from a glass vial onto the bandage with trembling but steady hands. His expression is brave despite his fear.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### putor_5 · `final/02_putor/putor_5_props.png`

- 생성: 시드 12205, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/02_putor/r3/putor_5_s12205_00001_.png`

**확장 입력 (요청)**

```
Prop design sheet for a dwarf healer laid out neatly: a huge boxy worn leather medicine bag opened to show rows of small compartments with glass vials and herb pouches, a small empty leather flint case with a tiny blank paper tag, spare half-moon reading glasses, an antique-brass healer badge, a scrap of coarse filter cloth, small bundles of dried herbs, with the healer himself standing right next to the bag for scale, the bag almost as big as he is. Plain light gray studio background with a soft white glow, without any lettering. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Putor, an elderly dwarf healer in his sixties, very short (about the height of a child) with a plump round body and round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out of it, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, round rosy nose, short thick fingers, small half-moon reading glasses (lenses shaped like half circles with flat tops) perched on the tip of his nose, no hat, a plain dusty antique-brass travel coat with a few small pale green herb-powder stains, an ink-black vest, a parchment-colored shirt, a small antique-brass healer badge on his chest, a huge boxy brown leather medicine bag with many small compartments of clinking glass vials, carried on a shoulder strap in front of his belly, an empty small leather flint case with a little paper tag at his belt. Signature design point: a round figure half hidden behind the huge medicine bag, pointed ear tips, half-moon glasses that he wears in every drawing, and a long white beard tipped with green herb powder that bristles when he is scared and droops when he is relieved
```

**확장 프롬프트**

```
Prop design sheet layout featuring Putor, an elderly dwarf healer in his sixties, standing right next to a huge boxy brown leather medicine bag that is almost as big as he is, the bag opened to show rows of small compartments with glass vials and herb pouches. Putor has a plump round body, round sloping shoulders, a full head of fluffy white hair with pointed ear tips peeking out, a long fluffy white beard dusted with pale green herb powder at the tips, bushy white eyebrows, and a round rosy nose. He wears small half-moon reading glasses perched on the tip of his nose, a plain dusty antique-brass travel coat with pale green herb-powder stains, an ink-black vest, and a parchment-colored shirt. A small antique-brass healer badge is on his chest. An empty small leather flint case with a tiny blank paper tag hangs at his belt. Spare half-moon reading glasses, a scrap of coarse filter cloth, and small bundles of dried herbs are arranged neatly around the bag. The background is a plain light gray studio background with a soft white glow, clean and uncluttered.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

## 03_quillins

### quillins_1 · `final/03_quillins/quillins_1_hooded_turnaround.png`

- 생성: 시드 12301, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/03_quillins/r3/quillins_1_s12301_00001_.png`

**확장 입력 (요청)**

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Quillins, a tall thin man with angular shoulders, wrapped in a worn ink-black hooded cloak, the deep hood hides his whole face in complete shadow with no visible features, black leather gloves, faded fur trim and bone toggles on the cloak, the hem dragging on the ground, a glimpse of an old dark indigo coat underneath. Signature design point: a faceless ink-black figure, the inside of the hood is pure black shadow like spreading ink with no eyes, nose or mouth, only the black-gloved hands stand out
```

**확장 프롬프트**

```
Character model sheet featuring one tall thin man named Quilins drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced, plain light gray studio background with a soft white glow, clean design sheet layout, Quilins has angular shoulders, wrapped in a worn ink-black hooded cloak, the deep hood hides his whole face in complete shadow, the inside of the hood is pure black shadow like spreading ink, black leather gloves, faded fur trim and bone toggles on the cloak, the hem dragging on the ground, a glimpse of an old dark indigo coat underneath, faceless ink-black figure, only the black-gloved hands stand out.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### quillins_2 · `final/03_quillins/quillins_2_night_shore.png`

- 생성: 시드 12302, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/03_quillins/r3/quillins_2_s12302_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, a faceless dark figure standing on a rocky shore at night, the black hooded cloak drawn like spreading ink-wash smudges, a low camera angle, cold blue-gray moonlight, the cloak edge dragging over wet stones, mysterious and frightening without gore. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Quillins, a tall thin man with angular shoulders, wrapped in a worn ink-black hooded cloak, the deep hood hides his whole face in complete shadow with no visible features, black leather gloves, faded fur trim and bone toggles on the cloak, the hem dragging on the ground, a glimpse of an old dark indigo coat underneath. Signature design point: a faceless ink-black figure, the inside of the hood is pure black shadow like spreading ink with no eyes, nose or mouth, only the black-gloved hands stand out
```

**확장 프롬프트**

```
A tall thin man with angular shoulders stands on a rocky shore at night, wrapped in a worn ink-black hooded cloak drawn like spreading ink-wash smudges. The deep hood hides his whole face in complete shadow, the inside of the hood is pure black shadow like spreading ink, only the black-gloved hands stand out. Faded fur trim and bone toggles decorate the cloak, while the hem dragging on the ground rests over wet stones. A glimpse of an old dark indigo coat is visible underneath. The scene is lit by cold blue-gray moonlight, creating a mysterious and frightening atmosphere. The camera uses a low camera angle to emphasize the figure's height against the dark environment. The texture of the wet rocks and the smooth, flowing nature of the ink-wash cloak are highlighted by the lighting.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### quillins_3 · `final/03_quillins/quillins_3_reveal_portrait.png`

- 생성: 시드 12353, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/03_quillins/r3/quillins_3_s12353_00001_.png`

**확장 입력 (요청)**

```
Bust portrait of the unhooded man looking down with tired sorrowful eyes, the hood resting on his shoulders, dim blue-gray light with a faint warm glint from the coral-pink chieftain's seal. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Quillins, an old man in his late fifties, clearly aged, tall and thin with angular shoulders, his hood pushed back off his head and hanging behind his neck, a long gaunt deeply lined face with sunken cheeks and hollow tired eyes, black hair heavily streaked with white, dark gray eyes with a black tint, patches of bluish-black decayed skin on his neck and jaw, cracked like dry mud with small white salt crystals in the cracks, an old dark indigo long chieftain coat with a small round coral-pink chieftain's seal pinned at the chest, a worn ink-black cloak on his shoulders, black leather gloves. Signature design point: an aged gaunt face, small white salt crystals in the cracks of the bluish-black decayed skin, and black leather gloves that hide his sick hands
```

**확장 프롬프트**

```
Bust portrait of Quilins, an old man in his late fifties, tall and thin with angular shoulders, looking down with tired sorrowful eyes, his hood pushed back off his head and hanging behind his neck, a long gaunt deeply lined face with sunken cheeks and hollow tired eyes, black hair heavily streaked with white, dark gray eyes with a black tint, patches of bluish-black decayed skin on his neck and jaw, cracked like dry mud with small white salt crystals in the cracks, an old dark indigo long chieftain coat with a small round coral-pink chieftain's seal pinned at the chest, a worn ink-black cloak on his shoulders, black leather gloves, dim blue-gray light with a faint warm glint from the coral-pink chieftain's seal, close-up shot from a slightly low angle, shallow depth of field, textured fabric and cracked skin details, cinematic composition.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

**편집 지시 (시드 101)**

```
Push his hood back off his head so the hood rests on his shoulders behind his neck, revealing his black hair heavily streaked with white. Keep everything else exactly the same: his tired gaunt face, expression, the coral-pink seal, the black gloves, the cloak, background, colors and anime style.
```

### quillins_4 · `final/03_quillins/quillins_4_seal.png`

- 생성: 시드 12354, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/03_quillins/r3/quillins_4_s12354_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, the gaunt man kneeling on wet sand at the edge of the sea at sunrise, gently whispering to a young gray seal pup with a bandaged flipper lying in front of him, his only warm moment, softer colors and warm light on his face. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Quillins, an old man in his late fifties, clearly aged, tall and thin with angular shoulders, his hood pushed back off his head and hanging behind his neck, a long gaunt deeply lined face with sunken cheeks and hollow tired eyes, black hair heavily streaked with white, dark gray eyes with a black tint, patches of bluish-black decayed skin on his neck and jaw, cracked like dry mud with small white salt crystals in the cracks, an old dark indigo long chieftain coat with a small round coral-pink chieftain's seal pinned at the chest, a worn ink-black cloak on his shoulders, black leather gloves. Signature design point: an aged gaunt face, small white salt crystals in the cracks of the bluish-black decayed skin, and black leather gloves that hide his sick hands
```

**확장 프롬프트**

```
Quillins, an old man in his late fifties, clearly aged, tall and thin with angular shoulders, kneeling on wet sand at the edge of the sea at sunrise, gently whispering to a young gray seal pup with a bandaged flipper lying in front of him, his hood pushed back off his head and hanging behind his neck, a long gaunt deeply lined face with sunken cheeks and hollow tired eyes, black hair heavily streaked with white, dark gray eyes with a black tint, patches of bluish-black decayed skin on his neck and jaw cracked like dry mud with small white salt crystals in the cracks, an old dark indigo long chieftain coat with a small round coral-pink chieftain's seal pinned at the chest, a worn ink-black cloak on his shoulders, black leather gloves, softer colors and warm light on his face, medium shot at eye level, serene beach with gentle waves and a soft sunrise sky, wet sand, smooth seal fur, rough cracked skin, fabric of the coat and cloak.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### quillins_5 · `final/03_quillins/quillins_5_glove.png`

- 생성: 시드 12355, 1328x1328, 원본 `main/2026-10-27/niki_compass_v2/03_quillins/r1/quillins_5_s12355_00001_.png`

**확장 입력 (요청)**

```
Extreme close-up of two hands only, filling the whole frame: a black-gloved right hand slowly pulls the black leather glove off the left hand, revealing bluish-black decayed skin cracked like dry mud with small white salt crystals in the cracks; only the hands and the dark indigo coat cuffs are visible, no face in the picture, quiet and sad mood, not gory. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Quillins, an old man in his late fifties, clearly aged, tall and thin with angular shoulders, his hood pushed back off his head and hanging behind his neck, a long gaunt deeply lined face with sunken cheeks and hollow tired eyes, black hair heavily streaked with white, dark gray eyes with a black tint, patches of bluish-black decayed skin on his neck and jaw, cracked like dry mud with small white salt crystals in the cracks, an old dark indigo long chieftain coat with a small round coral-pink chieftain's seal pinned at the chest, a worn ink-black cloak on his shoulders, black leather gloves. Signature design point: an aged gaunt face, small white salt crystals in the cracks of the bluish-black decayed skin, and black leather gloves that hide his sick hands
```

**확장 프롬프트**

```
Extreme close-up, center framing, two hands filling the entire frame, a black-gloved right hand slowly pulls the black leather glove off the left hand, revealing bluish-black decayed skin cracked like dry mud with small white salt crystals in the cracks, dark indigo coat cuffs visible at the wrists, quiet and sad mood, clean plain background, soft diffused lighting, shallow depth of field, glossy leather texture, dry cracked skin texture, matte fabric texture, cool blue-violet shadows, crisp clean line art, polished digital cel shading, bright rim light along the edges, luminous highly detailed painted background, glowing light particles, soft lens bloom, vivid saturated colors, cinematic depth of field, original character design.
```

- 이 컷은 그림체 머리말 없이 r1 로 그린 원본을 편집으로 애니풍으로 바꿨다.

**편집 지시 (시드 101)**

```
Redraw this exact picture as a Japanese anime cel illustration: flat simple colors with soft cel shading and thin clean outlines. Keep the same composition with only the two hands filling the frame, the black leather glove being pulled off, the bluish-black cracked skin with small white salt crystals, the dark indigo coat cuffs, the night background and colors.
```

## 04_james

### james_1 · `final/04_james/james_1_turnaround.png`

- 생성: 시드 12401, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/04_james/r3/james_1_s12401_00001_.png`

**확장 입력 (요청)**

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
James, a gentle father in his early forties, a youthful handsome adult face with smooth skin and only very faint smile lines at the corners of his eyes, kind warm eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly dark brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind smooth face in his early forties, and three stray strands of hair sticking out from his messy brown hair
```

**확장 프롬프트**

```
Character model sheet, three identical figures of James arranged side by side, front view on the left, side view in the center, back view on the right, evenly spaced, full body from head to toe, relaxed neutral standing pose, arms hanging naturally at the sides, legs straight and parallel, identical outfit and proportions in all three views, James is a gentle father in his early forties, youthful handsome adult face with smooth skin, very faint smile lines at the corners of his eyes, kind warm eyes, clean-shaven, very tall and lanky build with slightly stooped shoulders, messy unruly dark brown hair with three stray strands sticking out at the top like little cowlicks, slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, thin silver watch chain, plain light gray studio background with a soft white glow, clean design sheet layout, crisp clean line art, polished digital cel shading, bright rim light, vivid saturated colors, cool blue-violet shadows.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, elderly, old man, grandfather, deep wrinkles, weathered skin, sagging skin, gray hair, white hair`

### james_2 · `final/04_james/james_2_keypose.png`

- 생성: 시드 12402, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/04_james/r3/james_2_s12402_00001_.png`

**확장 입력 (요청)**

```
Full-body character key art of a single character, crouching down low on one knee and smiling warmly straight at the viewer at eye level, one hand resting on his knee, a metal watering can on the ground beside him. the character described in the must-keep details. Soft simple background: a soft slate-blue and cream wash.
```

**확장 입력 (꼭 지킬 특징)**

```
James, a gentle father in his early forties, a youthful handsome adult face with smooth skin and only very faint smile lines at the corners of his eyes, kind warm eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly dark brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind smooth face in his early forties, and three stray strands of hair sticking out from his messy brown hair
```

**확장 프롬프트**

```
Full-body character key art of James, a gentle father in his early forties, crouching down low on one knee and smiling warmly straight at the viewer at eye level, one hand resting on his knee, a metal watering can on the ground beside him, youthful handsome adult face with smooth skin and only very faint smile lines at the corners of his eyes, kind warm eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly dark brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain, very tall thin straight build with long limbs, a kind smooth face in his early forties, and three stray strands of hair sticking out from his messy brown hair, soft simple background: a soft slate-blue and cream wash, soft diffused lighting, low angle camera shot, wide framing, smooth painted textures, clean line art.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, elderly, old man, grandfather, deep wrinkles, weathered skin, sagging skin, gray hair, white hair`

### james_3 · `final/04_james/james_3_expressions.png`

- 생성: 시드 12403, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/04_james/r3/james_3_s12403_00001_.png`

**확장 입력 (요청)**

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: warm smile with crinkled eye lines; sheepish laugh while scratching the back of his head after a clumsy mistake; patiently waiting with a calm gentle gaze; worried with raised eyebrows; telling a gentle joke with one eyebrow up and a playful grin; quiet sadness with downcast eyes and a faint smile. Same hairstyle, outfit and accessories in every portrait. Every portrait is cropped at the chest, so no legs, boots or full-body figures appear anywhere on the sheet. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
James, a gentle father in his early forties, a youthful handsome adult face with smooth skin and only very faint smile lines at the corners of his eyes, kind warm eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly dark brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind smooth face in his early forties, and three stray strands of hair sticking out from his messy brown hair
```

**확장 프롬프트**

```
Expression sheet, six head-and-shoulders portraits of James in a two-row three-column grid, each showing a different emotion: warm smile with crinkled eye lines; sheepish laugh while scratching the back of his head after a clumsy mistake; patiently waiting with a calm gentle gaze; worried with raised eyebrows; telling a gentle joke with one eyebrow up and a playful grin; quiet sadness with downcast eyes and a faint smile. Same hairstyle, outfit and accessories in every portrait. Every portrait is cropped at the chest. James, a gentle father in his early forties, a youthful handsome adult face with smooth skin and only very faint smile lines at the corners of his eyes, kind warm eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly dark brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind smooth face in his early forties, and three stray strands of hair sticking out from his messy brown hair. Plain light gray studio background with a soft white glow, clean design sheet layout with a plain unmarked surface.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, elderly, old man, grandfather, deep wrinkles, weathered skin, sagging skin, gray hair, white hair`

### james_4 · `final/04_james/james_4_greenhouse.png`

- 생성: 시드 12404, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/04_james/r3/james_4_s12404_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, the tall gentle father watering rows of plants inside a sunlit glass greenhouse, warm light streaming through foggy glass panes, steam and green leaves, peaceful morning. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
James, a gentle father in his early forties, a youthful handsome adult face with smooth skin and only very faint smile lines at the corners of his eyes, kind warm eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly dark brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind smooth face in his early forties, and three stray strands of hair sticking out from his messy brown hair
```

**확장 프롬프트**

```
James, a gentle father in his early forties, youthful handsome adult face with smooth skin, faint smile lines at the corners of his eyes, kind warm eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly dark brown hair with three stray strands sticking out at the top like little cowlicks, slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, thin silver watch chain, very tall thin straight build with long limbs, kind smooth face, three stray strands of hair sticking out from his messy brown hair, watering rows of plants inside a sunlit glass greenhouse, warm light streaming through foggy glass panes, steam and green leaves, peaceful morning, luminous highly detailed painted backgrounds, glowing light particles, soft lens bloom, vivid saturated colors, cinematic depth of field.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, elderly, old man, grandfather, deep wrinkles, weathered skin, sagging skin, gray hair, white hair`

### james_5 · `final/04_james/james_5_doorframe.png`

- 생성: 시드 12405, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/04_james/r3/james_5_s12405_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, the very tall lanky father bending his long neck to pass under a low wooden doorframe of a cozy cottage and bumping his forehead lightly on the frame, rubbing his forehead and laughing at himself, warm interior light, gentle comedy. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
James, a gentle father in his early forties, a youthful handsome adult face with smooth skin and only very faint smile lines at the corners of his eyes, kind warm eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly dark brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind smooth face in his early forties, and three stray strands of hair sticking out from his messy brown hair
```

**확장 프롬프트**

```
James, a gentle father in his early forties, a youthful handsome adult face with smooth skin and only very faint smile lines at the corners of his eyes, kind warm eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly dark brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain, a very tall thin straight build with long limbs, a kind smooth face in his early forties, and three stray strands of hair sticking out from his messy brown hair, bending his long neck to pass under a low wooden doorframe of a cozy cottage and bumping his forehead lightly on the frame, rubbing his forehead and laughing at himself, warm interior light, gentle comedy, crisp clean line art, polished digital cel shading, large expressive eyes, glossy hair strands, luminous painted background, vivid saturated colors, cinematic depth of field, original character design.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, elderly, old man, grandfather, deep wrinkles, weathered skin, sagging skin, gray hair, white hair`

## 05_beth

### beth_1 · `final/05_beth/beth_1_turnaround.png`

- 생성: 시드 12501, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/05_beth/r3/beth_1_s12501_00001_.png`

**확장 입력 (요청)**

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest. Signature design point: a tall straight upright figure drawn with thin lines, the long wavy hair simplified into gentle wave lines, and a small amber brooch that matches the faint amber glint in her eyes
```

**확장 프롬프트**

```
Character model sheet featuring Beth, a calm middle-aged mother in her early forties, drawn three times side by side in front view, side view, and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and identical proportions in all three views, evenly spaced, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, deep forest-green long cardigan over a cream blouse, natural linen apron with a small notebook and a pencil in its front pocket, small amber brooch on her chest, plain light gray studio background with a soft white glow, clean design sheet layout, crisp clean line art with thin even dark lines, polished digital cel shading with two crisp shadow tones and a bright rim light along the edges, large expressive eyes with layered sparkling highlights, glossy light-catching hair strands, luminous highly detailed painted backgrounds with dramatic sky light, glowing light particles and soft lens bloom, vivid saturated colors with cool blue-violet shadows, cinematic depth of field, original character design.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### beth_2 · `final/05_beth/beth_2_tea.png`

- 생성: 시드 12502, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/05_beth/r3/beth_2_s12502_00001_.png`

**확장 입력 (요청)**

```
Full-body character key art of a single character, standing upright and calmly pouring tea from a ceramic teapot with precise graceful hands, a small notebook tucked in her apron pocket. the character described in the must-keep details. Soft simple background: a soft deep-forest-green and cream wash.
```

**확장 입력 (꼭 지킬 특징)**

```
Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest. Signature design point: a tall straight upright figure drawn with thin lines, the long wavy hair simplified into gentle wave lines, and a small amber brooch that matches the faint amber glint in her eyes
```

**확장 프롬프트**

```
Full-body character key art of Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, wearing a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest, standing upright and calmly pouring tea from a ceramic teapot with precise graceful hands, soft simple background of a soft deep-forest-green and cream wash, soft diffused lighting, wide shot framing, clean plain background, smooth linen texture, matte ceramic surface, crisp clean line art, polished digital cel shading, two crisp shadow tones, bright rim light along the edges, large expressive eyes with layered sparkling highlights, glossy light-catching hair strands, luminous highly detailed painted background, glowing light particles, soft lens bloom, vivid saturated colors, cool blue-violet shadows, cinematic depth of field, original character design.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### beth_3 · `final/05_beth/beth_3_expressions.png`

- 생성: 시드 12503, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/05_beth/r3/beth_3_s12503_00001_.png`

**확장 입력 (요청)**

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: calm neutral composure with straight eyebrows; a gentle subtle smile; firm determined look while speaking a short encouraging line; focused downward gaze as if writing in her notebook; a secretive sideways glance with a faint amber glint in her eyes; quiet worry with lips pressed together. Same hairstyle, outfit and accessories in every portrait. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest. Signature design point: a tall straight upright figure drawn with thin lines, the long wavy hair simplified into gentle wave lines, and a small amber brooch that matches the faint amber glint in her eyes
```

**확장 프롬프트**

```
Expression sheet, six head-and-shoulders portraits of Beth arranged in a neat grid of two rows and three columns, plain light gray studio background with a soft white glow, clean design sheet layout, calm neutral composure with straight eyebrows, gentle subtle smile, firm determined look speaking a short encouraging line, focused downward gaze writing in her notebook, secretive sideways glance with a faint amber glint in her eyes, quiet worry with lips pressed together, same long wavy black hair loosely tied at the nape in every portrait, deep forest-green long cardigan over a cream blouse, natural linen apron with a small notebook and a pencil in its front pocket, small amber brooch on her chest, intelligent calm mature face with faint lines at the corners of her eyes, dark chestnut eyes with faint amber glints, tall and slender upright straight posture, crisp clean line art, polished digital cel shading, large expressive eyes with layered sparkling highlights, glossy light-catching hair strands, vivid saturated colors with cool blue-violet shadows, cinematic depth of field.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### beth_4 · `final/05_beth/beth_4_greenhouse.png`

- 생성: 시드 12504, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/05_beth/r3/beth_4_s12504_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, the calm mother checking seedlings in a greenhouse at evening, the plants subtly leaning toward her, a barely visible faint blue-green glimmer passing over a leaf near her fingertip, warm lamp light, quiet mysterious mood. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest. Signature design point: a tall straight upright figure drawn with thin lines, the long wavy hair simplified into gentle wave lines, and a small amber brooch that matches the faint amber glint in her eyes
```

**확장 프롬프트**

```
Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest, checking seedlings in a greenhouse at evening, the plants subtly leaning toward her, a barely visible faint blue-green glimmer passing over a leaf near her fingertip, warm lamp light, quiet mysterious mood, medium shot from eye level, lush green foliage background, soft glass reflections, smooth fabric textures, crisp clean line art, polished digital cel shading, two crisp shadow tones, bright rim light, large expressive eyes, layered sparkling highlights, glossy light-catching hair strands, luminous painted backgrounds, dramatic sky light, glowing light particles, soft lens bloom, vivid saturated colors, cool blue-violet shadows, cinematic depth of field, original character design.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### beth_5 · `final/05_beth/beth_5_protect.png`

- 생성: 시드 12505, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/05_beth/r3/beth_5_s12505_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, the mother standing protectively with one arm spread out in front of her, strong wind, her loosely tied wavy black hair coming loose and flowing dramatically for the first time, a stormy dark-green background, intense determined eyes. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Beth, a calm middle-aged mother in her early forties, tall and slender with an upright straight posture, long wavy black hair loosely tied at the nape, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest. Signature design point: a tall straight upright figure drawn with thin lines, the long wavy hair simplified into gentle wave lines, and a small amber brooch that matches the faint amber glint in her eyes
```

**확장 프롬프트**

```
Beth, a calm middle-aged mother in her early forties, standing protectively with one arm spread out in front of her, strong wind, her loosely tied wavy black hair coming loose and flowing dramatically, a stormy dark-green background, intense determined eyes, tall and slender with an upright straight posture, an intelligent calm mature face with faint lines at the corners of her eyes and straight eyebrows, dark chestnut eyes with faint amber glints, a deep forest-green long cardigan over a cream blouse, a natural linen apron with a small notebook and a pencil in its front pocket, a small amber brooch on her chest, crisp clean line art with thin even dark lines, polished digital cel shading with two crisp shadow tones and a bright rim light along the edges, large expressive eyes with layered sparkling highlights, glossy light-catching hair strands, luminous highly detailed painted backgrounds with dramatic sky light, glowing light particles and soft lens bloom, vivid saturated colors with cool blue-violet shadows, cinematic depth of field, original character design.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

## 06_taoba

### taoba_1 · `final/06_taoba/taoba_1_turnaround.png`

- 생성: 시드 12601, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/06_taoba/r3/taoba_1_s12601_00001_.png`

**확장 입력 (요청)**

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Taoba, a jolly stocky gardener in his mid-fifties, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big bush-like shape around his face, a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass. Signature design point: his hair and beard are drawn as one big round bush-like mass around his face, on a big round pot-bellied body
```

**확장 프롬프트**

```
Character model sheet, Taoba drawn three times side by side, front view, side view, back view, full body, relaxed neutral standing pose, identical outfit and proportions, evenly spaced, plain light gray studio background with a soft white glow, clean design sheet layout, jolly stocky gardener in his mid-fifties, medium height, big round pot belly, round ruddy face, rosy cheeks, narrow eyes, curly bushy brown hair, thick bushy brown beard, few gray hairs, one big bush-like shape around his face, sage-green linen shirt with rolled sleeves, brown trousers with suspenders, tan leather work apron, labeled pockets, small garden tools, pruning shears, magnifying glass, hair and beard as one big round bush-like mass, big round pot-bellied body, crisp clean line art, thin even dark lines, polished digital cel shading, two crisp shadow tones, bright rim light, large expressive eyes, layered sparkling highlights, glossy light-catching hair strands, luminous painted backgrounds, dramatic sky light, glowing light particles, soft lens bloom, vivid saturated colors, cool blue-violet shadows, cinematic depth of field, original character design.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

**편집 지시 (시드 101)**

```
Change only his skin color: give him a natural warm light-tan skin tone on his face, neck, arms and hands, with only lightly rosy cheeks. Keep everything else exactly the same: his face shape, expression, curly brown hair and beard, clothes, apron, tools, pose, background, colors and anime style.
```

### taoba_2 · `final/06_taoba/taoba_2_keypose.png`

- 생성: 시드 12602, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/06_taoba/r3/taoba_2_s12602_00001_.png`

**확장 입력 (요청)**

```
Full-body character key art of a single character, laughing heartily with his arms open wide, wearing a worn straw hat, a tiny seedling pot held very gently in one big hand. the character described in the must-keep details. Soft simple background: a soft sage-green and dew-glass wash.
```

**확장 입력 (꼭 지킬 특징)**

```
Taoba, a jolly stocky gardener in his mid-fifties, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big bush-like shape around his face, a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass. Signature design point: his hair and beard are drawn as one big round bush-like mass around his face, on a big round pot-bellied body
```

**확장 프롬프트**

```
Full-body character key art of Taoba, a jolly stocky gardener in his mid-fifties, laughing heartily with his arms open wide, wearing a worn straw hat, a tiny seedling pot held very gently in one big hand. He has medium height with a big round pot belly, a round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles. His curly bushy brown hair and thick bushy brown beard with a few gray hairs merge into one big bush-like shape around his face. He wears a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, and a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass. Soft simple background: a soft sage-green and dew-glass wash. Bright warm lighting, wide shot, eye-level angle, clean line art, polished digital cel shading, vivid saturated colors.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### taoba_3 · `final/06_taoba/taoba_3_expressions.png`

- 생성: 시드 12603, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/06_taoba/r3/taoba_3_s12603_00001_.png`

**확장 입력 (요청)**

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: booming open-mouthed laugh with his eyes shut into happy curves; whispering softly to a sick plant with gentle eyes; gentle concern with raised bushy eyebrows; surprised with wide round eyes and an open mouth inside his beard; telling a joke with a wink; serious protective look with furrowed brows. Same hairstyle, outfit and accessories in every portrait. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Taoba, a jolly stocky gardener in his mid-fifties, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big bush-like shape around his face, a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass. Signature design point: his hair and beard are drawn as one big round bush-like mass around his face, on a big round pot-bellied body
```

**확장 프롬프트**

```
Expression sheet featuring six head-and-shoulders portraits of Taoba, a jolly stocky gardener in his mid-fifties, arranged in a neat grid of two rows and three columns. Taoba has a big round pot belly, a round ruddy face with rosy cheeks, and narrow eyes that turn into thin curved lines when smiling. His curly bushy brown hair and thick bushy brown beard with a few gray hairs merge into one big bush-like shape around his face. He wears a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, and a tan leather work apron with labeled pockets full of small garden tools, pruning shears, and a magnifying glass. The top-left portrait shows a booming open-mouthed laugh with eyes shut into happy curves. The top-middle portrait shows whispering softly to a sick plant with gentle eyes. The top-right portrait shows gentle concern with raised bushy eyebrows. The bottom-left portrait shows surprise with wide round eyes and an open mouth inside his beard. The bottom-middle portrait shows telling a joke with a wink. The bottom-right portrait shows a serious protective look with furrowed brows. The background is a plain light gray studio background with a soft white glow, presenting a clean design sheet layout.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

**편집 지시 (시드 101)**

```
Change only his skin color: give him a natural warm light-tan skin tone on his face, neck, arms and hands, with only lightly rosy cheeks. Keep everything else exactly the same: his face shape, expression, curly brown hair and beard, clothes, apron, tools, pose, background, colors and anime style.
```

### taoba_4 · `final/06_taoba/taoba_4_greenhouse.png`

- 생성: 시드 12604, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/06_taoba/r3/taoba_4_s12604_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, the round gardener kneeling inside his overgrown glass greenhouse full of potted plants with small wooden name tags, a small mist sprayer and dewy glass, examining a tiny seedling with surprisingly delicate fingers, warm green light. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Taoba, a jolly stocky gardener in his mid-fifties, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big bush-like shape around his face, a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass. Signature design point: his hair and beard are drawn as one big round bush-like mass around his face, on a big round pot-bellied body
```

**확장 프롬프트**

```
Taoba, a jolly stocky gardener in his mid-fifties, kneeling inside an overgrown glass greenhouse, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big bush-like shape around his face, wearing a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, and a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass, examining a tiny seedling with surprisingly delicate fingers, surrounded by potted plants with small wooden name tags, a small mist sprayer, and dewy glass, bathed in warm green light, close-up shot from a low angle, shallow depth of field, detailed textures of linen, leather, and glass, lush green environment, cinematic composition.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

**편집 지시 (시드 101)**

```
Change only his skin color: give him a natural warm light-tan skin tone on his face, neck, arms and hands, with only lightly rosy cheeks. Keep everything else exactly the same: his face shape, expression, curly brown hair and beard, clothes, apron, tools, pose, background, colors and anime style.
```

### taoba_5 · `final/06_taoba/taoba_5_vines.png`

- 생성: 시드 12605, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/06_taoba/r3/taoba_5_s12605_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, the round gardener caught and tangled in thick dark creeping vines inside a dim greenhouse, struggling but still grinning bravely, dramatic but not violent, cool shadows with warm highlights. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Taoba, a jolly stocky gardener in his mid-fifties, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes that turn into thin curved lines when he smiles, curly bushy brown hair and a thick bushy brown beard with a few gray hairs that merge into one big bush-like shape around his face, a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, a tan leather work apron whose labeled pockets are full of small garden tools, pruning shears and a magnifying glass. Signature design point: his hair and beard are drawn as one big round bush-like mass around his face, on a big round pot-bellied body
```

**확장 프롬프트**

```
Medium shot, eye-level angle, Taoba, a jolly stocky gardener in his mid-fifties, standing in the center of a dim greenhouse, medium height with a big round pot belly, round ruddy face with rosy cheeks and narrow eyes turned into thin curved lines in a brave grin, curly bushy brown hair and a thick bushy brown beard with gray hairs merging into one big round bush-like mass around his face, wearing a sage-green linen shirt with rolled sleeves, brown trousers with suspenders, and a tan leather work apron with labeled pockets full of small garden tools, pruning shears, and a magnifying glass, tangled in thick dark creeping vines that wrap around his torso and arms, struggling with a dynamic pose, arms raised slightly, cool blue-violet shadows contrasting with warm golden highlights on his face and apron, lush green foliage background, soft lens bloom, crisp clean line art, polished digital cel shading, two crisp shadow tones, bright rim light, large expressive eyes, glossy hair strands, luminous painted background, vivid saturated colors, cinematic depth of field, original character design.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

**편집 지시 (시드 101)**

```
Change only his skin color: give him a natural warm light-tan skin tone on his face, neck, arms and hands, with only lightly rosy cheeks. Keep everything else exactly the same: his face shape, expression, curly brown hair and beard, clothes, apron, vines, pose, background, colors and anime style.
```

## 07_ilia

### ilia_1 · `final/07_ilia/ilia_1_turnaround.png`

- 생성: 시드 12701, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/07_ilia/r3/ilia_1_s12701_00001_.png`

**확장 입력 (요청)**

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Ilia, a slim young woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, a practical apron, a folding notebook and small garden scissors hanging at her waist. Signature design point: a straight upright posture and a brown ponytail tied with a powder-blue ribbon, the ponytail stands up when she is angry and droops softly when she is gentle
```

**확장 프롬프트**

```
Character model sheet featuring one slim young woman named Ilia, drawn three times side by side in front view, side view, and back view, evenly spaced across a clean layout. Each figure displays a full body view from head to toe in a relaxed neutral standing pose with upright posture, identical proportions and outfit in all three instances. Ilia has a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, and a kind confident expression. She wears a sage-green work jacket over a cream t-shirt, with a practical apron, a folding notebook, and small garden scissors hanging at her waist. The background is a plain light gray studio background with a soft white glow, presenting a clean design sheet aesthetic with a clean plain background. The lighting is soft and even, highlighting the crisp line art and cel shading details.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### ilia_2 · `final/07_ilia/ilia_2_keypose.png`

- 생성: 시드 12702, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/07_ilia/r3/ilia_2_s12702_00001_.png`

**확장 입력 (요청)**

```
Full-body character key art of a single character, standing tall with one hand on her hip and the other holding an open folding notebook, giving brisk instructions, then glancing back with a warm smile. the character described in the must-keep details. Soft simple background: a soft powder-blue and sage-green wash.
```

**확장 입력 (꼭 지킬 특징)**

```
Ilia, a slim young woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, a practical apron, a folding notebook and small garden scissors hanging at her waist. Signature design point: a straight upright posture and a brown ponytail tied with a powder-blue ribbon, the ponytail stands up when she is angry and droops softly when she is gentle
```

**확장 프롬프트**

```
Full-body character key art of Ilia, a slim young woman in her mid-twenties, standing tall with an upright posture, one hand on her hip and the other holding an open folding notebook, giving brisk instructions, then glancing back with a warm smile, neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, sage-green work jacket over a cream t-shirt, practical apron, small garden scissors hanging at her waist, soft powder-blue and sage-green wash background, crisp clean line art with thin even dark lines, polished digital cel shading with two crisp shadow tones and a bright rim light along the edges, large expressive eyes with layered sparkling highlights, glossy light-catching hair strands, luminous highly detailed painted backgrounds with dramatic sky light, glowing light particles and soft lens bloom, vivid saturated colors with cool blue-violet shadows, cinematic depth of field, original character design.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### ilia_3 · `final/07_ilia/ilia_3_expressions.png`

- 생성: 시드 12703, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/07_ilia/r3/ilia_3_s12703_00001_.png`

**확장 입력 (요청)**

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: firm scolding with a raised finger and her ponytail sticking straight up; warm big-sister smile with the ponytail hanging softly; confident and focused with sharp eyes; exasperated sigh with closed eyes; gentle reassuring look with her head tilted as if asking are you okay; laughing openly. Same hairstyle, outfit and accessories in every portrait. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Ilia, a slim young woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, a practical apron, a folding notebook and small garden scissors hanging at her waist. Signature design point: a straight upright posture and a brown ponytail tied with a powder-blue ribbon, the ponytail stands up when she is angry and droops softly when she is gentle
```

**확장 프롬프트**

```
Expression sheet featuring six head-and-shoulders portraits of Ilia, a slim young woman in her mid-twenties, arranged in a neat grid of two rows and three columns. Each portrait displays a distinct emotion: firm scolding with a raised finger and her ponytail sticking straight up; warm big-sister smile with the ponytail hanging softly; confident and focused with sharp eyes; exasperated sigh with closed eyes; gentle reassuring look with her head tilted; and laughing openly. Ilia wears a sage-green work jacket over a cream t-shirt, a practical apron, and has a folding notebook and small garden scissors hanging at her waist. Her neat brown ponytail is tied with a powder-blue ribbon, with smooth forehead, sharp clear eyebrows, and clear well-defined features. The background is a plain light gray studio background with a soft white glow, maintaining a clean design sheet layout. The lighting is soft and even, highlighting the crisp line art and polished digital cel shading. The camera uses a straight-on frontal angle for each portrait, ensuring consistent framing and composition across the grid. Textures include the matte fabric of the jacket, the smooth skin, and the glossy ribbon.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### ilia_4 · `final/07_ilia/ilia_4_ribbon.png`

- 생성: 시드 12704, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/07_ilia/r3/ilia_4_s12704_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, inside a sunny greenhouse, the young woman kneels on the left and ties her own powder-blue hair ribbon into the black bob hair of a small shy 12-year-old girl with a jet-black bob in a wine-red cape coat, the floppy ends of her extremely long cream sleeves dangling over her hands so that her hands stay hidden, who stands on the right, tender big-sister moment, warm light. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Ilia, a slim young woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, a practical apron, a folding notebook and small garden scissors hanging at her waist. Signature design point: a straight upright posture and a brown ponytail tied with a powder-blue ribbon, the ponytail stands up when she is angry and droops softly when she is gentle
```

**확장 프롬프트**

```
Animation film key frame, inside a sunny greenhouse, warm light, Ilia, a slim young woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, a practical apron, a folding notebook and small garden scissors hanging at her waist, kneels on the left, ties her own powder-blue hair ribbon into the black bob hair of a small shy 12-year-old girl with a jet-black bob in a wine-red cape coat, who stands on the right, tender big-sister moment, the floppy ends of her extremely long cream sleeves dangling over her hands so that her hands stay hidden, oversized sleeves hanging well past the wrists, the cuffs closed and drooping, the ribbon tucked inside the drooping sleeve cuff and propped against the shoulder, crisp clean line art, polished digital cel shading, large expressive eyes, glossy light-catching hair strands, luminous highly detailed painted backgrounds, glowing light particles, soft lens bloom, vivid saturated colors, cinematic depth of field.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, visible hands, fingers, bare hands, hands outside the sleeves`

### ilia_5 · `final/07_ilia/ilia_5_greenhouse.png`

- 생성: 시드 12705, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/07_ilia/r3/ilia_5_s12705_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, the young woman walking briskly between rows of seedlings in a greenhouse, checking a care schedule in her folding notebook with a pencil, garden scissors at her waist, busy morning light. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Ilia, a slim young woman in her mid-twenties, medium height, upright posture, a neat brown ponytail tied with a powder-blue ribbon, smooth forehead, sharp clear eyebrows, clear well-defined features, kind confident expression, a sage-green work jacket over a cream t-shirt, a practical apron, a folding notebook and small garden scissors hanging at her waist. Signature design point: a straight upright posture and a brown ponytail tied with a powder-blue ribbon, the ponytail stands up when she is angry and droops softly when she is gentle
```

**확장 프롬프트**

```
Ilia, a slim young woman in her mid-twenties with medium height and upright posture, walking briskly between rows of seedlings in a greenhouse. She has a neat brown ponytail tied with a powder-blue ribbon, a smooth forehead, sharp clear eyebrows, and a kind confident expression. She wears a sage-green work jacket over a cream t-shirt and a practical apron. A folding notebook rests in her hands as she checks a care schedule with a pencil, while small garden scissors hang at her waist. The scene is bathed in busy morning light, with luminous highly detailed painted backgrounds and glowing light particles. The camera captures a medium shot from a slightly low angle, emphasizing her steady movement and the vibrant green textures of the seedlings.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

## 08_iloke

### iloke_1 · `final/08_iloke/iloke_1_turnaround.png`

- 생성: 시드 12801, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/08_iloke/r3/iloke_1_s12801_00001_.png`

**확장 입력 (요청)**

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt. Signature design point: a big broad rectangular body shape, neat short hair, brown leather accents, and gloved hands that always offer something first
```

**확장 프롬프트**

```
Character model sheet featuring the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced, Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt, big broad rectangular body shape, neat short hair, brown leather accents, gloved hands that always offer something first, plain light gray studio background with a soft white glow, clean design sheet layout with a clean plain background.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### iloke_2 · `final/08_iloke/iloke_2_handkerchief.png`

- 생성: 시드 12802, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/08_iloke/r3/iloke_2_s12802_00001_.png`

**확장 입력 (요청)**

```
Full-body character key art of a single character, silently holding out a folded handkerchief with one gloved hand, the other hand holding a closed umbrella, a tiny warm smile only in his eyes. the character described in the must-keep details. Soft simple background: a soft deep-forest-green and cream wash.
```

**확장 입력 (꼭 지킬 특징)**

```
Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt. Signature design point: a big broad rectangular body shape, neat short hair, brown leather accents, and gloved hands that always offer something first
```

**확장 프롬프트**

```
Full-body character key art of Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a tiny warm smile only in his eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt, silently holding out a folded handkerchief with one gloved hand, the other hand holding a closed umbrella, soft simple background, a soft deep-forest-green and cream wash, soft diffused lighting, eye-level full-body shot, centered composition, matte fabric textures, smooth leather surfaces, clean line art, polished digital cel shading, two crisp shadow tones, bright rim light, large expressive eyes, layered sparkling highlights, glossy light-catching hair strands, luminous painted background, dramatic sky light, glowing light particles, soft lens bloom, vivid saturated colors, cool blue-violet shadows, cinematic depth of field.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### iloke_3 · `final/08_iloke/iloke_3_expressions.png`

- 생성: 시드 12803, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/08_iloke/r3/iloke_3_s12803_00001_.png`

**확장 입력 (요청)**

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: calm stoic face; a tiny smile only in his eyes; quiet concern with slightly knitted brows; slight embarrassment looking away with a faint blush; firm protective look; relaxed and sleepy with half-closed eyes. Same hairstyle, outfit and accessories in every portrait. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt. Signature design point: a big broad rectangular body shape, neat short hair, brown leather accents, and gloved hands that always offer something first
```

**확장 프롬프트**

```
Expression sheet featuring six head-and-shoulders portraits of Iloke, a quiet young man in his mid-twenties, arranged in a neat grid of two rows and three columns. Each portrait displays a distinct emotion: calm stoic face, a tiny smile only in his eyes, quiet concern with slightly knitted brows, slight embarrassment looking away with a faint blush, firm protective look, and relaxed and sleepy with half-closed eyes. Iloke has neat short very dark brown hair, thick eyebrows, an angular square jaw, and steady gentle eyes. He wears a deep forest-green work vest over a cream linen shirt with rolled sleeves, a brown leather belt, and brown leather work gloves. A folded umbrella hangs from his belt in every frame. The background is a plain light gray studio background with a soft white glow, maintaining a clean design sheet layout. The lighting is soft and even, highlighting the crisp line art and polished digital cel shading. The camera uses a consistent frontal angle for each grid cell to ensure uniformity. Textures include the matte fabric of the linen shirt, the smooth leather of the gloves and belt, and the subtle sheen on the hair strands.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### iloke_4 · `final/08_iloke/iloke_4_umbrella.png`

- 생성: 시드 12804, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/08_iloke/r3/iloke_4_s12804_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, rainy day on a garden path, the tall quiet young man on the left tilts his umbrella over a small shy 12-year-old girl with a jet-black bob in a wine-red cape coat, the floppy ends of her extremely long cream sleeves dangling over her hands so that her hands stay hidden, who walks on the right, his gloved hand lightly holding her arm over her sleeve, his own shoulder getting wet, soft gray rain and green leaves, quiet kindness. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt. Signature design point: a big broad rectangular body shape, neat short hair, brown leather accents, and gloved hands that always offer something first
```

**확장 프롬프트**

```
A tall quiet young man on the left tilts his umbrella over a small shy 12-year-old girl on the right, the girl has a jet-black bob and wears a wine-red cape coat with extremely long cream sleeves dangling over her hidden hands, the man wears a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves, and a brown leather belt with a folded umbrella hanging from it, his gloved hand lightly holding her arm over her sleeve, his shoulder getting wet, soft gray rain falls on green leaves, a garden path background, medium shot, eye-level angle, soft diffused lighting, wet textures on leaves and clothing, quiet kindness atmosphere.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, visible hands, fingers, bare hands, hands outside the sleeves`

### iloke_5 · `final/08_iloke/iloke_5_pots.png`

- 생성: 시드 12805, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/08_iloke/r3/iloke_5_s12805_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, the tall young man walking one step ahead on a muddy garden path carrying two heavy clay flower pots, clearing the way, leather gloves, calm steady stride, morning mist. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt. Signature design point: a big broad rectangular body shape, neat short hair, brown leather accents, and gloved hands that always offer something first
```

**확장 프롬프트**

```
Iloke, a quiet young man in his mid-twenties, tall and sturdy with broad shoulders, neat short very dark brown hair, thick eyebrows, angular square jaw, steady gentle eyes, a deep forest-green work vest over a cream linen shirt with rolled sleeves, brown leather work gloves and a brown leather belt, plain practical clothes, a folded umbrella hanging from his belt, walking one step ahead on a muddy garden path carrying two heavy clay flower pots, clearing the way, calm steady stride, morning mist, big broad rectangular body shape, brown leather accents, gloved hands, soft diffused morning light with cool blue-violet shadows and a bright rim light along the edges, medium shot at eye level with cinematic depth of field, lush garden with wet soil textures and soft atmospheric haze, wet soil textures and soft atmospheric haze.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

## 09_iluki

### iluki_1 · `final/09_iluki/iluki_1_turnaround.png`

- 생성: 시드 12901, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/09_iluki/r3/iluki_1_s12901_00001_.png`

**확장 입력 (요청)**

```
Character model sheet: the same single character drawn three times side by side, front view, side view and back view, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Signature design point: a thin body with big gestures, a sharp pointed chin, curly chestnut hair, freckles only on the nose and upper cheeks, and the mustard-yellow sweater that catches the eye first
```

**확장 프롬프트**

```
Character model sheet featuring the same single young man drawn three times side by side in front, side, and back views, full body from head to toe, relaxed neutral standing pose, identical outfit and proportions in all three views, evenly spaced. Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin. Wearing an oversized mustard-yellow knit sweater with sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Plain light gray studio background with a soft white glow, clean design sheet layout, crisp clean line art, polished digital cel shading, two crisp shadow tones, bright rim light, large expressive eyes, glossy light-catching hair strands, vivid saturated colors, cool blue-violet shadows, cinematic depth of field.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### iluki_2 · `final/09_iluki/iluki_2_keypose.png`

- 생성: 시드 12902, 1056x1584, 원본 `main/2026-10-27/niki_compass_v2/09_iluki/r3/iluki_2_s12902_00001_.png`

**확장 입력 (요청)**

```
Full-body character key art of a single character, in a dynamic exaggerated pose, leaning forward and winking while holding up a little toy frog toward the viewer to make someone laugh. the character described in the must-keep details. Soft simple background: a soft mustard-yellow and cream wash.
```

**확장 입력 (꼭 지킬 특징)**

```
Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Signature design point: a thin body with big gestures, a sharp pointed chin, curly chestnut hair, freckles only on the nose and upper cheeks, and the mustard-yellow sweater that catches the eye first
```

**확장 프롬프트**

```
Full-body character key art of Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket, dynamic exaggerated pose leaning forward, winking, holding up a little toy frog toward the viewer to make someone laugh, soft simple background, soft mustard-yellow and cream wash, crisp clean line art, thin even dark lines, polished digital cel shading, two crisp shadow tones, bright rim light along the edges, large expressive eyes, layered sparkling highlights, glossy light-catching hair strands, luminous highly detailed painted backgrounds, dramatic sky light, glowing light particles, soft lens bloom, vivid saturated colors, cool blue-violet shadows, cinematic depth of field, original character design.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### iluki_3 · `final/09_iluki/iluki_3_expressions.png`

- 생성: 시드 12903, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/09_iluki/r3/iluki_3_s12903_00001_.png`

**확장 입력 (요청)**

```
Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: huge mischievous grin showing his teeth; exaggerated shocked face with bulging eyes and a dropped jaw; pouting with puffed cheeks after being scolded; sneaky plotting look with narrowed eyes; laughing so hard that tears gather at the corners of his eyes; a rare sincere gentle smile. Same hairstyle, outfit and accessories in every portrait. the character described in the must-keep details. Plain light gray studio background with a soft white glow, clean design sheet layout without any lettering or captions.
```

**확장 입력 (꼭 지킬 특징)**

```
Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Signature design point: a thin body with big gestures, a sharp pointed chin, curly chestnut hair, freckles only on the nose and upper cheeks, and the mustard-yellow sweater that catches the eye first
```

**확장 프롬프트**

```
Expression sheet, six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: huge mischievous grin showing his teeth, exaggerated shocked face with bulging eyes and a dropped jaw, pouting with puffed cheeks after being scolded, sneaky plotting look with narrowed eyes, laughing so hard that tears gather at the corners of his eyes, a rare sincere gentle smile. Same hairstyle, outfit and accessories in every portrait. Iluki is a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, wearing an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Plain light gray studio background with a soft white glow, clean design sheet layout, crisp clean line art, polished digital cel shading, large expressive eyes with layered sparkling highlights, glossy light-catching hair strands, vivid saturated colors with cool blue-violet shadows.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`

### iluki_4 · `final/09_iluki/iluki_4_toys.png`

- 생성: 시드 12904, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/09_iluki/r3/iluki_4_s12904_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, in a greenhouse, the playful young man crouches on the left and shows a toy insect and a toy frog from his stuffed pockets to a small shy 12-year-old girl with a jet-black bob in a wine-red cape coat, the floppy ends of her extremely long cream sleeves dangling over her hands so that her hands stay hidden, who stands on the right and giggles behind her sleeve ends, cheerful warm light. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Signature design point: a thin body with big gestures, a sharp pointed chin, curly chestnut hair, freckles only on the nose and upper cheeks, and the mustard-yellow sweater that catches the eye first
```

**확장 프롬프트**

```
Animation film key frame in a greenhouse, cheerful warm light, medium shot at eye level, Iluki a playful young man crouches on the left, medium height, thin body with big gestures, sharp pointed chin, curly chestnut hair, freckles only on the nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, oversized mustard-yellow sweater with sleeves pushed up to the elbows, cream shirt collar, baggy trousers with stuffed pockets, a little toy frog peeking out, holding a toy insect, a small shy 12-year-old girl stands on the right, jet-black bob, wine-red cape coat, extremely long cream sleeves dangling over her hands so that her hands stay hidden, oversized sleeves hanging well past the wrists, the cuffs closed and drooping, giggles behind her sleeve ends, glossy light-catching hair strands, luminous painted backgrounds, glowing light particles, soft lens bloom, vivid saturated colors, cool blue-violet shadows, cinematic depth of field, original character design.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed, visible hands, fingers, bare hands, hands outside the sleeves`

### iluki_5 · `final/09_iluki/iluki_5_scolded.png`

- 생성: 시드 12905, 1584x1056, 원본 `main/2026-10-27/niki_compass_v2/09_iluki/r3/iluki_5_s12905_00001_.png`

**확장 입력 (요청)**

```
Animation film key frame, comedic moment in a greenhouse: on the left, a slim young woman in her mid-twenties with a neat brown ponytail tied with a powder-blue ribbon, wearing a sage-green work jacket and an apron, stands with one hand on her hip, scolding and confiscating a toy frog and toy insects; on the right, the playful young man pouts with puffed cheeks and his empty pockets turned out, warm light. the character described in the must-keep details.
```

**확장 입력 (꼭 지킬 특징)**

```
Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket. Signature design point: a thin body with big gestures, a sharp pointed chin, curly chestnut hair, freckles only on the nose and upper cheeks, and the mustard-yellow sweater that catches the eye first
```

**확장 프롬프트**

```
Animation film key frame, comedic moment in a greenhouse, on the left, a slim young woman in her mid-twenties with a neat brown ponytail tied with a powder-blue ribbon, wearing a sage-green work jacket and an apron, stands with one hand on her hip, scolding and confiscating a toy frog and toy insects; on the right, Iluki, a playful thin young man in his mid-twenties, medium height, sharp pointed chin, short curly chestnut-brown hair, freckles only across his nose and upper cheeks, pale skin, big expressive eyebrows, mischievous grin, an oversized mustard-yellow knit sweater with the sleeves pushed up to the elbows, a cream shirt collar, baggy trousers with bulging pockets stuffed with toys, a little toy frog peeking out of one pocket, pouts with puffed cheeks and his empty pockets turned out, warm light, crisp clean line art, polished digital cel shading, two crisp shadow tones, bright rim light, large expressive eyes, layered sparkling highlights, glossy light-catching hair strands, luminous highly detailed painted backgrounds, dramatic sky light, glowing light particles, soft lens bloom, vivid saturated colors, cool blue-violet shadows, cinematic depth of field, original character design.
```

- 부정 프롬프트 추가: `semi-realistic, realistic face, realistic skin, skin pores, detailed wrinkles, wrinkle shading, digital painting, concept art, painterly, western cartoon, caricature, 3d cartoon, hyperdetailed`
