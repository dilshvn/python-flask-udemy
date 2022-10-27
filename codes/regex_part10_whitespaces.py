#matching whitespaces

#\s is for [\f\n\r\t\v] -> any whitespace from form feed, new line, carriage return, tab, vertical tab
#\S is for [^\f\n\r\t\v] -> any whitespace excluding form feed, new line, carriage return, tab, vertical tab

import re

if re.search('\w{2,20}\s\w{2,20}', 'Dilshan Deshapriya'): #\s for blank space
    print('valid full name') #valid full name