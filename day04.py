from collections import Counter

lines = [x for x in open('input.txt').read().strip().split('\n')]

numbers = '74,79,46,2,19,27,31,90,21,83,94,77,0,29,38,72,42,23,6,62,45,95,41,55,93,69,39,17,12,1,20,53,49,71,61,13,88,25,87,26,50,58,28,51,89,64,3,80,36,65,57,92,52,86,98,78,9,33,44,63,16,34,97,60,40,66,75,4,7,84,22,43,11,85,91,32,48,14,18,76,8,47,24,81,35,30,82,67,37,70,15,5,73,59,54,68,56,96,99,10'
numbers = list(map(int, numbers.split(',')))
boards = []


def tup(n):
    return [n, False]


def mark(n):
    return (n, False)


class Board:
    def __init__(self, board):
        grid = list(map(lambda i: list(filter(lambda x: x != '', i.split(' '))), board))
        a = list(map(lambda l: list(map(tup, l)), grid))
        self.board = a
        self.win = False

    def mark(self, num):
        for line in self.board:
            for n in line:
                if int(n[0]) == num:
                    n[1] = True

    def check_win(self):
        for i in range(5):
            hor = True
            ver = True
            line = self.board[i]
            for x in line:
                if not x[1]:
                    hor = False
            vline = [line[i][1] for line in self.board]
            for x in vline:
                if not x:
                    ver = False
            if hor or ver:
                return True

    def sum(self):
        sum = 0
        for line in self.board:
            for y in line:
                if not y[1]:
                    sum += int(y[0])
        return sum

for i, val in enumerate(lines):
    if val == '':
        b = lines[i - 5:i]
        boards.append(Board(b))
    if i == len(lines) - 1:
        b = lines[i - 4:i + 1]
        boards.append(Board(b))

for num in numbers:
    for b in boards:
        b.mark(num)
        if b.check_win() and not b.win:
            b.win = True
            print(b.sum()*num)

# print(lines)
# print(lines[0:lines.index('')])
