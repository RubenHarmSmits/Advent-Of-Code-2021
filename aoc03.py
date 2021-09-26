with open('input.txt') as f:
    lines = f.readlines()

def isCorrect(a):
    b = [int(numeric_string) for numeric_string in a]
    b.sort()
    if b[2] < b[1] + b[0]:
        return True
    else:
        return False

correct = 0;

mapped = []

for line in lines:
    a = list(filter(None, line.split("  ")))
    a[-1] = a[-1].strip()
    mapped.append(a)

for idx, val in enumerate(mapped):
    one = []
    two = []
    three = []
    if idx % 3 is 0:
        one.append(mapped[idx][0])
        one.append(mapped[idx+1][0])
        one.append(mapped[idx+2][0])
        two.append(mapped[idx][1])
        two.append(mapped[idx+1][1])
        two.append(mapped[idx+2][1])
        three.append(mapped[idx][2])
        three.append(mapped[idx+1][2])
        three.append(mapped[idx+2][2])
        if isCorrect(one):
            correct = correct + 1
        if isCorrect(two):
            correct = correct + 1
        if isCorrect(three):
            correct = correct + 1


print(correct)


