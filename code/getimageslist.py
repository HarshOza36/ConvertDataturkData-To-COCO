# Importing Libraries

##from fastai.vision import Path
##from fastai.vision.data import get_annotations

from fastai import *
from fastai.imports import *
from fastai.vision import *
from fastai.vision.all import *
from pathlib import Path
from tqdm import tqdm
import os

# Creating uselessDownloads folder if not already in system
if(not os.path.isdir('pascal/uselessDownloads')):
    os.mkdir('pascal/uselessDownloads')

# Creating Path variable for fastai
PATH = Path('../')
print(PATH.ls())

# Image filenames variable
fnames = get_image_files(PATH/'pascal'/'downloads')
print(fnames[:3])
IMG_PATH = fnames

# Main images accepted by fastai get_annotations function 
images, lbl_bbox = get_annotations(PATH/'mainTrain.json')

# print(images)
# with open("images.txt","w") as f:
#     f.write(str(images))
#     f.close()


# Procedure to remove the unwanted images from fastai folder to some random folder called "uselessDownloads"
l = images
dirr = os.listdir('pascal/downloads')
newlist = []
for i in range(len(dirr)):
    if(dirr[i] not in l):
        newlist.append(dirr[i])
print(len(newlist))
path = 'pascal\\downloads\\'
for i in tqdm(newlist):
    os.rename(path+i, 'pascal\\uselessDownloads\\'+i)
print(len(l))
