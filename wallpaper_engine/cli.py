import argparse
from .api import create_wallpaper
from .colors import parse_color
from .registry import SHAPES

def main():
    p = argparse.ArgumentParser()
    p.add_argument('-W','--width',  type=int, default=1920)
    p.add_argument('-H','--height', type=int, default=1080)
    p.add_argument('-n','--points', type=int, default=200)
    p.add_argument('-S','--shapes',
                   nargs='+', choices=SHAPES.keys(),
                   default=['triangles'])
    p.add_argument('-b','--bgcolor', type=parse_color, default="0,0,0")
    p.add_argument('--seed', type=int, default=None)
    p.add_argument('-o','--output', type=str, default="wallpaper.png")
    args = p.parse_args()

    create_wallpaper(
        width=args.width,
        height=args.height,
        points=args.points,
        shapes=args.shapes,
        bgcolor=args.bgcolor,
        seed=args.seed,
        output=args.output
    )

if __name__ == "__main__":
    main()
