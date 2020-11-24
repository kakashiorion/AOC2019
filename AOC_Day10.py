import math

l1='.#.####..#.#...#...##..#.#.##...#####.##..#..##....#..#...#.......#.......##.##.#....##..#..#..##..#.###.....#.#..###.#...#..#..##..#.#.##..###..........##....#.##.#.#..##.##.#...#.##...#.#.##..#.#........#.#...##...##.##..#.#.##.#.#.#.##.##..##....#...###.#..##.#...##..###.###..##......#..#...###.#.#..#.####.#..#....#.##..#.#.#..#...#..#.#######....###.....####..#.#.#...##...##....#..####..#.##.#.#..##.###.#.##.##....#.........#.#.#.#.......#..#...##.#.....#.#.##........#..###..###.....#.............#.##.#...#....#..####.#.#......##...#..##..###...#.....#...##..#...####..#.#.##..#....#.#.....####.#####.#.#....#.#....##.#.#.#..#......#.........##..#.#.#....##.....#........#..##.##..###.##...##..#.##.#.#...#.#.###.###....##....#.#.....#.###...#...#......#........####..#.#....#.###.##.#...#.#.#.#..............##....#...#.....#..#####....#.........#..#..#.#.#..##...#...###.#..#.###....#.##.'

l={}
for i in range(30):
    for j in range(30):
        l[(j,i)]=l1[i*30+j]

def myfunc(n):
    return n[1]

def findAsetroidAngle(l,x,y):
    p={}
    for item in l:
        angle=0.0
        if (l[item]=='#' and (x!=item[0] or y!= item[1])):
            distance=math.sqrt(((x-item[0])*(x-item[0])) +((y-item[1])*(y-item[1])))
            if x==item[0] and y>item[1]:
                angle=0.0
            elif x==item[0] and y<item[1]:
                angle=180.0
            elif x<item[0] and y==item[1]:
                angle=90.0
            elif x>item[0] and y==item[1]:
                angle=270.0
            elif x<item[0] and y>item[1]:
                slope=(y-item[1])/(item[0]-x)
                angle=90.0 - math.degrees(math.atan(slope))
            elif x>item[0] and y>item[1]:
                slope=(y-item[1])/(item[0]-x)
                angle=270.0 - math.degrees(math.atan(slope))
            elif x>item[0] and y<item[1]:
                slope=(y-item[1])/(item[0]-x)
                angle=270.0 - math.degrees(math.atan(slope))
            elif x<item[0] and y<item[1]:
                slope=(y-item[1])/(item[0]-x)
                angle=90.0 - math.degrees(math.atan(slope))
            found=(item,distance)
            if angle in p:
                newList=p[angle]
                newList.append(found)
                newList.sort(key=myfunc)
                p[angle]=newList
            else:
                newList=[found]
                p[angle]=newList
    return p

f={}
for asteroid in l:
    y=asteroid[1]
    x=asteroid[0]
    p=findAsetroidAngle(l,x,y)
    count=0
    for item in p:
        count+=1
    if l[asteroid]=='#':
        f[asteroid]=count

maximum=0
for item in f:
    if f[item]>maximum:
        maximum=f[item]
        suitableAsteroid=item

print(maximum)
print(suitableAsteroid)
#visible=286, asteroid=(22,25)

#part 2

baseAsteroid=findAsetroidAngle(l,22,25)

baseAngles=[]
for item in baseAsteroid:
    baseAngles.append(item)
baseAngles.sort()
#print(baseAngles)

destroyed=0
#remaining=286
while destroyed!=200:
    for x in baseAngles:
        #selectedList=baseAsteroid[x]
        target=baseAsteroid[x].pop(0)
        destroyed+=1
        if destroyed==200:
            break

print(target)

#200th=(5,4)