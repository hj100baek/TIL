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


labelRegex = re.compile(r'''(
    name=\"([a-zA-Z]|[가-힣a-zA-Z0-9._%+-;]+)\"       #label="한글xxx"
    )''', re.VERBOSE)

# Create camel regex
camelRegex = re.compile(r'''(
    ([a-zA-Z0-9]+)      
    ([A-Z][a-z0-9]+)      
    )''', re.VERBOSE)

# Create camel regex
camelRegex2 = re.compile(r'''(
    ([a-z0-9]+)      
    ([A-Z]{1}[a-z0-9]+)
    ([A-Z]{1}[a-z0-9]+)?
    )''', re.VERBOSE)


# Create underbar regex
underRegex2 = re.compile(r'''(
    ([a-zA-Z0-9]+)       
    (_)                    
    ([a-zA-Z0-9]+)
    (_)?
    ([a-zA-Z0-9]+)?
    )''', re.VERBOSE)

# Create underbar regex
underRegex3 = re.compile(r'''(
    ([a-zA-Z0-9]+)       
    (_)                    
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

def convertUnderbar3(word):
    tepms=word
    for groups in camelRegex2.findall(word):
        tepms=groups[1].upper() +'_'+groups[2].upper()
        if(len(groups[3]) >0):
            tepms = tepms +'_'+groups[3].upper()
    return tepms


# Convert camel   camel_case -> camelCase
def convertCamel(word):
    tepms=word
    for groups in underRegex2.findall(word):
        tepms=groups[1].lower() + groups[3].capitalize()
        if(len(groups[5]) >0):
            tepms = tepms + groups[5].capitalize()
        
    return tepms

# Find matches in clipboard text.
text = str(pyperclip.paste())
text2 = text
matches = []

for groups in idRegex.findall(text):
#    #matches.append(convertUnderbar2(groups[0])+'\t\t\t\t\t\t'+groups[0])
    matches.append(groups[0])

for groups in labelRegex.findall(text):
    matches.append(groups[0])    

# caCaCa -> ca_ca_ca
for groups in camelRegex2.findall(text):
    text2=text2.replace(groups[0], convertUnderbar3(groups[0]))         #대상을 바꿀
    #matches.append(convertUnderbar3(groups[0])+'\tString\t\t')  #대상만 뽑을때
    #print(groups[0]+"=>"+ convertUnderbar3(groups[0]))

# X_X_X  _3 -> caCaCa
for groups in underRegex2.findall(text):
    text2=text2.replace(groups[0], convertCamel(groups[0]))
    #matches.append(convertCamel(groups[0])+'\tString\t\t')


def camels():
    if len(text2) > 0 :
        pyperclip.copy(text2)
        pyperclip.paste()  
    else:
        print('Not fouund clipboard data')

# Copy results to the clipboard.
def idName():
    if len(matches) > 0 :
          
        pyperclip.copy('\n'.join(matches))
        pyperclip.paste()
        #print('Copied to clipboard:')
        #print('\n'.join(matches))
    else:
        print('Not found.')


#idName()

camels()

```
