"""Write the alien's one-star Earth review to /output/entry.txt.

Reads the output directory from MAKEFUN_OUTPUT_DIR when set, else /output.
"""

from pathlib import Path
import os

LINE = "One star: locals queue for hours to stare at glowing rectangles, the weather changes its mind mid-sentence, gravity is frankly excessive — but the noodles are so good I'd invade again for the broth."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
