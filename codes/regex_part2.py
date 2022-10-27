import re

text = 'Cat rat mat fat pat'

#[] will match one char from brackets with the rest of the text -> case sensitive
all_animals = re.findall('[crmfp]at', text) #findall finds all matchings
print(all_animals) #['rat', 'mat', 'fat', 'pat'] -> 'Cat' isn't a match ->'C' is upper case

all_animals = re.findall('[c-m]at', text) #[] finds between c to m characters
print(all_animals) #['mat', 'fat']

all_animals = re.findall('[C-M]at', text) #[] finds between C to M characters
print(all_animals) #['Cat']

all_animals = re.findall('[c-mC-M]at', text) #[] finds between c to m and C to M characters
print(all_animals) #['Cat', 'mat', 'fat']

all_animals = re.findall('[^Cr]at', text) #[] for any char except C and r
print(all_animals) #['mat', 'fat', 'pat']