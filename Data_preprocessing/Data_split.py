import os 
import pandas as pd
import shutil
!pip install split-folders
import splitfolders 

#import the labels csv file 
labels_path='/content/cellsData.csv'
df=pd.read_csv(labels_path)

#split images to infected & uninfected cells according to their infection probability
infected_list=[]
uninfected_list=[]
for index, row in df.iterrows():
  if row['probability']==0:
    uninfected_list.append(row['image'][7:])
  else:
    infected_list.append(row['image'][7:])

images_path='/content/Original_Data'

#add images directories to a list
images_list=os.listdir(images_path)

#copy infected cells to infected_path
for i in range(0,len(images_list)):
  if images_list[i] in infected_list:
    file_directory=images_path+'/'+images_list[i]
    shutil.copy(file_directory,'/content/new_PV_cells_data/infected_cells')
    
  #copy uninfected cells to uninfected_path
  else :
    file_directory=images_path+'/'+images_list[i]
    shutil.copy(file_directory,'/content/new_PV_cells_data/uninfected_cells')
 
#split DATA to 75% train and 25% test
splitfolders.ratio("/content/new_PV_cells_data",output="/content/Splitted_pv_cells_data",seed=1337, ratio=(.75, .25,))#the seed makes splits reproducible.





