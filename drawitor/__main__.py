from argparse import ArgumentParser
from .core import draw

drawitor = ArgumentParser(description="Draw Images or GIFs in your terminal")

drawitor.add_argument("image", type=str, help="Image to draw")

args = drawitor.parse_args()

draw(args.image)
