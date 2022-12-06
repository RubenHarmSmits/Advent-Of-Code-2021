from collections import Counter
lines = [x for x in open('input.txt').read().strip().split('\n')]

def remove(isOne, i, lines):
    fil = filter(lambda line: line[i] == '1' if isOne else line[i] == '0', lines)
    return list(fil)

for i in range(len(lines[0])-1):
    col = [item[i] for item in lines]
    one  = col.count('1')
    zero = col.count('0')
    lines = remove(one>=zero, i, lines)
    if len(lines)==1:
        print(int(lines[0],2))


#
# from collections import Counter
#
# with open('input.txt') as f:
#     lines = f.readlines()
#
# def remove(isOne, i, lines):
#     fil = filter(lambda line: line[i] == '1' if isOne else line[i] == '0', lines)
#     return list(fil)
#
# for i in range(len(lines[0])-1):
#     print(lines)
#     col = [item[i] for item in lines]
#     one  = col.count('1')
#     zero = col.count('0')
#     lines = remove(one>=zero, i, lines)
#
#
#
# print(int(lines[0],2))


