#### Directory Separator join : current operating system
```python
import os
os.path.join('usr','test')

# result = usr\\test
```

#### Directory Separator join : select operating system style 
```python
import posixpath
posixpath.join('usr','test')  # unix style

# result = usr/test
```

#### Get working Directory
```python
import os
os.getcwd()  # get working directory

#result = C:\\dev\\python34

os.chdir('C:\\Windows\\System32') # change directory
os.getcwd()

#result = C:\\Windows\\System32
```
