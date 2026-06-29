import rasterio

def read_orthophoto(path):

    with rasterio.open(path) as src:

        image = src.read([1, 2, 3])

        image = image.transpose((1, 2, 0))

        return image
