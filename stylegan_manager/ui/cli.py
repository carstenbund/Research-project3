from ..models import StyleGANModel
from ..walks import LatentWalk
from ..videos import VideoGenerator


class StyleGANCLI:
    """Simple command-style interface tying together model, walks and videos."""

    def __init__(self, weights_path: str):
        self.model = StyleGANModel(weights_path)
        self.video_gen = VideoGenerator()

    def create_walk_video(self, start_latent, end_latent, steps: int, out_file: str) -> str:
        """Generate frames from a latent walk and compose them into a text 'video'."""
        walker = LatentWalk(self.model)
        latents = walker.interpolate(start_latent, end_latent, steps)
        frames = [self.model.generate(latent) for latent in latents]
        return self.video_gen.create(frames, out_file)
