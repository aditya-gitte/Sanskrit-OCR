from dataclasses import dataclass
import easyocr
import PIL
from PIL import Image


def isEnglish(str):
    return str.isascii()


# function that reads the aadhar card and converts the text into list of strings (internal use only)
def getOCRListCoordinates(path):
    im = PIL.Image.open(path)

    reader = easyocr.Reader(['en','mr','hi'])
    # Bounds = reader.readtext(path, text_threshold=0.95, contrast_ths=0.35, adjust_contrast=0.05, add_margin=0.1, width_ths=0.7, decoder='beamsearch')
    Bounds = reader.readtext(path, text_threshold=0.75, contrast_ths=0.35, adjust_contrast=0.05, add_margin=0.1,
                             width_ths=0.1, decoder='beamsearch')
    finalList = []
    coordinatesList = []

    for i in range(len(Bounds)):
        finalList.append(Bounds[i][1])
        coordinatesList.append(Bounds[i][0])
    return finalList, coordinatesList


# Use this function to remove any english words from the image, this function alters the original image
def removeEnglishWordsfromImage(path, path2):
    dataList, coordinatesList = getOCRListCoordinates(path)

    # print(dataList)
    # print("\n")
    # print(coordinatesList)
    image = Image.open(path)
    pixels = image.load()

    for i in range(len(dataList)):
        if isEnglish(dataList[i]) == True:
            x0 = int(coordinatesList[i][0][0])
            y0 = int(coordinatesList[i][0][1])
            x1 = int(coordinatesList[i][1][0])
            y1 = int(coordinatesList[i][1][1])
            x2 = int(coordinatesList[i][2][0])
            y2 = int(coordinatesList[i][2][1])
            x3 = int(coordinatesList[i][3][0])
            y3 = int(coordinatesList[i][3][1])
            for x in range(x0, x1):
                for y in range(y0, y2):
                    pixels[x, y] = (255, 255, 255)
    # testing
    # image.show()
    image.save(path2)


#testing
removeEnglishWordsfromImage('Images/3.jpg', 'output.jpg')
