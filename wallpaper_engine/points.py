import numpy as np

def generate_points(n: int, w: int, h: int, seed: int | None = None) -> np.ndarray:
    if seed is not None:
        np.random.seed(seed)
    return np.random.rand(n, 2) * np.array([w, h])
