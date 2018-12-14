#bigfile_split.py
##### 파일을 특정 문자열기준으로 분리하고 

```python
#NUM_OF_LINES=40000
SPLIT_LINES_STRING = 'commit;'        #파일 분리기준
FILE_ID = 0
filename = 'bigfile_import.sql'
with open(filename) as fin:
    #fout = open("bigfile_0.txt","wb")
    fout = open("bigfile_0.sql","w")     #encoding='utf8'
    for i,line in enumerate(fin):
      fout.write(line)
      if line.strip() == SPLIT_LINES_STRING:
        fout.close()
        FILE_ID = FILE_ID + 1
        fout = open("bigfile_%d.sql"%(FILE_ID),"w")

    fout.close()
```
