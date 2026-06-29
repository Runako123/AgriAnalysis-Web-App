# services/analytics.py

def calculate_analytics(plants, image):

    count = (plants)

    height, width = image.shape[:2]

    image_area = width * height

    density = count / image_area

    return {
        "count": count,
        "image_area": image_area,
        "density": density
    }