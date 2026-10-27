const NEG="photorealistic, 3d render, cgi, glossy, plastic skin, text, letters, watermark, logo, signature, blurry, deformed hands, extra fingers, extra limbs, duplicate face, cropped feet";
const ST="Hand-drawn 2D animation style of a classic Japanese fantasy animated feature film from the early 2000s: clean thin warm-brown ink outlines, flat cel-shaded colors with one soft shadow tone, softly painted gouache and watercolor textures, muted dusty earthy palette, gentle warm natural light, nostalgic storybook atmosphere, simple readable silhouette, slightly imperfect hand-drawn charm, original character design.";
const BG="Plain warm off-white paper background, clean design sheet layout without any lettering or captions.";
const B={
"james": "James, a gentle father in his early forties with the clearly adult face of a forty-year-old man, not a young man: a long face with high cheekbones, faint lines on his forehead and around his eyes and mouth, slightly tired kind eyes, clean-shaven, very tall and lanky with slightly stooped shoulders, messy unruly brown hair with three stray strands sticking out at the top like little cowlicks, a slate-blue knit cardigan with small silver buttons over a cream shirt with elbow patches, sleeves rolled up, worn brown trousers with small pruning shears in the pocket, muddy brown rubber boots, a thin silver watch chain. Signature design point: a very tall thin straight build with long limbs, a kind adult face with laugh lines, and three stray strands of hair sticking out from his messy brown hair"
};
const T=[
"Expression sheet: six head-and-shoulders portraits of the same character arranged in a neat grid of two rows and three columns, each showing a different emotion: warm smile with crinkled eye lines; sheepish laugh while scratching the back of his head after a clumsy mistake; patiently waiting with a calm gentle gaze; worried with raised eyebrows; telling a gentle joke with one eyebrow up and a playful grin; quiet sadness with downcast eyes and a faint smile. Same hairstyle, outfit and accessories in every portrait. Every portrait is cropped at the chest, so no legs, boots or full-body figures appear anywhere on the sheet. §B{james}. §G §S"
];
const H=["bd25d449"];
const fnv = s => { let h = 0x811c9dc5; for (const x of new TextEncoder().encode(s)) { h ^= x; h = Math.imul(h, 0x01000193) >>> 0; } return h.toString(16); };
const X = T.map(t => t.split('§S').join(ST).split('§G').join(BG).replace(/§B\{(\w+)\}/g, (_, k) => B[k]));
const bad = X.map((x, i) => fnv(x) === H[i] ? null : i).filter(i => i !== null);
if (bad.length) throw new Error('prompt mismatch: ' + bad.join(','));
const jobs=[{"prefix": "niki_compass/04_james/r3/james_3_s12403", "w": 1536, "h": 1024, "seed": 12403, "t": 0}, {"prefix": "niki_compass/04_james/r3/james_3_s13403", "w": 1536, "h": 1024, "seed": 13403, "t": 0}, {"prefix": "niki_compass/04_james/r3/james_3_s14403", "w": 1536, "h": 1024, "seed": 14403, "t": 0}, {"prefix": "niki_compass/04_james/r3/james_3_s15403", "w": 1536, "h": 1024, "seed": 15403, "t": 0}].map(j => ({...j, text: X[j.t], negative: NEG}));
const r = await mgsZ.submit(jobs);
window.mgsLast = r;
r.map(x => `${x.status} #${x.number} ${x.prefix.split('/').slice(-3).join('/')} ${x.err ? JSON.stringify(x.err) : ''}`)
