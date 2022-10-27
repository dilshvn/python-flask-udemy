#else can be used with while
i = 1
while i < 10:
    print(i)
    i += 1
else:
    print('done')

#pattern using while loop
n = 6
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(' ', end = '')
        j += 1
    j = 1
    while j <= 2*i - 1:
        print('*', end = '')
        j += 1
    print() #prints empty line
    i += 1
"""
o/p:
     *
    ***
   *****
  *******
 *********
***********
"""