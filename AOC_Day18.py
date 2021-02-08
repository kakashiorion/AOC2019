maze=["#################################################################################",
"#.#...........#...#.....#.......#...#...#.....#.....#.....#...#...#..g.........x#",
"#.#.#####.###Z#.#.#.###.#.#.###.#.###.#.#.###.#.#####.#.#.#.#.#.###.###########.#",
"#...#...#.#.....#.#.#.#...#.#...#.#...#.#.#.#.#.#.....#p#.#.#.#.......#...#.....#",
"#.#####.#.#########.#.#####.#.###.#.###.#.#.#.#.#.#####.#.#.#.#######.###.#.###.#",
"#.......#...#.......#.....#.#.#.....#...#.#.....#...#...#...#.#.....#.....#.#...#",
"###########.#.#########.###.#.###.###.###.#####.###.#.#######.#.###.#####.#.#.###",
"#...V.....#.......#...#.#...#...#...#...#.#...#...#.#.#.......#.#.#.#.....#.#...#",
"#.#######.#######.#.#.#.#.#####.#######.#.#.#.#.###.#.#######.#.#.#.#.#####B###.#",
"#.#.......#...#.....#...#.....#.....#...#...#.#.#...#.......#...#...#.....#...#.#",
"#.#.#####.#.#K#.#############.#####.#.#.#####.###.#########.#####.#######.###.###",
"#.#.#.....#.#.#...#...#.......#...#.#.#.#...#.#...#...#.....#.....#....l..#.#...#",
"#.#.#####.#.#.###.#.#.#.#######.#.#.#.###.#.#.#.###.#.#.#####.#######.#####.###.#",
"#.#.....#.#.#...#.#.#.#.....#...#...#...#.#...#.#...#.#...#...#.....#.........#.#",
"#.#####.#.#.###.#.#.#.#####.#####.#####.#.#####.#.#.#####.#.###.###.#######.###.#",
"#.#...#.#.#...#.#.#.#..j..#.....#.......#.#...#...#.#...#.#.....#...#.......#...#",
"#.#.###.#Q###.#.###.#####.#####I#######.#.#.#.#.#####.#.#.#######.#######.###.#.#",
"#...#...#.#...#.....#...#.....#.....#...#.#.#...#.....#.#.#.#.....#.....#h..#.#.#",
"###.#.#####.#########.#.#####.#.###.#.###.#.#####.#####.#.#.#.#####.###.#####.#.#",
"#...#...#...#.......#.#.......#...#.#...#.#.#.....#.....#.#.....#.....#.......#.#",
"#.#####.#.###.#####.#.###########.#.#####.#.#.#####.#####.#.###.#####.###########",
"#.....#.#...#.#.....#.#.......#...#.#...#...#.#.......#...#.#.#.....#.....#.....#",
"#####.#.###.#.#.###.###.###.###.###.#.#.#####.#######.###.###.#####.#####.#.###.#",
"#.#...#...#.#.#.#...#.....#...#.#.#.#.#.#.....#...#.#.....#...#...#.....#.....#.#",
"#.#.###.###.###.#.###########.#.#.#.#.#.#.#.###.#.#.#####.#.#####.#####.#######.#",
"#.#...#...#.....#.#..e....#...#...#...#.#.#.#...#.#...#...#.....#.....#.#.......#",
"#.###.###.#######.#.#####.#.#####.#####.#.###.###.#.#.#.#######.#.#.###.#.#####.#",
"#.#...#.#...#...#...#.....#.#.........#.#.#.....#.#.#.#.......#.#.#.....#...#...#",
"#.#.###.#.###.#.#####.#####.#.#########.#.#.#####.###.###.#####.#.#########.#.###",
"#...#...#...#.#.....#.#.#.......#...#...#.#o#.#...#...#...#.....#.#.........#...#",
"#.#####.###.#.#.#####.#.#.#######.#.#.#.#.#.#.#.###.###.###.#####.#####.#######U#",
"#.........#...#...#...#...#.......#...#.#.....#...#.....#.#.#...#.#.....#.....#.#",
"#########.#######.#.###.###.###########.#.#######.#.#####.#.#.#.#.#.#########.#.#",
"#.......#.......#...#.....#...#.#.....#.#.#.....#.#.......#.#.#.#.#.#.......#...#",
"#.#####.#######.#############.#.#.#.###.#.#.###.#.#########.#.###.#.#.#####.#####",
"#.....#.#.......#.....#.......#.#.#.#...#.#.#.....#...#.....#.#...#.....#.#..tE.#",
"#.###.###.#######.###.#.#######.#.#.#.###.#.#######.#.#.#####.#.#######.#.#####.#",
"#.S.#...#.....#...#.#c..#...#.....#.#.#.#.#...#.....#..s#.....#.#.....#...#...#.#",
"###.###.#####.#.###.#####.#.#.#####.#.#.#.###.#.#########.###.#.###.#.#####.#.#.#",
"#.....#.........#.........#.......#.........#...#...........#.....F.#.......#...#",
"#######################################.@.#######################################",
"#m........#.............#...........#.........#.....#.........#.....#...#.......#",
"###.#####.#########.#####.#####.###.#.#.#.#.#.#.###.#.#####.#.#.###.#.#.#.###.#.#",
"#...#.#...#.......#...#...#...#.#.#...#.#.#.#.#...#...#...#.#.....#.#.#.#.#...#.#",
"#.###W#.###.#####.#.#.#O###.#.#.#.#####.###.#####.#####.#.#########.#.#.#.#.###.#",
"#.#.......#...#.#.#.#.#...#.#.#.#...#...#...#...#.....#.#.#...#...#.C.#.#.#.#...#",
"#.#######.###.#.#.#.#.###.#.#.#.#.###.###.###.#.#.#####.#.#.#.#.#.#####.#.#.###.#",
"#.#...#.#.#...#...#.#.#...#.#...#.......#.....#...#.....#.#.#.#.#.....#...#...#.#",
"#.#.#.#.#.#.###.###.#.#.###.#####.#######.#########.#####.#.#.#.#####.#.#####.#.#",
"#.#f#.#.#.#.#.#.#...#...#...#...#...#...#.#.......#...#.....#.#.#...#.#...#.#.#.#",
"#.#.#.#.#.#.#.#.#.#######.###.###.###.#D#.###.#.#####.#######.#.#.###.###.#.#.#.#",
"#...#.#...#.#...#.....#.#...#.....#...#.#...#.#.#...#.....#.#.#.#.....#.....#.#.#",
"#####.#.###.#.#######.#.###.###.###.###.###.#.###.#.#####.#.#.#.#.#####.#####.#.#",
"#.....#...#.#.#...#...#...#...#.#a..#.#.#.#.#.....#.....#.#...#.#w#...#...#...#.#",
"#.#######.#.#.#.#.#.###.#####.###.###.#.#.#.#.#######.###.#.###.#.#.#####.#.###.#",
"#.#.....#.#.#.#.#.#...#.#...#...#...#.#.#...#.....#...#...#...#.#.#.......#.#...#",
"#.###.#.#.#.#.#.#.###.#.#.#.#.#.###.#.#.#.#########.#.#.#####.#M#.#########.###.#",
"#...#.#...#.#...#.#.....#.#.#.#...#.#..d#.#.........#.#.#.......#...#.....#...#.#",
"#.#.#.#####.#####.#######.#.#####.#.#.###.###.#####.###.#.#########.#.###.###.#.#",
"#.#.#...#...#.............#.......#.#...#.#i..#.....#...#.#.......#...#.#...#.#.#",
"###.###.#.###.#################.###A###.#.#.###.#####.###.#.#####.#####.###.#.###",
"#...#.....#.#.#.....#.Y...#...#.#...#.#.#...#.#.#.#...#...#.#.N...#.........#...#",
"#.###.#####.#.#.###.#####.###.#.#.###.#.#####.#.#.#.###.###.#############.#####.#",
"#...#.#...#...#.#.#.....#...#...#.#...R.#.#.....#.#...#...#.....#...#...#q....#.#",
"#.#.###.#.#.###.#.###.#.###.#####.#.#####.#.#####.###.#########.#.#.#.#.#####.#.#",
"#.#...#.#.#.#...#...#.#...#..y....#.#...#.#.#.......#.........#...#...#...#.#.#.#",
"#####.#.#.###.###.#.#.###.#########.#.#.#.#.#.#####.#########.###########.#.#.#.#",
"#...#.#.#...#.#...#.#...#.....#...#.#.#.#.#.#.#.............#.#...#.....#.#.#.#.#",
"#.#.#.#.###.#.#.#######.#####.#.#.#.###.#.#.#.#.#######.#####.#.#.#.###.#.#.#.#.#",
"#.#...#.#.#.#...#.......#...#.#.#r..#...#...#.#.#.....#.#...#...#.#...#...#.#.#.#",
"#T###.#.#.#.###.#.#######.#.###.#####.###.#####.#.###.#.#.#.#####.###.#####.#.#.#",
"#.#...#u..#.....#...#...#n#...#.#.#.....#.#...#.#...#.#.#.#.#.......#.....#.....#",
"#.#.#####.#########.#.#H#.###.#.#.#.###.#.#.#.#.#.###.#.#.#J#.###########.#####.#",
"#.#.....#.#...#...#.#.#...#.#...#.#...#.#...#.#...#...#.#.#...#.........#.....#.#",
"#.#######.#.###.#.#.#.#####.#####.###.#.#####.#.###.#####.#.###.#####.#######.#.#",
"#.#.......#.#...#...#...#.....L.#.....#.#.#...#..v#z..#...#.#...#...#.......#.#.#",
"#.#.#######.#.###.#####.#.#####.#######.#.#.#########.#.#####.###.#.###.#####.#.#",
"#.#.#k......#...#.#...#...#.....#.....#.#.#.....#...#.#..b....#...#...#...#...#.#",
"#.#.#.#####.###.###.#.#####.#####.###.#.#.#####.#.#.#.#############.#.###X#.###.#",
"#.....#.......#...G.#.............#.....#.........#...P.............#...#...#...#",
"#################################################################################"]

wall="#"
path="."
home="@"

homePosition=(40,40)

keyPositions={}
doorPositions={}
masterMaze={}
for y in range(len(maze)):
    for x in range(len(maze[y])):
        currentChar=maze[y][x]
        masterMaze[(x,y)]=currentChar
        if currentChar!=wall and currentChar!=path and currentChar!=home and currentChar.islower():
            keyPositions[currentChar]=(x,y)
        
        if currentChar!=wall and currentChar!=path and currentChar!=home and currentChar.isupper():
            doorPositions[currentChar]=(x,y)
#print(keyPositions)
#print(doorPositions)
#print(masterMaze)

def createNewMaze():
    newMaze={}
    for i in range(81):
        for j in range(81):
            newMaze[(i,j)]=0
    return newMaze

def addGraph(starting, currentPosition,length, visitedMaze,graph,pathLengths):
    visitedMaze[currentPosition]=1

    up=(currentPosition[0],currentPosition[1]-1)
    down=(currentPosition[0],currentPosition[1]+1)
    left=(currentPosition[0]-1,currentPosition[1])
    right=(currentPosition[0]+1,currentPosition[1])

    length=length+1
    if (up not in graph):
        graph[up]=length
    if (down not in graph):
        graph[down]=length
    if (left not in graph):
        graph[left]=length
    if (right not in graph):
        graph[right]=length

    if(visitedMaze[up]==0 and (masterMaze[up]==path or masterMaze[up]==home or masterMaze[up] in keyPositions)):
        #graph[up]=length+1
        if (masterMaze[up] in keyPositions):
            #thisDoor=masterMaze[up]
            #masterMaze[doorPositions[thisDoor.upper()]]=path
            #print(masterMaze[up])
            #foundKeys[masterMaze[up]]=starting
            pathLengths[(starting,masterMaze[up])]=graph[up]
        addGraph(starting,up, graph[up], visitedMaze,graph,pathLengths)

    if(visitedMaze[down]==0 and (masterMaze[down]==path or masterMaze[down]==home or masterMaze[down] in keyPositions)):
        #graph[down]=length+1
        if (masterMaze[down] in keyPositions):
            #thisDoor=masterMaze[down]
            #masterMaze[doorPositions[thisDoor.upper()]]=path
            #print(masterMaze[down])
            #foundKeys[masterMaze[down]]=starting
            pathLengths[(starting,masterMaze[down])]=graph[down]
        addGraph(starting,down, graph[down], visitedMaze,graph,pathLengths)
    
    if(visitedMaze[left]==0 and (masterMaze[left]==path or masterMaze[left]==home or masterMaze[left] in keyPositions )):
        #graph[left]=length+1
        if (masterMaze[left] in keyPositions):
            #thisDoor=masterMaze[left]
            #masterMaze[doorPositions[thisDoor.upper()]]=path
            #print(masterMaze[left])
            #foundKeys[masterMaze[left]]=starting
            pathLengths[(starting,masterMaze[left])]=graph[left]
        addGraph(starting,left, graph[left], visitedMaze,graph,pathLengths)

    if(visitedMaze[right]==0 and (masterMaze[right]==path or masterMaze[right]==home or masterMaze[right] in keyPositions )):
        #graph[right]=length+1
        if (masterMaze[right] in keyPositions):
            #thisDoor=masterMaze[right]
            #masterMaze[doorPositions[thisDoor.upper()]]=path
            #print(masterMaze[right])
            #foundKeys[masterMaze[right]]=starting
            pathLengths[(starting,masterMaze[right])]=graph[right]
        addGraph(starting,right, graph[right], visitedMaze,graph,pathLengths)

keyPositions[home]=homePosition
pathLengths={}

def djikstra():
    dist={}
    prev={}

    Q=[]
    for key in keyPositions:
        dist[key]=2000000
        prev[key]=''
        Q.append(key)
    dist[home]=0

    while(len(Q)!=0):
        
        minDist=1000000
        for x in Q:
            if dist[x]<minDist:
                u=x
                minDist=dist[x]
        
        #Open the door with this key
        if u!=home:
            masterMaze[doorPositions[u.upper()]]=path

        Q.remove(u)

        graph={}
        visitedMaze=createNewMaze()
        addGraph(u, keyPositions[u],0,visitedMaze, graph,pathLengths)
        for neighbor in pathLengths:
            if neighbor[1] in Q:
                newDist = dist[u]+pathLengths[(u,neighbor[1])]
                if newDist<dist[neighbor[1]]:
                    dist[neighbor[1]]=newDist
                    prev[neighbor[1]]=u
            if neighbor[0] in Q:
                newDist = dist[u]+pathLengths[(neighbor[1],u)]
                if newDist<dist[neighbor[0]]:
                    dist[neighbor[0]]=newDist
                    prev[neighbor[0]]=u

    return dist, prev
        
distanceList, previousList = djikstra()

for x in distanceList:
    print(x , distanceList[x])

for y in previousList:
    print(y, previousList[y])
print(pathLengths)

# currentNode=home
# collected={}
# totalDist=0
# collected[currentNode]=1
# while (len(collected)<27):    
    # first=True
    # for path in pathLengths:
    #     if path[0]==currentNode:
    #         if path[1] not in collected:
    #             if first:
    #                 minimumDist = pathLengths[path]
    #                 newNode=path[1]
    #                 first =False
    #             elif pathLengths[path]<minimumDist:
    #                 minimumDist = pathLengths[path]
    #                 newNode=path[1]
    # totalDist+=minimumDist
    # collected[newNode]=1
    # for x in pathLengths:
    #     if newNode in x[1]:
    #         currentNode=newNode
    #         break
    #     else:
    #         totalDist+=minimumDist


def Astar(startNode,finalNode):
    openList=[]
    closedList=[]
    openList.append(startNode)
    g={}
    h={}
    f={}
    g[startNode]=0
    predecessor={}
    while (len(openList)!=0):
        minimumOpen=10000
        for x in openList:
            if g[x]<minimumOpen:
                minimumOpen=g[x]
                q=x
        closedList.append(q)
        for path in pathLengths:
            if path[0]==q and path[1] not in closedList:
                if path[1] not in openList:
                    predecessor[path[1]]=q
                    g[path[1]]=g[q] + pathLengths[path] 
                    h[path[1]]=heuristicsDist(path[1],finalNode)
                    f[path[1]]=g[path[1]]+h[path[1]]
                    openList.append(path[1])
                else:
                    if g[path[1]]<g[q]+pathLengths[path]:
                        predecessor[path[1]]=q
                        g[path[1]]=g[q] + pathLengths[path]
                        f[path[1]]=g[path[1]] + heuristicsDist(path[1],finalNode)
        if q==finalNode:
            reqPath=[]
            currentVert=finalNode
            while(currentVert!=startNode):
                reqPath.append(currentVert)
                currentVert=predecessor[currentVert]
            reqPath.append(startNode)
            return reqPath, g[finalNode]
        openList.remove(q)

def heuristicsDist(keyA, keyB):
    return abs(keyPositions[keyA][0]-keyPositions[keyB][0]) + abs(keyPositions[keyA][1]-keyPositions[keyB][1])

print(Astar('l','o'))

newKeys=[]
for x in keyPositions:
    newKeys.append(x)
newKeys.remove(home)
finalPath=[home]
totalDist = 0
i=0
currentVert=home
nextVert=''
for i in range(26):
    minDist=100000
    for x in newKeys:
        result=Astar(currentVert,x)
        if result[1]<minDist:
            minDist=result[1]
            nextVert=x
    newKeys.remove(nextVert)
    finalPath.append(nextVert)
    totalDist+=minDist
    print(nextVert,totalDist)
    currentVert=nextVert

print(finalPath)
print(totalDist)




