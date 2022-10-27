#practice work (pattern)
n = 11 #odd
m = int((n + 1)/2) #6
i = 1
while i <= n:
    if i <= m: #when i <= 6
        print(' '*(m - i) + '*'*(2*i - 1))
    else: #when i > 6
        print(' '*(i - m) + '*'*(11 - 2*(i - m))) #used a + (n - 1)d here
    i += 1
"""
o/p:
     *
    ***
   *****
  *******
 *********
***********
 *********
  *******
   *****
    ***
     *
"""