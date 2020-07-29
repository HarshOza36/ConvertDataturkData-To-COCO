##from fastai.vision import Path
##from fastai.vision.data import get_annotations
from fastai import *
from fastai.vision import *
PATH = Path('../')
print(PATH.ls())
fnames = get_image_files(PATH/'pascal'/'downloads')
print(fnames[:3])
IMG_PATH = fnames
images, lbl_bbox = get_annotations(PATH/'mainTrain.json')

# print(images)
# with open("images.txt","w") as f:
#     f.write(str(images))
#     f.close()
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