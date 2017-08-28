#IMPORTS

import keras
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator, img_to_array, array_to_img, load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

#

#DECLARATIONS

img_width = 320
img_height = 240
input_shape = (3,img_width,img_height)

train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
epochs = 5
batch_size = 16

# temp_img = load_img('data/train/Basketball/out147.png')
# x = img_to_array(temp_img)
# x = x.reshape(1,3,240,320)
# print(x.shape)

#

#CNN

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(3))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#

#TRAIN

train_datagen = ImageDataGenerator(
	# rotation_range=30,
 #    width_shift_range=0.25,
 #    height_shift_range=0.25,
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)



test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

model.fit_generator(
    train_generator,
    steps_per_epoch= 30,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=15,
    verbose = 1)

model.evaluate()

model.save_weights('first_try_eyemakeup_basketball_drumming.h5')