""" Day 10: Adapter Array """
from collections import Counter  

adapters = open('inputs/10.txt','r').read().split('\n')
adapters = sorted([int(num) for num in adapters] + [0])

diff_one = 0
diff_three = 0
for i in range(1, len(adapters)):
    diff = adapters[i] - adapters[i-1]
    if (diff == 1):
        diff_one += 1
    elif (diff == 3):
        diff_three += 1
print(diff_one * diff_three)

c = Counter({0:1})  
for a in adapters:  
    c[a+1] += c[a]  
    c[a+2] += c[a]  
    c[a+3] += c[a] 
print(c[max(adapters) + 3])