#solving backlash problems

#regex use '\' to designate special characters, python does the same inside strings -> creates issues
import re

text = 'here is \\stuff'
#.search -> checks if available
print(re.search('\\stuff', text)) #None -> issue
print(re.search('\\\\stuff', text)) #found -> no issue, have to enter 4 '\'

#use raw strings (r) to make this easy
print(re.search(r'\\stuff', text)) #found -> no issue, don't need to use 4 '\'
