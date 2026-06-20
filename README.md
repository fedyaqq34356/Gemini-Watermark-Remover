# ✦ Gemini Watermark Remover

Automatically detects and removes the **✦ sparkle watermark** placed by Google Gemini in the bottom-right corner of AI-generated images.

No neural networks. No cloud APIs. Just OpenCV — fast, offline, free.

---

## Before & After

| Before | After |
|--------|-------|
| ![Before](image/Gemini_Generated_Image_ftw3i0ftw3i0ftw3.png) | ![After](new_image/Gemini_Generated_Image_ftw3i0ftw3i0ftw3.png) |

> The ✦ symbol in the bottom-right corner is detected and cleanly removed.

---

## How It Works

```
image/          →     detector.py     →     remover.py     →     new_image/
original files        finds corner          fills with             clean output
                       mask (8×10%)         dark median
                                            + cv2 inpaint
```

**detector.py** — masks the bottom-right corner of the image (10% height × 8% width). Skips the image if the corner is already uniformly dark (no watermark present).

**remover.py** — samples dark pixels from the band directly above and to the left of the corner. Fills the masked region with their median color, then smooths with `cv2.INPAINT_NS`.

**logger.py** — progress goes to stdout (terminal), errors go to `logs/errors.log` only.

---

## Project Structure

```
.
├── main.py          # entry point — walks image/, saves to new_image/
├── detector.py      # finds the watermark region
├── remover.py       # removes it
├── logger.py        # logging setup
├── requirements.txt
├── .gitignore
├── image/           # put your input images here
└── new_image/       # cleaned images appear here
```

---

## Installation

```bash
git clone https://github.com/yourname/watermark-remover
cd watermark-remover
pip install -r requirements.txt
```

**Requirements:** Python 3.10+, works on Linux / macOS / Windows.

---

## Usage

1. Drop your Gemini images into the `image/` folder
2. Run:

```bash
python main.py
```

3. Pick up clean images from `new_image/`

**Supported formats:** `.jpg` `.jpeg` `.png` `.webp` `.bmp` `.tiff`

**Terminal output:**

```
found 3 image(s)
  done  photo_001.png
  done  photo_002.png
  skip  photo_003.png (no watermark found)
done.
```

Errors are silently written to `logs/errors.log` — the terminal stays clean.

---

## Configuration

All tunable constants live at the top of each module — no config files, no flags.

| File | Constant | Default | Description |
|------|----------|---------|-------------|
| `detector.py` | `CORNER_H` | `0.10` | corner height as fraction of image |
| `detector.py` | `CORNER_W` | `0.08` | corner width as fraction of image |
| `remover.py` | `SAMPLE_BAND` | `20` | px band to sample fill color from |
| `remover.py` | `DARK_MAX` | `50` | max brightness to consider "dark" |
| `remover.py` | `INPAINT_RADIUS` | `8` | cv2 inpaint neighborhood radius |

---

## Limitations

- Targets the **✦ Gemini sparkle** only — not other watermark types
- Assumes the watermark is always in the **bottom-right corner**
- Fill quality depends on how dark/uniform the surrounding area is

---

## License

This project is licensed under the **GNU General Public License v3.0**.
You are free to use, modify, and distribute this software, provided that any derivative work is also distributed under the same GPL-3.0 license. See [LICENSE](LICENSE) for full terms.

---

<div align="center">

Made with love ❤️ — **Fedya**

*If you liked this repo — leave a star ⭐*

</div>
