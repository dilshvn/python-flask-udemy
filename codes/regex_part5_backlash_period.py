#'.' matches any character, but '\.' matches a period
#.\..\.. matches char-period-char-period-char
import re

text = 'F.B.I. I.R.S. CIA'

print(len(re.findall('.\..\..', text))) #2 -> no. of all matches
print(re.findall('.\..\..', text)) #['F.B.I', 'I.R.S']