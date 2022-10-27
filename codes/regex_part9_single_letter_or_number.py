#matching any single letter or num

#\w is for [a-zA-Z0-9_] any char between a-z, A-Z, 0-9 and _
#\W is for [^a-zA-Z0-9_] excluding any char between a-z, A-Z, 0-9 and _

import re

text = '412-555-1212'
if re.search('\w{3}-\w{3}-\w{4}', text):
    print('phone number') #phone number

text = 'Superman'
if re.search('\w{2,20}', text):
    print('name with 2 to 20 characters') #name with 2 to 20 characters


