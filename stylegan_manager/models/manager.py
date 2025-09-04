class StyleGANModel:
    """Simple placeholder representing a StyleGAN model."""

    def __init__(self, weights_path: str):
        self.weights_path = weights_path

    def generate(self, latent):
        """Generate an image from a latent vector.

        For this placeholder implementation, return a string
        describing the latent vector used.
        """
        return f"image_from_{latent}"
