```python

#! python3
#  before starting to work: pip install pyperclip

import pyperclip, re

# Create phone regex.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # area code
    (\s|-|\.)?              # separator
    (\d{3})                 # first 3 digits
    (\s|-|\.)               # separator
    (\d{4})                 # liast 4 digits
    )''', re.VERBOSE)


# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)


# Create id regex !!!!!!!!
idRegex = re.compile(r'''(
    id=\"([a-zA-Z0-9._%+-]+)\"       #id="xxx"
    )''', re.VERBOSE)

# Create camel regex
camelRegex = re.compile(r'''(
    ([a-zA-Z0-9]+)      
    ([A-Z][a-z0-9]+)      
    )''', re.VERBOSE)


# Create underbar regex
underRegex = re.compile(r'''(
    ([a-zA-Z0-9]+)       
    (_)                    
    ([a-zA-Z0-9]+)         
    )''', re.VERBOSE)

# Convert underbar   CamelCase -> camel_case
def convertUnderbar(word):
    s1 = re.sub('([a-zA-Z0-9])([A-Z][a-z]+)', r'\1_\2', word)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def convertUnderbar2(word):
    tepms=word
    for groups in camelRegex.findall(word):
        tepms=groups[1].lower() +'_'+groups[2].lower()
    return tepms

# Convert camel   camel_case -> camelCase
def convertCamel(word):
    tepms=word
    for groups in underRegex.findall(word):
        tepms=groups[1].lower() + groups[3].capitalize()
    return tepms

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []

for groups in idRegex.findall(text):
    matches.append(convertUnderbar2(groups[0])+'\t\t\t\t\t\t'+groups[0])
    

# Copy results to the clipboard.
if len(matches) > 0 :
    pyperclip.copy('\n'.join(matches))
    pyperclip.paste()
    #print('Copied to clipboard:')
    #print('\n'.join(matches))
else:
    print('Not found.')
    


```
