from PreProcessor import removeEnglishWordsfromImage
from EasyOCR import getOCRListCoordinates
import os
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
    coordinatesList = getOCRListCoordinates(f"Images/{filename}")[1]

    # traverse through each block
    i_counter = 0
    boxes={}
    for i in coordinatesList:
        i_counter = i_counter + 1
        # Define the dictionary in the desired format

        box = {
                "top_left": [i[0][0], i[0][1]],
                "top_right": [i[1][0], i[1][1]],
                "bottom_right": [i[2][0], i[2][1]],
                "bottom_left": [i[3][0], i[3][1]]
        }

        boxes[f"box{i_counter}"] = box

    #convert dictionary to JSON
    my_json = json.dumps(boxes, default=str)

    #store the JSON
    with open(f"Output_JSON/{counter}.json", "w") as f:
        f.write(my_json)



