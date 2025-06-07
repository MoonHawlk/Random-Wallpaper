import random
from PIL import ImageDraw
from scipy.spatial import Delaunay, Voronoi
from .colors import random_color


def draw_triangles(draw: ImageDraw.Draw, pts, **_):
    """Filled Delaunay triangles."""
    tri = Delaunay(pts)
    for simp in tri.simplices:
        poly = [tuple(pts[i]) for i in simp]
        draw.polygon(poly, fill=random_color())


def draw_wireframe(draw: ImageDraw.Draw, pts, **_):
    """Triangle wireframe mesh."""
    tri = Delaunay(pts)
    for simp in tri.simplices:
        path = [tuple(pts[i]) for i in simp] + [tuple(pts[simp[0]])]
        draw.line(path, fill=random_color(), width=1)


def draw_voronoi(draw: ImageDraw.Draw, pts, width, height, **_):
    """Voronoi ridge lines clipped to canvas."""
    vor = Voronoi(pts)
    for v0, v1 in vor.ridge_vertices:
        if v0 < 0 or v1 < 0:
            continue
        p0, p1 = vor.vertices[v0], vor.vertices[v1]
        if (0 <= p0[0] <= width and 0 <= p0[1] <= height and
            0 <= p1[0] <= width and 0 <= p1[1] <= height):
            draw.line([tuple(p0), tuple(p1)], fill=random_color(), width=1)


def draw_circles(draw: ImageDraw.Draw, pts, **_):
    """Random circles around each seed point."""
    W, H = draw.im.size
    for x, y in pts:
        r = random.randint(10, min(W, H) // 10)
        bbox = (x - r, y - r, x + r, y + r)
        draw.ellipse(bbox, outline=random_color(), width=2)


def draw_rectangles(draw: ImageDraw.Draw, pts, **_):
    """Random rectangles around each seed point."""
    W, H = draw.im.size
    for x, y in pts:
        w = random.randint(20, W // 8)
        h = random.randint(20, H // 8)
        bbox = (x - w/2, y - h/2, x + w/2, y + h/2)
        draw.rectangle(bbox, outline=random_color(), width=2)


def draw_trapezoids(draw: ImageDraw.Draw, pts, **_):
    """Random trapezoids centered at each seed point."""
    W, H = draw.im.size
    for x, y in pts:
        top = random.randint(20, W // 6)
        bot = random.randint(20, W // 6)
        hgt = random.randint(20, H // 6)
        p1 = (x - top/2, y - hgt/2)
        p2 = (x + top/2, y - hgt/2)
        p3 = (x + bot/2, y + hgt/2)
        p4 = (x - bot/2, y + hgt/2)
        draw.polygon([p1, p2, p3, p4], outline=random_color(), width=2)


def draw_random(draw: ImageDraw.Draw, pts, width, height, **_):
    """Apply a random mix of 2–all available drawers in sequence."""
    all_funcs = [
        draw_triangles, draw_wireframe, draw_voronoi,
        draw_circles, draw_rectangles, draw_trapezoids
    ]
    k = random.randint(2, len(all_funcs))
    for fn in random.sample(all_funcs, k):
        fn(draw, pts, width=width, height=height)