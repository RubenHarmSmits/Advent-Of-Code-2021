# from collections import Counter

# a = Counter()

# a.update({(3,4):6, (5,6):8, (8,9):7})

# for (t,i), y in a.items():
#     print(3)

# a=6 ; b =9
# print(a,b)


input = [x for x in list(open('input.txt').read().split('\n'))]

blocks = []
# size=300000
# grid = size*[size*[size*[False]]]



# grid = [[[False for _ in range(size)] for _ in range(size)] for _ in range(size)]

def compareBlocks(bn, bo):
    y=False
    x=False
    z=False
    if  min(bo[0],bo[1]) <= bn[0] <= max(bo[0],bo[1]):
        x = True
        x1=True
    if  min(bo[0],bo[1]) <= bn[1] <= max(bo[0],bo[1]):
        x = True
        x1=False
    if  min(bo[2],bo[3]) <= bn[2] <= max(bo[2],bo[3]):
        y = True
        y1=True
    if  min(bo[2],bo[3]) <= bn[3] <= max(bo[2],bo[3]):
        y = True
        y1 = False
    if  min(bo[4],bo[5]) <= bn[4] <= max(bo[4],bo[5]):
        # new is bigger
        z = True
        z1 = True
    if  min(bo[4],bo[5]) <= bn[5] <= max(bo[4],bo[5]):
        z = True
        z1 = False
    hasOverlap = y == x == z == True
    if hasOverlap:
        blocks.remove(bo)
        a=b=c=()
        if z1:
            a = (bo[0],bo[1],bo[2],bo[3],bo[4],bn[4]-1)
            if x1:
                b = (bo[0],bn[0]-1,bo[2],bo[3],bn[4],bo[5])
                if y1:
                    c = (bn[0],bo[1],bo[3],bn[3]-1,bn[4],bo[5])
                else:
                    c = (bn[0],bo[1],bn[4]-1,bo[3],bn[4],bo[5])
            else:
                b = (bn[1]+1,bo[1],bo[2],bo[3],bn[4],bo[5])
                if y1:
                    c = (bo[0],bn[1],bo[2],bn[2]-1,bn[4],bo[5])
                else:
                    c = (bo[0],bn[1],bn[3],bo[2],bn[4],bo[5])

        
        
        blocks.append(a)
        blocks.append(b)
        blocks.append(c)

    

    
    return hasOverlap

        




for line in input:
    c = line.replace("x=","..").replace(",y=","..").replace(",z=","..").split("..")
    isOn = c.pop(0) == 'on '
    c = [int(n) for n in c]

    block = (c[0], c[1], c[2], c[3], c[4], c[5])

    if isOn:
        copy = blocks[:]
        for b in copy:
            compareBlocks(block, b, )

    blocks.append(block)

total = 0
for b in blocks:
    total+= (abs(b[0] - b[1])+1) * (abs(b[2] - b[3])+1) * (abs(b[4] - b[5])+1)
print(total)
