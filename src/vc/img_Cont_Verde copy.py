import cv2
from cv2 import imshow
import numpy as np
import os
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras import utils as np_utils
import function

# the MNIST data is split between train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

   
image  = cv2.imread('grid.PNG')
cv2.imshow("Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)
#cv2.imshow("Image", blur)

thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
#cv2.imshow("Image", thresh)


contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_area = 0
c = 0
for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
                if area > max_area:
                    max_area = area
                    best_cnt = i
                    image = cv2.drawContours(image, contours, c, (0, 255, 0), 3)
        c+=1

mask = np.zeros((gray.shape),np.uint8)
cv2.drawContours(mask,[best_cnt],0,255,-1)
cv2.drawContours(mask,[best_cnt],0,0,2)
#cv2.imshow("mask", mask)

out = np.zeros_like(gray)
out[mask == 255] = gray[mask == 255]

#cv2.imshow("Out", out)


blur = cv2.GaussianBlur(out, (5,5), 0)


thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
cv2.imshow("thresh1", thresh)




edge_h = np.shape(thresh)[0]
edge_w = np.shape(thresh)[1]
celledge_h = edge_h // 11
celledge_w = np.shape(thresh)[1] // 10

tempgrid = []
for i in range(celledge_h, edge_h + 1, celledge_h):
    for j in range(celledge_w, edge_w + 1, celledge_w):
        rows = thresh[i - celledge_h:i]
        tempgrid.append([rows[k][j - celledge_w:j] for k in range(len(rows))])

print(len(tempgrid))

# Creating the 9X9 grid of images
finalgrid = []
for i in range(0, len(tempgrid) -8, 9):
    finalgrid.append(tempgrid[i:i + 9])
# Converting all the cell images to np.array
for i in range(9):
    for j in range(9):
        finalgrid[i][j] = np.array(finalgrid[i][j])
try:
    for i in range(9):
        for j in range(9):
            os.remove("cell" + str(i) + str(j) + ".jpg")
except:
    pass
for i in range(9):
    for j in range(9):
        cv2.imwrite(str(r"C:\Users\Usuario\Desktop\PROYECTO RLP\Celdas\cell" + str(i) + str(j) + ".jpg"), finalgrid[i][j])


# ----------------------------- MODELO ---------------------------- #

# the MNIST data is split between train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Reshape to be samples*pixels*width*height
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32')

# One hot Cpde
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

# convert from integers to floats
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
# normalize to range [0, 1]
X_train = (X_train / 255.0)
X_test = (X_test / 255.0)

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(10, activation='softmax'))
# model.summary()

# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.save("model.h5")
print("Saved model to disk")

#thresh = 128  # define a threshold, 128 is the middle of black and white in grey scale
# threshold the image
#gray = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]

# Find contours
cnts  = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

"""
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)

    if (x < 3 or y < 3 or h < 3 or w < 3):
        # Note the number is always placed in the center
        # Since image is 28x28
        # the number will be in the center thus x >3 and y>3
        # Additionally any of the external lines of the sudoku will not be thicker than 3
        continue
    ROI = gray[y:y + h, x:x + w]
    cv2.imshow("O",ROI)
    cv2.waitKey(0)
    # increasing the size of the number allws for better interpreation,
    # try adjusting the number and you will see the differnce
    #ROI = scale_and_centre(ROI, 120)
  
    finalgrid[i][j] = function.predict(ROI)
"""
   
for i in range(9):
    for j in range(9):
        finalgrid[i][j] = function.predict(finalgrid[i][j])


cv2.waitKey(0)
cv2.destroyAllWindows()
