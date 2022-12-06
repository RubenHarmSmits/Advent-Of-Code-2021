from collections import Counter
import numpy
from coor import Coor
import math



line = open('input.txt').read()

mapper = {}
mapper['0']='0000'
mapper['1']='0001'
mapper['2']='0010'
mapper['3']='0011'
mapper['4']='0100'
mapper['5']='0101'
mapper['6']='0110'
mapper['7']='0111'
mapper['8']='1000'
mapper['9']='1001'
mapper['A']='1010'
mapper['B']='1011'
mapper['C']='1100'
mapper['D']='1101'
mapper['E']='1110'
mapper['F']='1111'

hex = list(''.join(list(map(lambda c:mapper[c],line))))

def getDecimal(arr):
    return int(''.join(arr),2)

ans = 0

def subPackage(hex):
    i=0
    output=0
    version = getDecimal(hex[i:i+3])
    global ans
    ans+=version
    type = getDecimal(hex[i+3:i+6])
    i+=6
    if type == 4:
        start = '1'
        a =''
        while start == '1':
            package = hex[i:i+5]
            start = package.pop(0)
            a+=''.join(package)
            i+= 5
        output = getDecimal(a)
        
    else:
        subpackages = []
        id = hex[i]
        if id == '0':
            sub = hex[i+1:i+16]
            num = getDecimal(sub)
            i+=16
            tot=0
            while tot<num:
                a , o= subPackage(hex[i:])
                subpackages.append(o)
                i+=a
                tot+=a
        if id == '1':
            sub = hex[i+1:i+12]
            i+=12
            num = getDecimal(sub)
            for _ in range(num):
                isu,o = subPackage(hex[i:])
                i+= isu
                subpackages.append(o)

        if type == 0:
            output = sum(subpackages)
        if type == 1:
            output = math.prod(subpackages)        
        if type == 2:
            output = min(subpackages)    
        if type == 3:
            output = max(subpackages)      
        if type == 5:
            output = 1 if subpackages[0] > subpackages[1] else 0
        if type == 6:
            output = 1 if subpackages[0] < subpackages[1] else 0
        if type == 7:
            output = 1 if subpackages[0] == subpackages[1] else 0
    return i, output

i, output = subPackage(hex)
print('ans= ', output)





