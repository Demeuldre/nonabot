import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras import utils as np_utils
from keras.models import load_model
import cv2
import numpy as np

def predict(img):
    image = img.copy()
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image = cv2.threshold(image, 140, 255, cv2.THRESH_BINARY)[1]
    image = cv2.resize(image, (28, 28))
    # display_image(image)
    image = image.astype('float32')
    image = image.reshape(1, 28, 28, 1)
    image /= 255

    # plt.imshow(image.reshape(28, 28), cmap='Greys')
    # plt.show()
    model = load_model('model.h5')
    pred = model.predict(image.reshape(1, 28, 28, 1), batch_size=1)
    # return pred.argmax()
    print("Predicted Number: ", pred.argmax())

    