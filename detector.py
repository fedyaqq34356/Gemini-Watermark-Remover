from __future__ import annotations

import cv2
import numpy as np

CORNER_H = 0.10
CORNER_W = 0.08
SAMPLE_BAND = 15


def detect(image: np.ndarray) -> np.ndarray | None:
    h, w = image.shape[:2]
    zh = int(h * CORNER_H)
    zw = int(w * CORNER_W)

    zone_gray = cv2.cvtColor(image[h - zh : h, w - zw : w], cv2.COLOR_BGR2GRAY)

    if zone_gray.max() < 30:
        return None

    mask = np.zeros((h, w), dtype=np.uint8)
    mask[h - zh : h, w - zw : w] = 255
    return mask
