from collections import Counter
l = list(map(int,open('input.txt').read().strip().split(',')))
counts = Counter(ages)

for i in range(3):

    for x,y in counts.values():
        print(x)
print(counts)
print(sum(counts.values()))
