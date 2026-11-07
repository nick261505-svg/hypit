"""Install the portable GloPick draft into this computer's local CapCut drafts.

Run while CapCut is closed. Existing drafts are never overwritten.
"""

import argparse
import json
import os
import re
import shutil
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "templates" / "glopick_60s"
DEFAULT_NAME = "GloPick 60초 템플릿"


def install(name: str, draft_root: Path) -> Path:
    if not SOURCE.is_dir():
        raise FileNotFoundError(SOURCE)
    target = draft_root / name
    if target.exists():
        raise FileExistsError(f"이미 같은 이름의 프로젝트가 있습니다: {target}")
    draft_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE / "capcut_project", target)
    media = target / "media"
    shutil.copytree(SOURCE / "assets", media)
    shutil.copy2(SOURCE / "captions.srt", media / "captions.srt")

    local_appdata = Path(os.environ.get("LOCALAPPDATA", ""))
    if not local_appdata.is_dir():
        raise RuntimeError("LOCALAPPDATA를 찾을 수 없습니다. Windows에서 실행하세요.")
    capcut_local = (local_appdata / "CapCut").as_posix()
    generic_font = Path(r"C:\Windows\Fonts\malgun.ttf").as_posix()
    font_candidates = list((local_appdata / "CapCut" / "Apps").glob("*/Resources/Font/SystemFont/en.ttf"))
    en_font = max(font_candidates, key=lambda p: p.stat().st_mtime).as_posix() if font_candidates else generic_font

    substitutions = {
        "__GLOPICK_TEMPLATE__/assets/": media.as_posix() + "/",
        "__GLOPICK_TEMPLATE__/captions.srt": (media / "captions.srt").as_posix(),
        "__CAPCUT_DRAFT_DIR__": draft_root.as_posix(),
        "__CAPCUT_LOCAL__/Apps/9.7.0.4153/Resources/Font/SystemFont/en.ttf": en_font,
        "__CAPCUT_LOCAL__": capcut_local,
    }
    for path in target.rglob("*"):
        if not path.is_file() or path.suffix in {".jpg", ".png", ".mp4"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            continue
        for old, new in substitutions.items():
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")

    meta_path = target / "draft_meta_info.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    meta["draft_name"] = name
    meta["draft_fold_path"] = target.as_posix()
    meta["draft_root_path"] = draft_root.as_posix()
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    draft_path = target / "draft_content.json"
    draft = json.loads(draft_path.read_text(encoding="utf-8"))
    referenced = []
    for group in ("videos", "stickers", "audios"):
        for item in draft.get("materials", {}).get(group, []):
            value = item.get("path")
            if value and re.match(r"^[A-Za-z]:/", value):
                referenced.append(value)
    missing = [p for p in referenced if not Path(p).is_file()]
    unresolved = [p for p in target.rglob("*.json") if "__GLOPICK_TEMPLATE__" in p.read_text(encoding="utf-8")]
    if missing or unresolved:
        raise RuntimeError(f"미디어 경로 확인 실패: missing={missing}, unresolved={unresolved}")
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", default=DEFAULT_NAME, help="새 CapCut 프로젝트 이름")
    parser.add_argument("--draft-root", type=Path, help="기본 CapCut 초안 폴더 대신 사용할 위치 (테스트용)")
    args = parser.parse_args()
    local = os.environ.get("LOCALAPPDATA", "")
    root = args.draft_root or Path(local) / "CapCut" / "User Data" / "Projects" / "com.lveditor.draft"
    print(install(args.name, root))


if __name__ == "__main__":
    main()
