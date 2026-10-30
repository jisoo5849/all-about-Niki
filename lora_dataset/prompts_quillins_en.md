# 퀼린스 두 모습 프롬프트 (영문)

- 두건 모습(얼굴 없음)과 정체 공개 모습(얼굴 드러남)을 다른 LoRA 로 학습하도록 20장씩 나눴다.
- 두건 모습은 4개 모델, 정체 공개 모습은 klein·Qwen 2개 모델에 같은 프롬프트·시드로 만들었다.
- 두 모습 모두 그림체 문장에서 큰 눈·볼 홍조를 뺐다 (두건 속 얼굴, 어린 얼굴이 나와서).
- 부정어는 두건 모습에 `face, eyes, glowing eyes, skin`, 정체 공개 모습에 `hood on head, hooded head, hood covering the hair, bald, shaved head, young man, teenager, elderly, very old man, completely white hair, large red circle, big medallion` 를 더했다 (cfg 4 인 Qwen 에서만 듣는다).

### quillins_hood_01 · full · front · 1024x1536 · 시드 21301

```
Full-body illustration of a single hooded figure from head to toe, front view facing the viewer, standing perfectly still. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Plain soft cream background without any lettering.
```

### quillins_hood_02 · full · 3ql · 1024x1536 · 시드 21302

```
Full-body illustration of a single hooded figure from head to toe, three-quarter view turned slightly to the left, walking slowly with the black cloak dragging behind him. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Plain soft cream background without any lettering.
```

### quillins_hood_03 · full · 3qr · 1024x1536 · 시드 21303

```
Full-body illustration of a single hooded figure from head to toe, three-quarter view turned slightly to the right, standing perfectly still. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Plain soft cream background without any lettering.
```

### quillins_hood_04 · full · side · 1024x1536 · 시드 21304

```
Full-body illustration of a single hooded figure from head to toe, side profile view facing right, in profile, standing perfectly still. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Plain soft cream background without any lettering.
```

### quillins_hood_05 · full · back · 1024x1536 · 시드 21305

```
Full-body illustration of a single hooded figure from head to toe, rear view, the character stands facing away from the viewer toward the background, so we see only the back, the back of the hood, standing perfectly still. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Plain soft cream background without any lettering.
```

### quillins_hood_06 · full · 3qr · 1024x1536 · 시드 21306

```
Full-body illustration of a single hooded figure from head to toe, three-quarter view turned slightly to the right, standing at the edge of a cliff with the cloak blowing in the wind. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Background: a rocky shore at night under cold blue-gray moonlight, painted in soft watercolor detail.
```

### quillins_hood_07 · full · front · 1024x1536 · 시드 21307

```
Full-body illustration of a single hooded figure from head to toe, front view facing the viewer, crouching over a tide pool, one black-gloved hand reaching toward the water. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Background: a foggy pine forest, painted in soft watercolor detail.
```

### quillins_hood_08 · full · 3ql · 1024x1536 · 시드 21308

```
Full-body illustration of a single hooded figure from head to toe, three-quarter view turned slightly to the left, turning away into the fog. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Background: a ruined stone pier by a gray sea, painted in soft watercolor detail.
```

### quillins_hood_09 · waist · front · 1024x1280 · 시드 21309

```
Medium shot from the waist up of a single hooded figure, the picture is cropped at the waist so the legs are out of frame, front view facing the viewer, standing perfectly still, the empty black shadow inside the hood facing the viewer. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak. Plain soft cream background without any lettering.
```

### quillins_hood_10 · waist · 3qr · 1024x1280 · 시드 21310

```
Medium shot from the waist up of a single hooded figure, the picture is cropped at the waist so the legs are out of frame, three-quarter view turned slightly to the right, standing still with the deep black hood turned toward the sea. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak. Background: a rocky shore at night under cold blue-gray moonlight, painted in soft watercolor detail.
```

### quillins_hood_11 · waist · side · 1024x1280 · 시드 21311

```
Medium shot from the waist up of a single hooded figure, the picture is cropped at the waist so the legs are out of frame, side profile view facing right, in profile, standing still in profile, the deep hood hiding his face. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak. Background: a foggy pine forest, painted in soft watercolor detail.
```

### quillins_hood_12 · face · front · 1024x1024 · 시드 21312

```
Close-up of a single hooded figure, the hooded head and shoulders fill the whole picture, cropped just below the shoulders, front view facing the viewer, the deep hood filling the picture, its inside pure black shadow with no face. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak. Plain soft cream background without any lettering.
```

### quillins_hood_13 · face · 3ql · 1024x1024 · 시드 21313

```
Close-up of a single hooded figure, the hooded head and shoulders fill the whole picture, cropped just below the shoulders, three-quarter view turned slightly to the left, the deep hood and fur-trimmed collar filling the picture, the inside of the hood pure black. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak. Background: a ruined stone pier by a gray sea, painted in soft watercolor detail.
```

### quillins_hood_14 · waist · 3ql · 1024x1280 · 시드 21314

```
Medium shot from the waist up of a single hooded figure, the picture is cropped at the waist so the legs are out of frame, three-quarter view turned slightly to the left, one black-gloved hand raised to hold the edge of his cloak closed. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak. Background: an empty beach at dawn, painted in soft watercolor detail.
```

### quillins_hood_15 · full · front · 1024x1536 · 시드 21315

```
Full-body illustration of a single hooded figure from head to toe, front view facing the viewer, looming over the viewer from a low camera angle, the cloak spreading like ink. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Background: a rocky shore at night under cold blue-gray moonlight, painted in soft watercolor detail.
```

### quillins_hood_16 · full · back · 1024x1536 · 시드 21316

```
Full-body illustration of a single hooded figure from head to toe, rear view, the character stands facing away from the viewer toward the background, so we see only the back, the back of the hood, standing still and looking out at the night sea. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Background: a rocky shore at night under cold blue-gray moonlight, painted in soft watercolor detail.
```

### quillins_hood_17 · full · 3qr · 1024x1536 · 시드 21317

```
Full-body illustration of a single hooded figure from head to toe, three-quarter view turned slightly to the right, walking slowly along the waterline, the cloak hem dragging over wet sand. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Background: an empty beach at dawn, painted in soft watercolor detail.
```

### quillins_hood_18 · full · side · 1024x1536 · 시드 21318

```
Full-body illustration of a single hooded figure from head to toe, side profile view facing right, in profile, standing between dark pine trunks in the fog. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Background: a foggy pine forest, painted in soft watercolor detail.
```

### quillins_hood_19 · waist · front · 1024x1280 · 시드 21319

```
Medium shot from the waist up of a single hooded figure, the picture is cropped at the waist so the legs are out of frame, front view facing the viewer, standing at the end of a stone pier, the wind pulling at the cloak. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak. Background: a ruined stone pier by a gray sea, painted in soft watercolor detail.
```

### quillins_hood_20 · full · front · 1024x1536 · 시드 21320

```
Full-body illustration of a single hooded figure from head to toe, front view facing the viewer, standing with both black-gloved hands hanging at his sides. Quillins, a tall thin man with drooping shoulders, wrapped in a worn ink-black hooded cloak with fur trim and bone toggles, the opening of his deep hood is filled completely with solid pitch-black shadow, a smooth black oval of darkness where a head should be, a mysterious hooded shadow figure, black leather gloves, a glimpse of a dark indigo coat under the cloak, the cloak hem dragging on the ground. Plain soft cream background without any lettering.
```

### quillins_face_01 · full · front · 1024x1536 · 시드 23351

```
Full-body illustration of a single character from head to toe, front view facing the viewer, standing with his back straight. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves, the worn ink-black cloak hanging down to his black boots. Plain soft cream background without any lettering.
```

### quillins_face_02 · full · 3ql · 1024x1536 · 시드 23352

```
Full-body illustration of a single character from head to toe, three-quarter view turned slightly to the left, walking slowly along the waterline. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves, the worn ink-black cloak hanging down to his black boots. Plain soft cream background without any lettering.
```

### quillins_face_03 · full · 3qr · 1024x1536 · 시드 23353

```
Full-body illustration of a single character from head to toe, three-quarter view turned slightly to the right, standing with his back straight. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves, the worn ink-black cloak hanging down to his black boots. Plain soft cream background without any lettering.
```

### quillins_face_04 · full · side · 1024x1536 · 시드 23354

```
Full-body illustration of a single character from head to toe, side profile view facing right, in profile with only one eye visible, standing with his back straight. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves, the worn ink-black cloak hanging down to his black boots. Plain soft cream background without any lettering.
```

### quillins_face_05 · full · back · 1024x1536 · 시드 23355

```
Full-body illustration of a single character from head to toe, rear view, the character stands facing away from the viewer toward the background, so we see only the back, the back of the head and the hair, standing with his back straight. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves, the worn ink-black cloak hanging down to his black boots. Plain soft cream background without any lettering.
```

### quillins_face_06 · full · 3qr · 1024x1536 · 시드 23356

```
Full-body illustration of a single character from head to toe, three-quarter view turned slightly to the right, kneeling on wet sand beside a young gray seal pup with a bandaged flipper. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves, the worn ink-black cloak hanging down to his black boots. Background: a rocky shore at night under cold blue-gray moonlight, painted in soft watercolor detail.
```

### quillins_face_07 · full · front · 1024x1536 · 시드 23357

```
Full-body illustration of a single character from head to toe, front view facing the viewer, sitting on a large rock with his gloved hands resting on his knees. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves, the worn ink-black cloak hanging down to his black boots. Background: a foggy pine forest, painted in soft watercolor detail.
```

### quillins_face_08 · full · 3ql · 1024x1536 · 시드 23358

```
Full-body illustration of a single character from head to toe, three-quarter view turned slightly to the left, standing at the end of a stone pier looking out at the sea. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves, the worn ink-black cloak hanging down to his black boots. Background: a ruined stone pier by a gray sea, painted in soft watercolor detail.
```

### quillins_face_09 · waist · front · 1024x1280 · 시드 23359

```
Medium shot from the waist up of a single character, the picture is cropped at the waist so the legs are out of frame, front view facing the viewer, tired sorrowful eyes looking down. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Plain soft cream background without any lettering.
```

### quillins_face_10 · waist · 3qr · 1024x1280 · 시드 23360

```
Medium shot from the waist up of a single character, the picture is cropped at the waist so the legs are out of frame, three-quarter view turned slightly to the right, a faint sad smile. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Plain soft cream background without any lettering.
```

### quillins_face_11 · waist · 3ql · 1024x1280 · 시드 23361

```
Medium shot from the waist up of a single character, the picture is cropped at the waist so the legs are out of frame, three-quarter view turned slightly to the left, a stern cold stare. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Background: a rocky shore at night under cold blue-gray moonlight, painted in soft watercolor detail.
```

### quillins_face_12 · waist · side · 1024x1280 · 시드 23362

```
Medium shot from the waist up of a single character, the picture is cropped at the waist so the legs are out of frame, side profile view facing right, in profile with only one eye visible, quiet surprise. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Background: a foggy pine forest, painted in soft watercolor detail.
```

### quillins_face_13 · waist · front · 1024x1280 · 시드 23363

```
Medium shot from the waist up of a single character, the picture is cropped at the waist so the legs are out of frame, front view facing the viewer, a pained grimace. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Background: a ruined stone pier by a gray sea, painted in soft watercolor detail.
```

### quillins_face_14 · waist · 3qr · 1024x1280 · 시드 23364

```
Medium shot from the waist up of a single character, the picture is cropped at the waist so the legs are out of frame, three-quarter view turned slightly to the right, a gentle soft look. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Background: an empty beach at dawn, painted in soft watercolor detail.
```

### quillins_face_15 · face · front · 1024x1024 · 시드 23365

```
Close-up portrait of a single character, the face and shoulders fill the whole picture, cropped just below the shoulders, front view facing the viewer, tired sorrowful eyes looking down. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Plain soft cream background without any lettering.
```

### quillins_face_16 · face · 3ql · 1024x1024 · 시드 23366

```
Close-up portrait of a single character, the face and shoulders fill the whole picture, cropped just below the shoulders, three-quarter view turned slightly to the left, a faint sad smile. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Plain soft cream background without any lettering.
```

### quillins_face_17 · face · 3qr · 1024x1024 · 시드 23367

```
Close-up portrait of a single character, the face and shoulders fill the whole picture, cropped just below the shoulders, three-quarter view turned slightly to the right, a stern cold stare. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Background: an empty beach at dawn, painted in soft watercolor detail.
```

### quillins_face_18 · face · side · 1024x1024 · 시드 23368

```
Close-up portrait of a single character, the face and shoulders fill the whole picture, cropped just below the shoulders, side profile view facing right, in profile with only one eye visible, calm tired face looking into the distance. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Plain soft cream background without any lettering.
```

### quillins_face_19 · face · front · 1024x1024 · 시드 23369

```
Close-up portrait of a single character, the face and shoulders fill the whole picture, cropped just below the shoulders, front view facing the viewer, quiet surprise. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Background: a rocky shore at night under cold blue-gray moonlight, painted in soft watercolor detail.
```

### quillins_face_20 · face · 3ql · 1024x1024 · 시드 23370

```
Close-up portrait of a single character, the face and shoulders fill the whole picture, cropped just below the shoulders, three-quarter view turned slightly to the left, a pained grimace. Quillins, a weathered fifty-seven-year-old man whose face clearly shows his late fifties, middle-aged rather than elderly, tall and thin with drooping shoulders, a full head of messy shoulder-length black hair streaked with gray and white, fully visible, his black hood folded down and resting on his shoulders behind his neck, a long lean face with hollow cheeks and a firm jaw, a few faint lines on his forehead and beside his eyes, visible signs of age: deep lines from his nose to the corners of his mouth, crow's feet at the corners of his eyes, a creased forehead, gray stubble on his chin and jaw, graying sideburns, narrow tired dark gray eyes with a black tint, patches of bluish-black cracked skin with small white salt crystals on his neck and jaw, a dark indigo long chieftain coat with a tiny coin-sized round coral-pink seal pin on the chest under a worn ink-black cloak, black leather gloves. Background: a foggy pine forest, painted in soft watercolor detail.
```
