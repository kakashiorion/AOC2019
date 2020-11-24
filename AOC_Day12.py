import math
#s1=(-17,9,-5)
#s2=(-1,7,13)
#s3=(-19,12,5)
#s4=(-6,-6,-4)

class Moon:
    def __init__(self, xpos, ypos, zpos):
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.xvel =0
        self.yvel =0
        self.zvel =0
    def potEnergy(self):
        return abs(self.xpos) +abs(self.ypos)+abs(self.zpos)
    def kinEnergy(self):
        return abs(self.xvel) +abs(self.yvel)+abs(self.zvel)

m1 = Moon(-17,9,-5)
m2 = Moon(-1,7,13)
m3 = Moon(-19,12,5)
m4 = Moon(-6,-6,-4)

def updateVelocity(m1,m2,m3,m4):
    #update m1.xpos
    count=0
    if m1.xpos< m2.xpos:
        count+=1
    elif m1.xpos> m2.xpos:
        count-=1
    if m1.xpos< m3.xpos:
        count+=1
    elif m1.xpos>m3.xpos:
        count-=1
    if m1.xpos<m4.xpos:
        count+=1
    elif m1.xpos>m4.xpos:
        count-=1
    m1.xvel+=count
    #update m2.xpos
    count=0
    if m2.xpos< m1.xpos:
        count+=1
    elif m2.xpos> m1.xpos:
        count-=1
    if m2.xpos< m3.xpos:
        count+=1
    elif m2.xpos>m3.xpos:
        count-=1
    if m2.xpos<m4.xpos:
        count+=1
    elif m2.xpos>m4.xpos:
        count-=1
    m2.xvel+=count
    #update m3.xpos
    count=0
    if m3.xpos< m1.xpos:
        count+=1
    elif m3.xpos> m1.xpos:
        count-=1
    if m3.xpos< m2.xpos:
        count+=1
    elif m3.xpos>m2.xpos:
        count-=1
    if m3.xpos<m4.xpos:
        count+=1
    elif m3.xpos>m4.xpos:
        count-=1
    m3.xvel+=count
    #update m4.xpos
    count=0
    if m4.xpos< m1.xpos:
        count+=1
    elif m4.xpos> m1.xpos:
        count-=1
    if m4.xpos< m2.xpos:
        count+=1
    elif m4.xpos>m2.xpos:
        count-=1
    if m4.xpos<m3.xpos:
        count+=1
    elif m4.xpos>m3.xpos:
        count-=1
    m4.xvel+=count

    #update m1.ypos
    count=0
    if m1.ypos< m2.ypos:
        count+=1
    elif m1.ypos> m2.ypos:
        count-=1
    if m1.ypos< m3.ypos:
        count+=1
    elif m1.ypos>m3.ypos:
        count-=1
    if m1.ypos<m4.ypos:
        count+=1
    elif m1.ypos>m4.ypos:
        count-=1
    m1.yvel+=count
    #update m2.ypos
    count=0
    if m2.ypos< m1.ypos:
        count+=1
    elif m2.ypos> m1.ypos:
        count-=1
    if m2.ypos< m3.ypos:
        count+=1
    elif m2.ypos>m3.ypos:
        count-=1
    if m2.ypos<m4.ypos:
        count+=1
    elif m2.ypos>m4.ypos:
        count-=1
    m2.yvel+=count
    #update m3.ypos
    count=0
    if m3.ypos< m1.ypos:
        count+=1
    elif m3.ypos> m1.ypos:
        count-=1
    if m3.ypos< m2.ypos:
        count+=1
    elif m3.ypos>m2.ypos:
        count-=1
    if m3.ypos<m4.ypos:
        count+=1
    elif m3.ypos>m4.ypos:
        count-=1
    m3.yvel+=count
    #update m4.ypos
    count=0
    if m4.ypos< m1.ypos:
        count+=1
    elif m4.ypos> m1.ypos:
        count-=1
    if m4.ypos< m2.ypos:
        count+=1
    elif m4.ypos>m2.ypos:
        count-=1
    if m4.ypos<m3.ypos:
        count+=1
    elif m4.ypos>m3.ypos:
        count-=1
    m4.yvel+=count

    #update m1.zpos
    count=0
    if m1.zpos< m2.zpos:
        count+=1
    elif m1.zpos> m2.zpos:
        count-=1
    if m1.zpos< m3.zpos:
        count+=1
    elif m1.zpos>m3.zpos:
        count-=1
    if m1.zpos<m4.zpos:
        count+=1
    elif m1.zpos>m4.zpos:
        count-=1
    m1.zvel+=count
    #update m2.zpos
    count=0
    if m2.zpos< m1.zpos:
        count+=1
    elif m2.zpos> m1.zpos:
        count-=1
    if m2.zpos< m3.zpos:
        count+=1
    elif m2.zpos>m3.zpos:
        count-=1
    if m2.zpos<m4.zpos:
        count+=1
    elif m2.zpos>m4.zpos:
        count-=1
    m2.zvel+=count
    #update m3.zpos
    count=0
    if m3.zpos< m1.zpos:
        count+=1
    elif m3.zpos> m1.zpos:
        count-=1
    if m3.zpos< m2.zpos:
        count+=1
    elif m3.zpos>m2.zpos:
        count-=1
    if m3.zpos<m4.zpos:
        count+=1
    elif m3.zpos>m4.zpos:
        count-=1
    m3.zvel+=count
    #update m4.zpos
    count=0
    if m4.zpos< m1.zpos:
        count+=1
    elif m4.zpos> m1.zpos:
        count-=1
    if m4.zpos< m2.zpos:
        count+=1
    elif m4.zpos>m2.zpos:
        count-=1
    if m4.zpos<m3.zpos:
        count+=1
    elif m4.zpos>m3.zpos:
        count-=1
    m4.zvel+=count

def updatePosition(m1,m2,m3,m4):
    m1.xpos+=m1.xvel
    m2.xpos+=m2.xvel
    m3.xpos+=m3.xvel
    m4.xpos+=m4.xvel
    m1.ypos+=m1.yvel
    m2.ypos+=m2.yvel
    m3.ypos+=m3.yvel
    m4.ypos+=m4.yvel
    m1.zpos+=m1.zvel
    m2.zpos+=m2.zvel
    m3.zpos+=m3.zvel
    m4.zpos+=m4.zvel

#Part 1: 1000 steps
for i in range(1000):
    updateVelocity(m1,m2,m3,m4)
    updatePosition(m1,m2,m3,m4)

def calcEnergy(m1,m2,m3,m4):
    m1Energy=m1.potEnergy()*m1.kinEnergy()
    m2Energy=m2.potEnergy()*m2.kinEnergy()
    m3Energy=m3.potEnergy()*m3.kinEnergy()
    m4Energy=m4.potEnergy()*m4.kinEnergy()
    totalEnergy = m1Energy+m2Energy+m3Energy+m4Energy
    return totalEnergy

print(calcEnergy(m1,m2,m3,m4))
#total energy(after 1000 steps) = 8742

#Part2: Reach same state
def findPeriodX():
    m1 = Moon(-17,9,-5)
    m2 = Moon(-1,7,13)
    m3 = Moon(-19,12,5)
    m4 = Moon(-6,-6,-4)
    step=1
    running=True
    while(running):
        updateVelocity(m1,m2,m3,m4)
        updatePosition(m1,m2,m3,m4)
        if m1.xvel==0 and m2.xvel==0 and m3.xvel==0 and m4.xvel==0:
            running=False
        else:
            step+=1
    return step

def findPeriodY():
    m1 = Moon(-17,9,-5)
    m2 = Moon(-1,7,13)
    m3 = Moon(-19,12,5)
    m4 = Moon(-6,-6,-4)
    step=1
    running=True
    while(running):
        updateVelocity(m1,m2,m3,m4)
        updatePosition(m1,m2,m3,m4)
        if m1.yvel==0 and m2.yvel==0 and m3.yvel==0 and m4.yvel==0:
            running=False
        else:
            step+=1
    return step

def findPeriodZ():
    m1 = Moon(-17,9,-5)
    m2 = Moon(-1,7,13)
    m3 = Moon(-19,12,5)
    m4 = Moon(-6,-6,-4)
    step=1
    running=True
    while(running):
        updateVelocity(m1,m2,m3,m4)
        updatePosition(m1,m2,m3,m4)
        if m1.zvel==0 and m2.zvel==0 and m3.zvel==0 and m4.zvel==0:
            running=False
        else:
            step+=1
    return step

xperiod=findPeriodX()
yperiod=findPeriodY()
zperiod=findPeriodZ()

#print(xperiod,yperiod,zperiod)

def findLCM(a,b,c):
    res=math.gcd(a,b)
    lcm = a*b//res
    res=math.gcd(lcm,c)
    lcm= lcm*c//res
    return lcm

print(findLCM(xperiod,yperiod,zperiod)*2)
#325433763467176
