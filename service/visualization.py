# services/visualization.py

import cv2

def draw_plants(image, plants):

    for plant in plants:

        cv2.circle(
            image,
            (plant["x"], plant["y"]),
            6,
            (255, 0, 0),
            2
        )

    return image