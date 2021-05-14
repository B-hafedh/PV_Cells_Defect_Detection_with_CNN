import os 
import pandas as pd

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





