#matching whitespace

import re

text = '''this is a long
string that goes on
for many lines'''

regex = re.compile('\n') #compiles matching patterns of new lines -> to remove new lines
text = regex.sub(' ', text) #replace new lines with spaces
print(text) #this is a long string that goes on for many lines

'''
similary, we can match;
\b for backspace
\f for form feed
\r for carriage return
\t for tab
\v for vertical tab
'''

#you may need to remove \r\n on windows