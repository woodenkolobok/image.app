from PIL import Image, ImageFilter


def open_image(filename):
    return Image.app(filename)

def blur_image(filename):
    image = Image.open(filename)
    image = image.filter(ImageFilter.GaussianBlur(2))
    image.save(filename)

def unmask_image(filename):
    image = Image.open(filename)
    image = image.filter(ImageFilter.UnsharpMask())
    image.save(filename)