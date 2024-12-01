from  PIL import Image

image = Image.open("Battlefield-2042.jpg")
box = (0, 0, 256, 256)
region = image.crop(box)
r, g, b = region.split()
region = Image.merge("RGB", (g, b, r))
region.paste(region,box)

box = (0, 256, 256, 512)
region = image.crop(box)
region = region.rotate(117)
r, g, b = region.split()
region = Image.merge("RGB", (b, r, g))
image.paste(region, box)

image.show()
image.save("Battlefield-228.jpg")