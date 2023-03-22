from PreProcessor import removeEnglishWordsfromImage
from EasyOCR import getOCRListCoordinates
import os
from PIL import Image
import json

# Set the path to the folder containing the images
folder_path = "Images"

counter = 0
# Loop over each file in the folder
for filename in os.listdir(folder_path):
    if not (filename.endswith('.jpg')):
        continue
    counter = counter + 1

    # pre-process the image and store the output at the same location
    removeEnglishWordsfromImage(f"Images/{filename}", f"Images/{filename}")

    # get the coordinates of ROIs of the sanskrit detections
    clist,coordinatesList = getOCRListCoordinates(f"Images/{filename}")

    # traverse through each ROI
    i_counter = 0
    boxes={}
    for i in clist:
        i_counter = i_counter + 1
        # Define the dictionary in the desired format

        box = {
                "top_left": [i[0], i[3]],
                "top_right": [i[2], i[3]],
                "bottom_right": [i[2], i[1]],
                "bottom_left": [i[0], i[1]]
        }

        boxes[f"box{i_counter}"] = box

    #load the input image
    input_image = Image.open(f"Images/{filename}")
    # loop through each coordinate and extract the pixels
    for i, coordinates in enumerate(clist):
        # get the coordinates
        x1, y1, x2, y2 = coordinates

        # extract the pixels
        cropped_image = input_image.crop((x1, y1, x2, y2))

        # save the cropped image with a unique name
        cropped_image.save(f"Output_Images/{counter}_image_{i}.jpg")

    #convert dictionary to JSON
    my_json = json.dumps(boxes, default=str)

    #store the JSON
    with open(f"Output_JSON/{counter}.json", "w") as f:
        f.write(my_json)

    #store the indivisual ROI images



