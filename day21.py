mem = {}
mapper = {'6': 7, '5': 6, '7': 6, '4': 3, '8': 3, '3': 1, '9': 1}

def play(p1, p2, score1, score2, p1turn,opoints):
    points = opoints
    h = str(p1)+'-'+str(p2)+'-'+str(score1)+'-'+str(score2)+'-'+str(p1turn)
    if h in mem.keys():
        points+=mem[h]       
    elif score1 > 20:
        points+=1
        mem[h] = points
    elif score2 > 20:
        mem[h] = points     
    else:
        for key in mapper:
            if p1turn:
                np1 =((p1 + int(key) -1) % 10) +1
                sc = play(np1, p2, score1+np1, score2, not p1turn,opoints)
            else:
                np2=((p2 + int(key) -1) % 10) +1
                sc = play(p1, np2, score1, score2+np2, not p1turn,opoints)
            points += (mapper[key] * sc)
    return points        

print(play(1, 10, 0, 0, True,0))


[x for x in range(10)]