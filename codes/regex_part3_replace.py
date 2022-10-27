#replace matching items
import re

text = 'rat cat mat pat'

regex = re.compile('[cr]at') #compiling regex into pattern objects
print(regex) #prints nothing

text = regex.sub('owl', text) #replacing items in regex pattern objects
print(text) #owl owl mat pat
