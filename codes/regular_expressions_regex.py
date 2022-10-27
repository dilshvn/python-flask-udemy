#regex allows to locate and change strings
import re #regex module

if re.search('ape', 'planet of the apes: apex'): #searching for 'ape' in 'planet of the apes' -> returns boolean
    print('found') #found

all_apes = re.findall('ape', 'planet of the apes: apex') #returns list of all findings
print(all_apes) #['ape', 'ape']
all_apes = re.findall('ape.', 'planet of the apes: apex') #'.' -> 1 character or space
print(all_apes) #['apes', 'apex']

text = 'planet of the apes: apex'
for i in re.finditer('ape.', text): #.finditer() returns iterator
    print(i) #returns nothing
    tup1 = i.span() #.span() returns tuple
    print(tup1) #(14, 18) and (20, 24) -> index span -> end index is exclusive
    print(text[tup1[0]:tup1[1]]) #apes and apex -> slicing values we need
