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


for i in range(1, 10):
   fwrite1GBtxt('D:/temps/','largeFile'+str(i))
```
