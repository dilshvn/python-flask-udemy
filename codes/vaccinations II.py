import numpy as np

vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]

vac_nums = np.array(vac_nums)

mean = np.sum(vac_nums)/20

var = np.sum((vac_nums - mean)**2)/20

print(var)