import cv2
import numpy as np

SAMPLE_BAND = 20
DARK_MAX = 50
INPAINT_RADIUS = 8


def inpaint(image: np.ndarray, mask: np.ndarray) -> np.ndarray:
    ys, xs = np.where(mask > 0)
    if len(ys) == 0:
        return image

    h, w = image.shape[:2]
    y0 = int(ys.min())
    x0 = int(xs.min())

    top_band = image[max(0, y0 - SAMPLE_BAND) : y0, x0:]
    left_band = image[y0:, max(0, x0 - SAMPLE_BAND) : x0]

    candidates = np.vstack(
        [
            top_band.reshape(-1, 3),
            left_band.reshape(-1, 3),
        ]
    )

    gray_c = candidates.mean(axis=1)
    dark = candidates[gray_c < DARK_MAX]

    fill = (
        np.median(dark, axis=0).astype(np.uint8)
        if len(dark) > 0
        else np.median(candidates, axis=0).astype(np.uint8)
    )

    result = image.copy()
    result[mask > 0] = fill

    result = cv2.inpaint(result, mask, INPAINT_RADIUS, cv2.INPAINT_NS)
    return result
