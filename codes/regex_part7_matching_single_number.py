#matching single number

#\d can be used for [0-9] -> between 0-9
#\D can be used for [^0-9] -> excluding 0-9

import re

text = '12345'

print(len(re.findall('\d', text))) #5 -> any number between 0-9
print(re.findall('\d', text)) #['1', '2', '3', '4', '5']
print(re.findall('\D', text)) #[] -> excluding numbers between 0-9