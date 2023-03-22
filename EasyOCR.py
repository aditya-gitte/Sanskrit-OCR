import easyocr
import cv2
import PIL
from PIL import ImageDraw


def getOCRListCoordinates(path):
    im = PIL.Image.open(path)

    reader = easyocr.Reader(['hi', 'mr'])


    Bounds = reader.readtext(path, text_threshold=0.5, contrast_ths=0.35, adjust_contrast=0.05, add_margin=0.1,
                             width_ths=1.5, decoder='wordbeamsearch')
    finalList = []

    # coordinateslist contains the coordinates in the format that is required for the assignment
    coordinatesList = []

    # clist contains the coordinates in a more universally accepted format, used to drawing bounding boxes for testing
    clist = []

    for i in range(len(Bounds)):
        finalList.append(Bounds[i][1])
        coordinatesList.append(Bounds[i][0])

    for i in coordinatesList:
        x1 = i[0][0]
        x2 = i[1][0]
        y1 = i[0][1]
        y2 = i[2][1]
        temp_list = []
        temp_list.append(int(x1))
        temp_list.append(int(y1))
        temp_list.append(int(x2))
        temp_list.append(int(y2))
        clist.append(temp_list)


    #Debugging
    # for i in clist:
    #     print(i)

    return clist





def draw_boxes(list_of_coordinates, img_path):
    img = cv2.imread(img_path)
    for i in list_of_coordinates:
        start_point = (i[0], i[1])
        end_point = (i[2], i[3])
        cv2.rectangle(img, start_point, end_point, color=(0, 255, 0), thickness=2)
    cv2.imwrite("output.jpg",img)


# testing
list = getOCRListCoordinates('Images/3.jpg')
draw_boxes(list, 'Images/3.jpg')

