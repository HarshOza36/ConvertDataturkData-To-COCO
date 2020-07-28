import shutil
import os
# Paste the images list that we got from fastai get_annotations function below as list l
l=['']    
dirr = os.listdir('pascal/downloads')
newlist = []
for i in range(len(dirr)):
    if(dirr[i] not in l):
        newlist.append(dirr[i])
print(len(newlist))
path = 'pascal\\downloads\\'
for i in newlist:
    os.rename(path+i, 'pascal\\untagged\\'+i)

#Remember to remove untagged folder somewhere else 
