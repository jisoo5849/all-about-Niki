"""메인 ComfyUI 페이지에 올릴 데이터 파일(tools/data_v3.js)을 만든다.

페이지는 이 데이터로 build_v3.py 와 같은 프롬프트를 조립하고, 컷마다 해시로 파이썬 쪽 문장과 같은지 확인한다.

  python emit_js.py   ->  tools/data_v3.js
"""
import json
import sys
from pathlib import Path

OUT = Path(__file__).parent
sys.path.insert(0, str(OUT))
import build_v3 as b  # noqa: E402


def fnv(s: str) -> str:
    h = 0x811C9DC5
    for x in s.encode("utf-8"):
        h = ((h ^ x) * 0x01000193) & 0xFFFFFFFF
    return format(h, "x")


def main():
    data = {
        "STYLE": b.STYLE, "PLAIN": b.PLAIN, "NEGATIVE": b.NEGATIVE,
        "FRAME": {k: [v[0], v[1][0], v[1][1]] for k, v in b.FRAME.items()}, "VIEW": b.VIEW,
        "MATRIX": [list(m) for m in b.MATRIX], "ORDER": b.ORDER,
        "CHAR": b.CHAR, "H": {s["id"]: fnv(s["text"]) for s in b.shots()},
    }
    js = "window.V3 = " + json.dumps(data, ensure_ascii=False) + ";\n" + COMPOSE
    (OUT / "tools").mkdir(exist_ok=True)
    (OUT / "tools" / "data_v3.js").write_text(js, encoding="utf-8", newline="\n")
    print(len(js), "bytes -> tools/data_v3.js")


# build_v3.shots() 를 그대로 옮긴 조립 함수
COMPOSE = r"""
V3.fnv = s => { let h = 0x811c9dc5; for (const x of new TextEncoder().encode(s)) { h ^= x; h = Math.imul(h, 0x01000193) >>> 0; } return h.toString(16); };
V3.shots = () => {
  const out = [];
  V3.ORDER.forEach((char, i) => V3.MATRIX.forEach(([frame, view, bg, what], k) => {
    const row = k + 1, ck = char !== 'quillins' ? char : (frame === 'full' ? 'quillins_hood' : 'quillins_reveal'), c = V3.CHAR[ck];
    const content = what === 'stand' ? c.stand : what === 'calm' ? c.calm : what[0] === 'pose' ? c.pose[what[1]] : c.expr[what[1]];
    const back = bg === null ? V3.PLAIN : `Background: ${c.scene[bg]}, painted in soft watercolor detail.`;
    const desc = [c.head, c.upper].concat(frame === 'full' && c.lower ? [c.lower] : []).join(', ');
    const [head, w, h] = V3.FRAME[frame];
    const id = `${char}_${String(row).padStart(2, '0')}`;
    const text = `${head}, ${V3.VIEW[view]}, ${content}. ${desc}. ${back} ${V3.STYLE}`;
    out.push({ id, char, dir: `${String(i + 1).padStart(2, '0')}_${char}`, row, w, h, seed: c.seed + row, text, negative: V3.NEGATIVE, ok: V3.fnv(text) === V3.H[id] });
  }));
  return out;
};
"""

if __name__ == "__main__":
    main()
