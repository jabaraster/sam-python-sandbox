import numpy as np

def sum_color(img):
    ret = 0
    height, width, _ = img.shape
    for y in range(0, height):
        for x in range(0, width):
            for color in range(0, 3):
                ret += img[y, x, color]
    return ret