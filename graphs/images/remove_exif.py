import os
import sys
from PIL import Image

# Script removes metadata from most common image types
# Use the following command in a command line: "python remove_exif.py path\to\images"

def remove_metadata(image_path):
    image = Image.open(image_path)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save(image_path)

def process_directory(dir_path):
    for filename in os.listdir(dir_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            remove_metadata(os.path.join(dir_path, filename))

if __name__ == "__main__":
    process_directory(sys.argv[1])