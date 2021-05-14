#import image generator
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_path='/content/Splitted_pv_cells_data/train'
test_path='/content/Splitted_pv_cells_data/test'

datagen=ImageDataGenerator(rotation_range=3,height_shift_range=0.1,width_shift_range=0.1,shear_range=0.1,zoom_range=0.1,fill_mode='nearest',horizontal_flip=True,vertical_flip=True)

# flow images batches from train_path & test path directories
train_img_gen=datagen.flow_from_directory(train_path,target_size=(300,300),color_mode='rgb',batch_size=16,class_mode='categorical')
test_img_gen=datagen.flow_from_directory(test_path,target_size=(300,300),color_mode='rgb',batch_size=16,class_mode='categorical',shuffle=False)








