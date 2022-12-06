from collections import Counter
l = list(map(int,open('input.txt').read().strip().split(',')))

ans = []
for i in range(1000):
    fuel = 0
    for n in l:
        r = abs(n-i)
        a = (r * (r+1))/2
        fuel += a

    ans.append(fuel)
    # print(fuel, i)

print(min(ans))
