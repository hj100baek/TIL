#### Standard Format Specifiers
[[fill]align][sign][#][0][minimumwidth][.precision][type]

```python
def competitiveEating(t, width, precision):
    return "{0:^{a}.{b}f}".format(t,a=width,b=precision)



'''
Input:
t: 3.1415
width: 10
precision: 2

Output:
"   3.14   "
'''

#'^' - align. Forces the field to be centered within the available
      space.
# '.' - precision. a decimal number indicating how many digits should be displayed after the decimal point in a floating point conversion
#f   - Fixed point. Displays the number as a fixed-point
      number.
```
