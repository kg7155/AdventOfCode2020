""" Day 7: Handy Haversacks """

def construct_dict(rules):
    bags_dict = {}
    for rule in rules:
        if ('no other' in rule):
            continue
        bags = rule.strip().replace('contain', '').split('bag')
        bags[:] = [x.replace('s ','').replace('s,', '').replace(',','').strip() for x in bags if len(x)>2]
        external_bag = bags[0]
        internal_bags = []
        for bag in bags[1:]:
            n = int(bag[0])
            colour = bag[2:]
            internal_bags.append((colour, n))
        bags_dict[external_bag] = internal_bags
    return bags_dict

with open('inputs/7.txt') as f:
    rules = f.readlines()

bags_dict = construct_dict(rules)

external_bags = ['shiny gold']
changed = 0
while (len(bags_dict) > 0):
    for bag, vals in bags_dict.items():
        for val in vals:
            for eb in external_bags:
                if (eb == val[0]):
                    changed = 1
                    external_bags.append(bag)
                    break
    for eb in external_bags:
        if (eb in bags_dict):
            bags_dict.pop(eb)
    if (changed == 0):
        break
    changed = 0

# minus one because 'shiny gold' does not count
print(len(set(external_bags))-1)