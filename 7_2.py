""" Day 7: Handy Haversacks """

def construct_dict(rules):
    bags_dict = {}
    for rule in rules:
        bags = rule.strip().replace('contain', '').split('bag')
        bags[:] = [x.replace('s ','').replace('s,', '').replace(',','').strip() for x in bags if len(x)>2]
        external_bag = bags[0]
        if ('no other' in rule):
            bags_dict[external_bag] = []
            continue
        internal_bags = []
        for bag in bags[1:]:
            n = int(bag[0])
            colour = bag[2:]
            internal_bags.append((colour, n))
        bags_dict[external_bag] = internal_bags
    return bags_dict

def count(L):
    total = 1
    for e in L:
        total += count(bags_dict[e[0]]) * e[1]
    return total

with open('inputs/7.txt') as f:
    rules = f.readlines()

bags_dict = construct_dict(rules)
print(count(bags_dict['shiny gold'])-1)