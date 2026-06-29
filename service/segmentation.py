import cv2
import numpy as np
from skimage import measure

def vegetation_mask(image):
    # Split image into Red, Green, Blue channels
    b, g, r = cv2.split(image)

    # Convert to float
    r = r.astype(np.float32)
    g = g.astype(np.float32)
    b = b.astype(np.float32)

    # Calculate Excess Green
    exg = (2 * g) - r - b

    # Threshold
    _, mask = cv2.threshold(exg, 0, 255, cv2.THRESH_BINARY)

    # Remove noise
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    return mask.astype(np.uint8)

def count_plants(image):
    """
    Takes an image, creates vegetation mask, counts distinct plant blobs
    """
    mask = vegetation_mask(image)
    
    # Label connected components in the mask
    labels = measure.label(mask, connectivity=2)
    
    # Count unique labels, subtract 1 for background
    plant_count = len(np.unique(labels)) - 1
    
    return plant_count