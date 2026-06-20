from pathlib import Path

import cv2

from detector import detect
from logger import progress, setup_logger
from remover import inpaint

INPUT_DIR = Path("image")
OUTPUT_DIR = Path("new_image")
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}

log = setup_logger("main")


def process(path: Path):
    image = cv2.imread(str(path))
    if image is None:
        raise ValueError(f"Cannot read: {path}")

    mask = detect(image)
    if mask is None:
        progress(f"  skip  {path.name} (no watermark found)")
        return

    result = inpaint(image, mask)

    out_path = OUTPUT_DIR / path.name
    cv2.imwrite(str(out_path), result)
    progress(f"  done  {path.name}")


def main():
    if not INPUT_DIR.exists():
        progress(f"error: '{INPUT_DIR}' not found")
        raise SystemExit(1)

    OUTPUT_DIR.mkdir(exist_ok=True)

    files = [f for f in INPUT_DIR.iterdir() if f.suffix.lower() in EXTENSIONS]

    if not files:
        progress("error: no images in 'image/'")
        raise SystemExit(1)

    progress(f"found {len(files)} image(s)")

    for path in sorted(files):
        try:
            process(path)
        except Exception as e:
            log.error(e, exc_info=True)
            progress(f"  fail  {path.name} (see logs/errors.log)")

    progress("done.")


if __name__ == "__main__":
    main()
