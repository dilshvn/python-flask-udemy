"""
rules,
1-20 lowercase and uppercase letters, numbers, plus ._%+-
@ symbol
2-20 lowercase and uppercase letters, numbers, plus .-
period
2-3 lowercase and uppercase letters
"""

import re

emails = 'db@aol.com m@.com @apple.com db@.com'

print(re.findall('[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}', emails)) #['db@aol.com']
