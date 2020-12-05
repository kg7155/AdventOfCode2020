""" Day 1: Report Repair """

with open('inputs/1.txt') as f:
    entries = list(map(int, f.readlines()))

def find():
    for i in range (0, len(entries)):
        for j in range (i+1, len(entries)):
            for k in range (j+1, len(entries)):
                e1 = entries[i]
                e2 = entries[j]
                e3 = entries[k]
                if (e1 + e2 + e3 == 2020):
                    print(e1*e2*e3)
                    return
    print("Did not find.")
            
find()

# Afterthought: After receiving the second part of the puzzle it became clear I should have used combination from the itertools module.