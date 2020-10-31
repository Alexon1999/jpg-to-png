import re
import sys
from pathlib import Path
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# windowPath object
path = Path('new')

# pathlib module
if not Path(output_folder).exists():
    Path(output_folder).mkdir()
    path = Path(output_folder)


pattern = re.compile(r"(?<=[\\/])\w+")

for image_path in Path(image_folder).glob('*.jpg'):
    # images\astro.jpg
    # images\bulbasaur.jpg
    # etc
    print(image_path)  # + window path object
    img_name = pattern.search(str(image_path)).group()

    img = Image.open(image_path)
    img.save(f"{Path(output_folder, img_name)}.png")
