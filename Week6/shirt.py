import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    check_command_line()
    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(image, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])

def check_command_line():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png")):
        sys.exit("Invalid input")
 
    if not (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".png")):
        sys.exit("Invalid output")
    
    if not ((sys.argv[1].lower().endswith(".jpg") and sys.argv[2].endswith(".jpg")) or (sys.argv[1].lower().endswith(".png") and sys.argv[2].endswith(".png")) or (sys.argv[1].lower().endswith(".jpeg") and sys.argv[2].endswith(".jpeg"))):
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()