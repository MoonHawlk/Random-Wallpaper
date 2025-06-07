from .drawers import (
    draw_triangles, draw_wireframe, draw_voronoi,
    draw_circles, draw_rectangles, draw_trapezoids, draw_random,
    draw_morph
)

SHAPES: dict[str, callable] = {
    'triangles':  draw_triangles,
    'wireframe':  draw_wireframe,
    'voronoi':    draw_voronoi,
    'circles':    draw_circles,
    'rectangles': draw_rectangles,
    'trapezoids': draw_trapezoids,
    'random':     draw_random,
    'morph':      draw_morph
}
