import os
dirr = os.listdir('pascal')
dirr.remove('downloads')
if('ids.txt' in dirr):
    dirr.remove('ids.txt')
if('labels.txt' in dirr):
    dirr.remove('labels.txt')
with open('ids.txt', 'a') as f:
    for i in range(len(dirr)):
        f.write(dirr[i]+"\n")
