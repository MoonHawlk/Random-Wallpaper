from PIL import Image, ImageDraw
from .points import generate_points
from .colors import parse_color
from .registry import SHAPES

def create_wallpaper(
    width: int, height: int, points: int,
    shapes: list[str], bgcolor: tuple[int,int,int],
    seed: int | None, output: str
):
    if seed is not None:
        import random; random.seed(seed)
    pts = generate_points(points, width, height, seed)
    img = Image.new("RGB", (width, height), bgcolor)
    draw = ImageDraw.Draw(img)
    for shape in shapes:
        SHAPES[shape](draw, pts, width=width, height=height)
    img.save(output)
    return img
