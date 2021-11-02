from PIL import Image
from numpy import asarray

def yes_or_no(question):
    answer = input(question + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False

img = Image.open("test.jpg")

image_size = input("Enter max dimension for larger side (px): ")

algo_name = input("Input brightness algorithm name (luminosity, max_min, or average): ")

invert = yes_or_no("Invert brightness? ")

imgarray = asarray(img)
resize_factor = max(imgarray.shape[0], imgarray.shape[1])/int(image_size)
img2 = img.resize((int(imgarray.shape[1]/resize_factor), int(imgarray.shape[0]/resize_factor)))

img2 = img2.convert("RGB")
img2.save("resized.jpg")

imgarray = asarray(img2)

brightarr = [[0]*imgarray.shape[1]]*imgarray.shape[0]
#print(imgarray)

asciichars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"[::-1]
asciichars2 = ""
scale = int(255 / len(asciichars)) + 1
for c in asciichars:
    asciichars2 += scale*c
asciichars = asciichars2
for x in range(0, imgarray.shape[0]):
    for y in range(0, imgarray.shape[1]):
        if algo_name == 'average':
            brightarr[x][y] = (imgarray[x][y][0] + imgarray[x][y][1] + imgarray[x][y][2]) / 3.0
            #print(brightarr[x][y], end=" ")
        elif algo_name == 'max_min':
            brightarr[x][y] = (max(imgarray[x][y]) + min(imgarray[x][y])) / 2.0
        elif algo_name == 'luminosity':
            brightarr[x][y] = 0.21*imgarray[x][y][0] + 0.72*imgarray[x][y][1] + 0.07*imgarray[x][y][2]
        else:
            raise Exception("Unrecognized algo_name: %s" % algo_name)
        if (not invert):
            brightarr[x][y] = 255 - brightarr[x][y]
        
        chartype = int(brightarr[x][y])
        print(3*asciichars[chartype], end='')
        #brightarr[x][y] = (imgarray[x][y][0]*0.21 + imgarray[x][y][1]*0.72 + imgarray[x][y][2]*0.07)
    print()
#   print(brightarr)
#print(len(asciichars))

#print(len(asciichars))
#for x in range(0, imgarray.shape[0]):
    #for y in range(0, imgarray.shape[1]):
        #brightarr[x][y] = int( brightarr[x][y] * (len(asciichars))/ 255 - 1)
        #print(brightarr[x][y])
#print(brightarr)
'''for x in range(0, imgarray.shape[0]):
    for y in range(0, imgarray.shape[1]):
        #print(str(x) + " " + str(y), end="")
        chartype = int(brightarr[x][y])
        print(3*asciichars[chartype], end ="")
    print()'''



