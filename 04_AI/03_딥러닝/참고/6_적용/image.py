from PIL import Image
from numpy import asarray
# load the image
image = Image.open('opera_house.jpg')
# summarize some details about the image
print(image.format)
print(image.mode)
# show the image
image.show()
data = asarray(image)
# summarize shape
print(data.shape)
