# To work with images you need to install Pillow
# pip install Pillow
# https://pillow.readthedocs.io/en/stable/
print("========================================================================")
print("1--------------------------------")
# openning an image (image object)
from PIL import Image

mac = Image.open("testImg.png")
# mac.show()
imgSize = mac.size								# returns tuple
print(imgSize)


print("\n2--------------------------------")
# cropping images

x = 1212 / 4
y = 0
w = 1212 / 2
h = 710 / 2
mac2 = mac.crop((x, y, w, h))
# mac2.show()


print("\n3--------------------------------")
# copying and pasting
# only affects image in working memory
# (original img does not change)
mac.paste(im=mac2, box=(0,0))		# paste mac2 into mac at 0,0
# mac.show()


print("\n4--------------------------------")
# stretching and squeezing, and rotating
mac2.resize((3000, 500))
# mac2.show()

mac2.rotate(45)
# mac2.show()


print("\n5--------------------------------")
# transparency - RGBA system
# alpha = 0 transparent , 255 opaque
mac2.putalpha(128)
# mac2.show()

mac.paste(im=mac2, box=(0,350), mask=mac2)
mac.show()






print("========================================================================")
