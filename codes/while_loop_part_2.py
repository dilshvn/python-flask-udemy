#another pattern using while loop
n = 11 #n has to be odd for this pattern
m = int((n + 1 )/2) #6 -> middle layer of pattern
i = 1
while i <= n:
    if i > m: #when i > 6
        b = n - i #b -> no. of blanks
        s = 2*(i - m) + 1 #s -> no. of stars
    else: #when i <= 6
        b = i - 1
        s = 2*(m - i) + 1
    j = 1
    while j <= b:
        print(' ', end = '')
        j += 1
    j = 1
    while j <= s:
        print('*', end = '')
        j += 1
    print()
    i += 1
"""
o/p:
***********
 *********
  *******
   *****
    ***
     *
    ***
   *****
  *******
 *********
***********
"""
