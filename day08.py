lines = [x.strip().split(' ') for x in open('input.txt').read().strip().split('\n')]

numbers = [[],['rb', 'ro'],['mb', 'rb','mm', 'lo', 'mo'],['mb', 'rb','mm', 'ro', 'mo'],['lb','mm', 'rb','ro'],['lb','mb','mm','ro','mo'],['lb','mb','mm', 'lo','ro','mo'],['mb', 'rb', 'ro'],['lb','mb', 'rb','mm', 'lo','ro','mo'],['lb','mb', 'rb','mm','ro','mo']]
#acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab

def calcScore(line):
    input = line[0:10]
    output = line[11:]
    print(input ,3,output)
    a= b = c = d = e = f = g = ['mb', 'lb', 'rb', 'mm', 'lo', 'ro', 'mo']
    one = next(x for x in input if len(x) ==2 )
    four = next(x for x in input if len(x) ==4 )
    seven = next(x for x in input if len(x) ==3 )
    eight = next(x for x in input if len(x) ==7 )

     # 2,3,5 == len 6
     # 6,9 == len 5
    for l in one:
        if l == 'a':
            ll =a

        print(l, one)

    a = list(filter(lambda i:i=='lb' or i=='lo',a))

for line in lines:
    calcScore(line)

