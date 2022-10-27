#matching one or more characters

import re

#+ matches one or more characters
print(re.findall('a+', 'a as ape bug')) #['a', 'a', 'a']

