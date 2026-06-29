from skimage.measure import label
from skimage.measure import regionprops

def detect_plants(mask):

    labels = label(mask)

    plants = []

    for region in regionprops(labels):

        if region.area > 20:

            y, x = region.centroid

            plants.append(
                {
                    "x": int(x),
                    "y": int(y),
                    "area": region.area
                }
            )

    return plants