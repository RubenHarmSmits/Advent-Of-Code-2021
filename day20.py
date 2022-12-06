inc = 100
input = [list(inc*'.'+x+inc*'.') for x in list(open('input.txt').read().split('\n'))]
os = len(input)
for i in range(inc):
    input.insert(0,list((os+2*inc)*'.'))
    input.append(list((os+2*inc)*'.'))

algo2 = '########..#..#.##.##.#.#..#.#.###.######.##..##.##..#...#....##.##...##.#.#...#.#.##.###.#.##.#.##.#...#.#.###.#.##.#.####.###..#.####.##..#.#####..####.#.#.#....##.#.#.##...#.####.#....#.##..##...#...#.##..#...#.#..#..#.#.#..##..#.##.##..##...#..###...##..#..###.###.##..#..#####...#.#..###..##....##...#####.#####...##.#.##.#....#.##.#.###.#.##.#.##...######.#...##.#..#.#.#...###.#..#.##.####..##.#..#.##.#.##.######.#.....#.#....####.####.###...#....#..###..###.#...#.#.#.##..#..##.#.#..#..###.#.###..#......'
l = input[0]
for _ in range(50):
    output = []
    for y in range(l):
        line = []
        for x in range(l):
            string = ''
            for iy in range (-1,2):
                for ix in range (-1,2):
                    try:
                        string+=input[y+iy][x+ix]
                    except IndexError:
                        string+='.' if _ % 2 == 0 else '#'
                            
            line.append(algo2[int(''.join(a = list(map(lambda c: '1' if c == '#' else '0',''.join(string)))),2)])
        output.append(line)
    input = output

print(sum(list(map(lambda l:l.count('#'),output))))