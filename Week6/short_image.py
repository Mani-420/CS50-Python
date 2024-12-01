from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("insta1.png") as img:
        # print(img.size)
        # print(img.format)
        image = img.rotate(180)
        # image.save("insta_change.png")
        image = img.filter(ImageFilter.BLUR)
        image.save("insta_blur.png")



main()