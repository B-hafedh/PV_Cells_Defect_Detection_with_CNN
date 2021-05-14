# PV_Cells_Defect_Detection_with_CNN
# Introduction

The installation of photovoltaic (PV) cells is increasing due the growing demand of generating clean energy.<br/>
But up keeping the photovoltaic modules functional, replacing defective ones is a great challenge, in fact invisible <br/>
microcracks or defects in the Si wafer, caused by dropping the PV module during installation or in production <br/>
phase, are common during process steps.The main problem is that PV module inspection is a challenging task and requires trained experts.

# Objective

In this project, we propose an automated classification strategy using CNN based methods.<br/>
We subdivide each PV module into its solar cells, and analyze each cell individually focusing on two different types of defects:<br/>

**1. Microcracks** : While microcracks do not divide the cell completely, they still must be detected because such cracks may grow <br/>
over time and eventually impair the module efficiency.<br/>

**2. Inactive regions** : these regions are usually caused by mechanical damage,and well known to reduce the cell performance.<br/>

# Dependencies 
- _python 3.7_
- _tensorflow 2.x_ ( it includes Keras )
- _pandas_ 
- _shutil_
- _split-folders_
- _matplotlib_

# Dataset
![image](https://user-images.githubusercontent.com/84082577/118333119-13ffe980-b503-11eb-953e-2d1484307be8.png)


The dataset contains 2,624 samples of 300x300 grayscale images of functional and defective solar cells<br/>
extracted from high resolution EL images of mono-crystalline and multicrystalline PV modules.<br/>
All images are normalized with respect to size and perspective, stored in the `/Data/Original_Data` directory<br/>
and the corresponding labels in `/Data/labels.csv`.

# Code Structure

**1. Data preprocessing** : 
- Data split :
 


