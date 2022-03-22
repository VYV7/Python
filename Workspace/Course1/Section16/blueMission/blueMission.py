# To work with images you need to install Pillow
# pip install Pillow
# https://pillow.readthedocs.io/en/stable/
print("========================================================================")
print("1--------------------------------")
# open images
from PIL import Image

img1 = Image.open("image_link.png")
img2 = Image.open("cover_image.png")


print("\n2-------------------------------")
# prepare img2 - stretch to fit img1, set transparency
img1Size = img1.size
print("img1 size: ", img1Size)

print("img2 size: ", img2.size)
img2 = img2.resize(img1Size)
print("img2 new size: ", img2.size)


img2.putalpha(64)


img1.paste(im=img2, box=(0, 0), mask=img2)
img1.show()


print("========================================================================")
