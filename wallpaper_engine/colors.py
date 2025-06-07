import random

def parse_color(s: str) -> tuple[int,int,int]:
    return tuple(int(x) for x in s.split(','))

def random_color() -> tuple[int,int,int]:
    return tuple(random.randint(0, 255) for _ in range(3))
