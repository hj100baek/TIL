## Python filewrite

```python
def fwrite1GBtxt(argSavePath, argFileName):
    savePath = argSavePath
    filename = argFileName
    GB = 1024*1024*1024 # 1GB
    completeName = os.path.join(savePath, filename+".txt")
    fout = open(completeName, 'wb')
    fout.write(os.urandom(GB))

    print("Complete :" + completeName)

def fwriteSeekGBtxt(argSavePath, argFileName, argSizeType='1GB'):
    savePath = argSavePath
    filename = argFileName
    GB = 1024*1024*1024 # 1GB
    completeName = os.path.join(savePath, filename+".txt")
    fout = open(completeName, 'wb')
    if(argSizeType == '10GB'):
        fout.seek((GB * 10) - 1)
    else:
        fout.seek(GB - 1)
    fout.write(b'\0')

    print("Complete :" + completeName)


for i in range(1, 10):
   fwrite1GBtxt('D:/temps/','largeFile'+str(i))
   
for i in range(10, 15):
   fwriteSeekGBtxt('D:/temps/','largeFile'+str(i), '10GB')
   
for i in range(15, 21):
   fwriteSeekGBtxt('D:/temps/','largeFile'+str(i), '1GB')
   
```
