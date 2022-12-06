from collections import Counter

tpl, _, *rules = open('input.txt').read().split('\n')
rules = dict(r.split(" -> ") for r in rules)
pairs = Counter(map(str.__add__, tpl, tpl[1:]))
chars = Counter(tpl)

print(pairs.copy().items())


for _ in range(40):
    for (a,b), c in pairs.copy().items():
        x = rules[a+b]
        pairs[a+b] -= c
        pairs[a+x] += c
        pairs[x+b] += c
        chars[x] += c

print(max(chars.values())-min(chars.values()))























# import math
# from collections import Counter



# input = [x for x in open('input.txt').read().strip().split('\n')]

# polymer = list(input[0])
# rules = input[2:]

# r = {}
# for rule in rules:
#     r[rule[0]+rule[1]]=rule[6]

# mem = {}
# size = 500


# for n in range(40):
#     print(n)
#     new = [1]

#     for i in range(0,len(polymer),size-1):
#         sub = polymer[i:i+size]
#         if len(sub) > 1:
#             substri = ''.join(sub)
#             if substri in mem:
#                 new.pop(-1)
#                 new+=mem[substri]
#             else:
#                 newsub = [sub[0]]
#                 for y in range(len(substri)-1):
#                     first = sub[y]
#                     second = sub[y+1]
#                     newsub+=r[first+second]+second
#                 mem[substri] = newsub
#                 new.pop(-1)
#                 new+=newsub

#     polymer = new

# print(Counter(polymer).most_common(1)[0][1]-Counter(polymer).most_common()[-1][1])
# print(len(polymer))






