"""2차 최종본 PNG 에 들어 있는 실행 정보(프롬프트·시드·편집 지시)를 꺼내 final_v2.json 으로 정리한다.

  python extract_v2.py   (final/, sources/, manifest.json 이 있어야 함)

생성 PNG 는 Qwen-Image-2512 그래프(노드 6 긍정, 7 부정, 8 크기, 9 샘플러), 편집 PNG 는 Qwen-Image-Edit-2511 그래프
(노드 9 편집 지시, 14 샘플러)다. 편집본은 확장 프롬프트가 원본(sources/)에 있으므로 거기서 읽는다.
"""
import json
import struct
import sys
import zlib
from pathlib import Path

OUT = Path(__file__).parent
# 작업 폴더에서는 download/ 아래, 저장소에서는 이 폴더 바로 아래에 final/, sources/, manifest.json 이 있다
DL = OUT / "download" if (OUT / "download").exists() else OUT
sys.path.insert(0, str(OUT))
import build_v2  # noqa: E402

# r3 에서 확장 프롬프트 앞에 붙인 그림체 고정 머리말 (확장문 자체는 바꾸지 않았다)
ANCHOR = ("Anime screencap, a single frame from a Japanese TV anime series, cel animation with flat simple colors and "
          "minimal soft shading, thin clean black outlines, anime-style faces with large eyes, a small simple nose and "
          "smooth simplified skin. ")


def png_text(path: Path) -> dict:
    data = path.read_bytes()
    pos, out = 8, {}
    while pos < len(data):
        n, kind = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + n]
        if kind == b"tEXt":
            k, v = body.split(b"\0", 1)
            out[k.decode("latin-1")] = v.decode("utf-8", "replace")
        elif kind == b"zTXt":
            k, rest = body.split(b"\0", 1)
            out[k.decode("latin-1")] = zlib.decompress(rest[1:]).decode("utf-8", "replace")
        elif kind == b"iTXt":
            k, rest = body.split(b"\0", 1)
            flag, _method = rest[0], rest[1]
            rest = rest[2:].split(b"\0", 2)[2]
            out[k.decode("latin-1")] = (zlib.decompress(rest) if flag else rest).decode("utf-8", "replace")
        pos += 12 + n
    return out


def gen_info(path: Path) -> dict:
    p = json.loads(png_text(path)["prompt"])
    text = p["6"]["inputs"]["text"]
    body = text[len(ANCHOR):] if text.startswith(ANCHOR) else text
    if body.endswith(" " + build_v2.STYLE):
        body = body[: -len(build_v2.STYLE) - 1]
    k = p["9"]["inputs"]
    return {"file": path.name, "anchor": text.startswith(ANCHOR), "expanded": body.strip(), "prompt": text,
            "negative": p["7"]["inputs"]["text"], "seed": k["seed"], "steps": k["steps"], "cfg": k["cfg"],
            "w": p["8"]["inputs"]["width"], "h": p["8"]["inputs"]["height"],
            "lightning": "4" in p}


def edit_info(path: Path) -> dict:
    p = json.loads(png_text(path)["prompt"])
    return {"file": path.name, "text": p["9"]["inputs"]["prompt"], "seed": p["14"]["inputs"]["seed"],
            "input": p["7"]["inputs"]["image"]}


def main():
    plan = json.loads((DL / "manifest.json").read_text(encoding="utf-8"))
    by_shot = {}
    for item in plan:
        by_shot.setdefault(item["shot"], []).append(item)
    inputs = {x["id"]: x for x in build_v2.expand_inputs()}
    out = []
    for shot, items in by_shot.items():
        final = next(i for i in items if i["zip"].startswith("final/"))
        src = next((i for i in items if i["zip"].startswith("sources/")), None)
        rec = {"shot": shot, "final": final["zip"], "main_file": final["src"],
               "expand_input": {"text": inputs[shot]["text"],
                                "notes": build_v2.CHAR_OVERRIDE.get(shot.split("_")[0], inputs[shot]["notes"])
                                if shot.startswith("james") else inputs[shot]["notes"]}}
        if src:
            rec["generation"] = gen_info(DL / src["zip"])
            rec["generation"]["main_file"] = src["src"]
            rec["edit"] = edit_info(DL / final["zip"])
        else:
            rec["generation"] = gen_info(DL / final["zip"])
        out.append(rec)
    (OUT / "final_v2.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(len(out), "shots -> final_v2.json")
    for r in out:
        g = r["generation"]
        print(r["shot"], g["seed"], g["steps"], g["cfg"], g["w"], g["h"], "anchor" if g["anchor"] else "-",
              len(g["expanded"].split()), "edit" if "edit" in r else "")


if __name__ == "__main__":
    main()
