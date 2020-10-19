# Image Processing Task 2 - Handling Images
# Phillip Simango - C17341516

# 1. Open a user-selected image;
# 2. Show this image on the screen;
# 3. Capture the user’s click on the image
# 4. Draw a 201 x 201, 5-pixel thick red square around this location
# 5. Convert the pixels within the square to YUV
# 6. Advanced Task: Don’t fall off the edge!

import cv2
import easygui


# Defining the draw function to complete tasks 4 & 5
def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        image1 = cv2.imread(A)
        h = image1.shape[0]
        w = image1.shape[1]
        YUVimage = cv2.cvtColor(image1, cv2.COLOR_BGR2YUV)
        if x < 100:
            x = 100
        if y < 100:
            y = 100
        if x > w - 100:
            x = w - 100
        if y > h - 100:
            y = h - 100

        image1[y - 100:y + 100, x - 100:x + 100] = YUVimage[y - 100:y + 100, x - 100:x + 100]
        cv2.rectangle(img=image1, pt1=(x - 100, y - 100), pt2=(x + 100, y + 100), color=(0, 0, 255), thickness=5)
        cv2.imshow("image", image1)


# 1. Open a user-selected image
A = easygui.fileopenbox(filetypes=['*.jpg'])
image1 = cv2.imread(A)
original = image1.copy()  # Making a copy of the image file we are about to annotate on

# 2. Show this image on the screen
cv2.namedWindow("Image")
cv2.imshow("Image", image1)
cv2.setMouseCallback("User Selected Image", draw)  # Using draw function
cv2.waitKey()
