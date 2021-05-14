import tensorflow
from tensorflow.keras.applications import ResNet50

Resnet50_model=ResNet50(include_top=False,weights='imagenet',input_tensor=tensorflow.keras.Input(shape=(300,300,3)))

from tensorflow.keras.models import Sequential
#import ncessary top layers 
from tensorflow.keras.layers import Dense,GlobalAveragePooling2D

model=Sequential()

  

layer_names=[layer.name for layer in Resnet50_model.layers]
batch_normalization_layers=[]

for i in layer_names:
  if "_bn" in i:
    batch_normalization_layers.append(i)
    
for layer in Resnet50_model.layers:
  if layer.name in batch_normalization_layers:
   layer.trainable=True     #Unfrozen batch normalization layer
  else:
    layer.trainable=False   # freeze layers to avoid destroying any of the information they contain during future training rounds  

model.add(Resnet50_model)
model.summary()

Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
resnet50 (Functional)        (None, 10, 10, 2048)      23587712  
_________________________________________________________________
global_average_pooling2d (Gl (None, 2048)              0         
_________________________________________________________________
dense (Dense)                (None, 4096)              8392704   
_________________________________________________________________
dense_1 (Dense)              (None, 2048)              8390656   
_________________________________________________________________
dense_2 (Dense)              (None, 2)                 4098      
=================================================================
Total params: 40,375,170
Trainable params: 16,840,578
Non-trainable params: 23,534,592
_________________________________________________________________
                      
# callbacks
from tensorflow.keras.callbacks import EarlyStopping,TensorBoard
earlystop=EarlyStopping(monitor='val_loss',patience=3,mode="min")
tensorboard_callback =TensorBoard(log_dir="/content/tensor_board",histogram_freq=0,write_graph=True,update_freq="epoch",)
     
#Train the top layers
results=model.fit(train_img_gen,
                  epochs=100,
                  callbacks=[earlystop,tensorboard_callback,],
                  validation_data=test_img_gen)
                          
#model evaluation
model.evaluate(test_img_gen)
                          
#save the model
save_path='/content'
model.save(os.path.join(save_path,'resnet50_modified'))

                          
