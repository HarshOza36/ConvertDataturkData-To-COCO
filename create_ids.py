import os
dirr = os.listdir('pascal_voc')
dirr.remove('downloads')
with open('ids.txt', 'a') as f:
    for i in range(len(dirr)):
        f.write(dirr[i]+"\np")
