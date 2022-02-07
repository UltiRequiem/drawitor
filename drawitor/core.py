from PIL import Image, GifImagePlugin
import io
import os
import sys
import time

from .utils import colored, PIXEL, clear_console

image_size = tuple[int, int]


def draw_gif(source: GifImagePlugin.GifImageFile, size: image_size = None):
    try:
        while True:
            for frame in range(0, source.n_frames):
                source.seek(frame)
                draw_image(source, size)
                time.sleep(0.1)
                print(f"\033[{source.size[1]}A", end="")
    except KeyboardInterrupt:
        clear_console()
        sys.exit()


def draw_image(img: Image.Image, size: image_size = None):
    buffer = io.StringIO()
    size = size or os.get_terminal_size()

    img = img.resize(size)

    pixel_values = img.convert("RGB").getdata()

    width, _ = img.size

    cluster_pixel = pixel_values[0]

    n = 0

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


def draw(source: str | Image.Image, size: image_size = None):
    """
    Draws an image/GIF to the terminal.
    You can pass a path to an image or a PIL Image.
    """

    image = Image.open(source) if isinstance(source, str) else source

    drawer = draw_gif if isinstance(image, GifImagePlugin.GifImageFile) else draw_image

    drawer(image, size)
