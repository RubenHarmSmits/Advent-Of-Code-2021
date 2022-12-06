from collections import Counter
import numpy
from coor import Coor
import math
lines = [list(map(lambda c:int(c) if c.isnumeric() else c,x)) for x in list(open('input.txt').read().split('\n'))]


def run(lines):
    while True:
        line = lines[0]
        cont = True
        while cont:
            cont = False
            #check explosions
            exploding = True
            while exploding:
                exploding = False
                open = 0
                for i,n in enumerate(line):
                    if open == 5:
                        pair = line[i-1:i+line[i:].index(']')+1]
                        left = pair[1:pair.index(',')][0]
                        right = pair[pair.index(',')+1:-1][0]
                        for l in range(i):
                            if isinstance(line[i-l-2],int):
                                line[i-l-2]+=left
                                break
                        for r in range(len(line)-i-3):
                            if isinstance(line[i+3+r],int):
                                line[i+3+r]+=right
                                break
                        line[i-1:i+line[i:].index(']')+1] = [0]
                        exploding = True
                        break
                    if n == '[':
                        open +=1
                    if n == ']':
                        open -=1

            #check splits
            for i,n in enumerate(line):
                if len(str(n))>1:
                    line[i:i+1] = ['[',int(n/2),',',math.ceil(n/2),']'] 
                    cont =True
                    break


        if len(lines) == 1:
            break
        second = lines.pop(1)
        lines[0] = ['['] + line + [','] + second + [']']

    ans = lines[0]


    going = True
    while going:
        going = False
        for i,n in enumerate(ans[:-2]):
            if isinstance(ans[i],int) and isinstance(ans[i+2],int):
                left = ans[i]
                right = ans[i+2]
                res = 3 * left + 2* right
                ans[i-1:i+4] = [res]
                going = True
                break
    return ans[0]


options = []
for line1 in lines:
    for line2 in lines:
        if line1 != line2:
            options.append(run([line1,line2]))
print(max(options))




