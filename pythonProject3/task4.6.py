from itertools import count
from itertools import cycle


for el in count(10):
    if el > 25:
        break
    else:
        print(el)


c = 0
for el in cycle("mynameisVasya"):
    if c > 25:
        break
    print(el)
    c += 1
