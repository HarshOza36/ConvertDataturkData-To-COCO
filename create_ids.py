import os
dirr = os.listdir('pascal')
dirr.remove('downloads')
with open('ids.txt', 'a') as f:
    for i in range(len(dirr)):
        f.write(dirr[i]+"\np")
