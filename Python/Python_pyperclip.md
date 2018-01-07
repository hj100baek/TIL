
module : pip install pyperclip


```python
#! python3
# bulletPointAdder.py

import pyperclip
text = pyperclip.paste()

#Sperate line and add stars

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
```
