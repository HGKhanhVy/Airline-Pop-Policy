"""Builds the planes that fly across the site's sky: each of the game's plane liveries
turned to fly right, with one of the cat regulars sitting upright in its cockpit.

The art is read from the game project, so run it from a machine that has both:

    python tools/make_planes.py [path to the AirLine-Pop project]
"""
import os
import sys

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
GAME = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "AirLine-Pop")
FLAT = os.path.join(GAME, "Assets", "_Game", "Art", "Flat")
CATS = os.path.join(GAME, "Assets", "_Game", "Art", "FlatCats")
OUT = os.path.join(HERE, "..", "assets", "img")

# Every livery's cockpit window, in its 512 px drawing.
COCKPIT = (255, 172)
WINDOW = 70

# Livery, the regular flying it.
PLANES = [
    ("airplane", "bo"),
    ("airplane_mint", "kem"),
    ("airplane_lavender", "mun"),
    ("airplane_sunny", "muop"),
    ("airplane_sky", "tro"),
]

SIZE = 256


def bust(breed, diameter):
    """The cat's head and shoulders, scaled to fill a round window of this size."""
    cat = Image.open(os.path.join(CATS, "passenger_%s_sit.png" % breed)).convert("RGBA")
    box = cat.getbbox()
    width = box[2] - box[0]
    head = cat.crop((box[0], box[1], box[2], box[1] + int(width * 0.9)))
    scale = diameter * 1.08 / head.width
    head = head.resize((int(head.width * scale), int(head.height * scale)), Image.LANCZOS)
    window = Image.new("RGBA", (diameter, diameter), (0, 0, 0, 0))
    window.alpha_composite(head, ((diameter - head.width) // 2, int(diameter * 0.12)))
    mask = Image.new("L", (diameter, diameter), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diameter - 1, diameter - 1), fill=255)
    out = Image.new("RGBA", (diameter, diameter), (0, 0, 0, 0))
    out.paste(window, (0, 0), mask)
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    for livery, breed in PLANES:
        plane = Image.open(os.path.join(FLAT, livery + ".png")).convert("RGBA")
        # The drawings point up; turned a quarter clockwise they fly to the right. The
        # window turns with the plane, but the cat is pasted afterwards so it sits upright.
        turned = plane.rotate(-90, resample=Image.BICUBIC)
        cx, cy = plane.width - COCKPIT[1], COCKPIT[0]
        diameter = WINDOW * 2
        turned.alpha_composite(bust(breed, diameter), (cx - WINDOW, cy - WINDOW))
        turned = turned.crop(turned.getbbox())
        turned.thumbnail((SIZE, SIZE), Image.LANCZOS)
        turned.save(os.path.join(OUT, "fly_%s.png" % breed))
        print("fly_%s.png" % breed)


if __name__ == "__main__":
    main()
