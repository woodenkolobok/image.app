from PIL import Image, ImageFilter

image = Image.open('Battlefield-2042.jpg')
image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
image.show()