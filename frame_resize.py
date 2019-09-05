import cv2
import numpy as np

def frame_resize(img, init_h, init_v, h, v, method):
    init_v, init_h = img.shape[:2]
    if method == "Resize Only":
        new_image = cv2.resize(img, (h, v))
    else:
        if method == "Resize to Width":
            scale = h / init_h
        else:
            scale = v / init_v
        img = cv2.resize(img, dsize=None, fx=scale, fy=scale)
        init_v, init_h = img.shape[:2]
        max_v = max(init_v, v)
        max_h = max(init_h, h)
        virtual = np.zeros((max_v, max_h, 3), dtype = np.uint8)
        start_v, start_h = int((max_v-init_v)/2), int((max_h-init_h)/2)
        virtual[start_v:start_v + init_v, start_h:start_h + init_h, :] = img
        start_v, start_h = int((max_v-v)/2), int((max_h-h)/2)
        new_image = virtual[start_v:start_v + v, start_h:start_h + h, :]
    return new_image
