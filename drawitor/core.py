from PIL import Image
import io
import os

from .utils import colored, PIXEL


def draw_image(path: str):
    buffer = io.StringIO()
    img = Image.open(path)

    img = img.resize(os.get_terminal_size())

    pixel_values = img.convert("RGB").getdata()

    width, _height = img.size

    n = 0
    cluster_pixel = pixel_values[0]

    for index, pixel in enumerate(pixel_values):
        if pixel != cluster_pixel or index % width == 0:
            buffer.write(colored(*cluster_pixel, PIXEL * n))
            if index and index % width == 0:
                buffer.write("\n")
            n = 0
            cluster_pixel = pixel
        n += 1

    buffer.write(colored(*cluster_pixel, PIXEL * n) + "\033[0m")

    buffer.seek(0)

    print(buffer.getvalue())

    buffer.seek(0)
    buffer.truncate()
