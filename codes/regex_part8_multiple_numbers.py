#matching multiple numbers

import re

text = '67891'
print(re.findall('\d{5}', text)) #['67891'] -> any 5 nums
print(re.findall('\d{4}', text)) #['6789'] -> any 4 nums, starts from left
print(re.findall('\d{6}', text)) #[] -> any 6 nums

text = '1234 123 12'
print(re.findall('\d{2,4}', text)) #['1234', '123', '12'] -> any between 2-4 (4 inclusive) nums, starts from left
print(re.findall('\d{2, 4}', text)) #[] -> don't use space for better readability


