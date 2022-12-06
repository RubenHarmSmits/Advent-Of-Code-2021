import math

lines = [x for x in open('input.txt').read().strip().split('\n')]

def score(line):
    opened = []
    for char in line:
        if char == '{':
            opened.append('{')
        if char == '<':
            opened.append('<')
        if char == '[':
            opened.append('[')
        if char == '(':
            opened.append('(')
        if char == '}':
            last = opened.pop(-1)
            if last != '{':
                return False
        if char == ']':
            last = opened.pop(-1)
            if last != '[':
                return False
        if char == ')':
            last = opened.pop(-1)
            if last != '(':
                return False
        if char == '>':
            last = opened.pop(-1)
            if last != '<':
                return False

    return True


incomplete = list(filter(score,lines))

def calcScore(line):
    opened = []
    for char in line:
        if char in '{<([':
            opened.append(char)
        else:
            opened.pop(-1)
    score = 0
    for char in reversed(opened):
        if char == '[':
            score = score * 5 + 2
        if char == '(':
            score = score * 5 + 1
        if char == '{':
            score = score * 5 + 3
        if char == '<':
            score = score * 5 + 4
    return score


scores = [calcScore(line) for line in incomplete]

scores.sort()

print(scores[int((len(scores)-1)/2)])

