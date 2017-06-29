from PIL import Image

myImage = Image.open("poster.jpeg")
imageData = myImage.getdata()
pixellist = list(imageData)

newPixelList = []

#pixel manipulation
for pixel in pixellist:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    newRed = red*2
    if newRed > 255:
        newRed = 255

    p = (newRed,green,blue)



#add pixel to new pixel list
    newPixelList.append(p)


#opening the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
##newImage.show()
newImage.save("newPhoto.jpeg","jpeg")
