from typing import Iterable, List


class LatentWalk:
    """Utility for interpolating between latent vectors."""

    def __init__(self, model):
        self.model = model

    def interpolate(self, start: List[float], end: List[float], steps: int) -> Iterable[List[float]]:
        """Yield latent vectors interpolated from start to end."""
        if steps < 2:
            raise ValueError("steps must be at least 2")
        for i in range(steps):
            t = i / (steps - 1)
            yield [(1 - t) * s + t * e for s, e in zip(start, end)]
