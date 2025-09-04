class VideoGenerator:
    """Placeholder video generator that writes frames to a text file."""

    def create(self, frames, out_file: str) -> str:
        with open(out_file, "w") as fh:
            for frame in frames:
                fh.write(str(frame) + "\n")
        return out_file
