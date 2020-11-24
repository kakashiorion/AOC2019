master=[3,8,1005,8,299,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,29,1,1007,14,10,2,1106,8,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,58,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,80,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,103,1,5,6,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,128,1,106,18,10,1,7,20,10,1006,0,72,1006,0,31,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,164,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,186,1,1007,8,10,1006,0,98,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,216,2,102,8,10,1,1008,18,10,1,1108,8,10,1006,0,68,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,253,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,274,1,1105,7,10,101,1,9,9,1007,9,1060,10,1005,10,15,99,109,621,104,0,104,1,21102,936995738520,1,1,21102,316,1,0,1106,0,420,21101,0,936995824276,1,21102,1,327,0,1106,0,420,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,248129784923,1,1,21102,1,374,0,1105,1,420,21102,29015149735,1,1,21101,385,0,0,1106,0,420,3,10,104,0,104,0,3,10,104,0,104,0,21101,983925826304,0,1,21101,0,408,0,1105,1,420,21102,825012036364,1,1,21101,0,419,0,1105,1,420,99,109,2,22101,0,-1,1,21101,0,40,2,21101,0,451,3,21102,441,1,0,1105,1,484,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,446,447,462,4,0,1001,446,1,446,108,4,446,10,1006,10,478,1101,0,0,446,109,-2,2105,1,0,0,109,4,2102,1,-1,483,1207,-3,0,10,1006,10,501,21102,0,1,-3,21201,-3,0,1,22102,1,-2,2,21102,1,1,3,21101,520,0,0,1106,0,525,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,548,2207,-4,-2,10,1006,10,548,21201,-4,0,-4,1105,1,616,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,1,567,0,1105,1,525,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,586,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,608,21201,-1,0,1,21102,1,608,0,106,0,483,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

l={}
for i in range(20):
    for j in range(20):
        l[(i,j)]='.'

def printmap(l):
    for i in range(20):
        for j in range (20):
            print(l[(j,i)],end=' ')
        print('\n')

def mul(number):
    c=str(number)
    if (c[len(c)-2:]=='02'):
        return True
def ad(number):
    c=str(number)
    if (c[len(c)-2:]=='01'):
        return True
def ip(number):
    c=str(number)
    if (c[len(c)-2:]=='03'):
        return True
def op(number):
    c=str(number)
    if (c[len(c)-2:]=='04'):
        return True
def halt(number):
    c=str(number)
    if (c[len(c)-2:]=='99'):
        return True
def jt(number):
    c=str(number)
    if (c[len(c)-2:]=='05'):
        return True
def jf(number):
    c=str(number)
    if (c[len(c)-2:]=='06'):
        return True
def ls(number):
    c=str(number)
    if (c[len(c)-2:]=='07'):
        return True
def eq(number):
    c=str(number)
    if (c[len(c)-2:]=='08'):
        return True

def getpar1(number):
    c=str(number)
    if(len(c)==3):
        #print("par1 is " + (c[0]))
        return int(c[0])
    if(len(c)==4):
       # print("par1 is "+ (c[1]))
        return int(c[1])
    if(len(c)==5):
       # print("par1 is"+ c[2])
        return int(c[2])

def getpar2(number):
    c=str(number)
    if(len(c)==3):
        return 0
    if(len(c)==4):
       # print("par2 is"+c[0])
        return int(c[0])
    if(len(c)==5):
       # print("par2 is"+c[1])
        return int(c[1])

def getpar3(number):
    c=str(number)
    if(len(c)==3):
        return 0
    if(len(c)==4):
        return 0
    if(len(c)==5):
      #  print("par3 is" +c[0])
        return int(c[0])

def amplifier(a, param,i):
    
    output=0
    while(a[i]!=99):
        # print(a[i], a[i+1],":",a[a[i+1]], a[i+2], a[i+3])
        if (a[i]>99):
            parType1=getpar1(a[i])
            parType2=getpar2(a[i])
            parType3=getpar3(a[i])
            if (ad(a[i])):
                if(parType1==1):
                    par1=int(a[i+1])
                else:
                    par1=int(a[a[i+1]])
                if(parType2==1):
                    par2=int(a[i+2])
                else:
                    par2=int(a[a[i+2]])
                b=par1+par2
                #print(b)
                if(parType3==1):
                    a[i+3]=b
                else:
                    a[int(a[i+3])]=b
                i=i+4
            elif (mul(a[i])):
                if(parType1==1):
                    par1=int(a[i+1])
                else:
                    par1=int(a[a[i+1]])
                if(parType2==1):
                    par2=int(a[i+2])
                else:
                    par2=int(a[a[i+2]])
                b=par1*par2
                #print(b)
                if(parType3==1):
                    a[i+3]=b
                else:
                    a[int(a[i+3])]=b
                i=i+4
            elif (op(a[i])):
                if(parType1==1):
                    res= (a[i+1])
                else:
                    res= (a[a[i+1]])
                if output==0:
                    output=1
                    final=[res]
                    i+=2
                elif output==1:
                    final.append(res)
                    final.append(i)
                    final.append(a)
                    output=0
                    return final
            elif jt(a[i]):
                if(parType1==1):
                    par1=a[i+1]
                else:
                    par1=a[a[i+1]]
                if(parType2==1):
                    par2=a[i+2]
                else:
                    par2=a[a[i+2]]
                if(par1!=0):
                    i = par2
                    #print ("jt index "+str(i))
                else:
                    i = i+3
            elif jf(a[i]):
                if(parType1==1):
                    par1=a[i+1]
                else:
                    par1=a[a[i+1]]
                if(parType2==1):
                    par2=a[i+2]
                else:
                    par2=a[a[i+2]]
                if(par1==0):
                    i = par2
                    #print ("jf index "+str(i))
                else:
                    i = i+3
            elif ls(a[i]):
                if(parType1==1):
                    par1=a[i+1]
                else:
                    par1=a[a[i+1]]
                if(parType2==1):
                    par2=a[i+2]
                else:
                    par2=a[a[i+2]]
                if(par1<par2):
                    par3=1
                else:
                    par3=0
                if(parType3==1):
                    a[i+3]=par3
                else:
                    a[a[i+3]]=par3
                i=i+4
            elif eq(a[i]):
                if(parType1==1):
                    par1=a[i+1]
                else:
                    par1=a[a[i+1]]
                if(parType2==1):
                    par2=a[i+2]
                else:
                    par2=a[a[i+2]]
                if(par1==par2):
                    par3=1
                else:
                    par3=0
                if(parType3==1):
                    a[i+3]=par3
                else:
                    a[a[i+3]]=par3
                i=i+4
        else:
            if (a[i]==1):
                print(a[i],a[i+1],a[i+2])
                b=int(a[int(a[i+1])])+int(a[int(a[i+2])])
                a[int(a[i+3])]=b
            # print(b)
                i=i+4
            elif (a[i]==2):
                b=int(a[int(a[i+1])])*int(a[int(a[i+2])])
                a[int(a[i+3])]=b
            # print(b)
                i=i+4
            elif(a[i]==3):
                x=param
                a[int(a[i+1])]=x
                i=i+2
            elif(a[i]==4):
                res= (a[int(a[i+1])])
                if output==0:
                    output=1
                    final=[res]
                    i+=2
                elif output==1:
                    final.append(res)
                    final.append(i)
                    final.append(a)
                    output=0
                    return final
            elif(a[i]==5):
                if(a[a[i+1]]!=0):
                    i=a[a[i+2]]
                else:
                    i=i+3
            elif(a[i]==6):
                if(a[a[i+1]]==0):
                    i=a[a[i+2]]
                else:
                    i=i+3
            elif(a[i]==7):
                if(a[a[i+1]]<a[a[i+2]]):
                    a[a[i+3]]=1
                else:
                    a[a[i+3]]=0
                i=i+4
            elif(a[i]==8):
                if(a[a[i+1]]==a[a[i+2]]):
                    a[a[i+3]]=1
                else:
                    a[a[i+3]]=0
                i=i+4
    return 'ended'

class Face:
    
    def __init__(self, currentFace,position):
        self.currentFace = currentFace
        self.position=position
        
    def turn(self,turnDirection):
        direction=['up','left','down','right']
        s=direction.index(self.currentFace)
        if turnDirection==0:
            if s==3:
                s=1
            else:
                s+=1
        elif turnDirection==1:
            if s==0:
                s=3
            else:
                s==1
        self.currentFace=direction[s]
    
    def move(self):
        if self.currentFace=='up':
            self.position[1]+=1
        elif self.currentFace=='left':
            self.position[0]-=1
        elif self.currentFace=='down':
            self.position[1]-=1
        elif self.currentFace=='right':
            self.position[0]+=1
    def getTicker(self):
        if self.currentFace=='up':
            return'^'
        elif self.currentFace=='left':
            return '<'
        elif self.currentFace=='down':
            return 'v'
        elif self.currentFace=='right':
            return '>'


#Step1:initiate robot
robot=Face('up',[10,10])
#l[(robot.position[0],robot.position[1])]=robot.getTicker()
#printmap(l)
currentPosition=(robot.position[0],robot.position[1])
currentColor=l[currentPosition]
#Step2: Feed input based on current position
running=100
i=0
inputProgram=master
painted={}
while(running>0):
    
    if currentColor=='.':
        inputParam=0
    elif currentColor=='#':
        inputParam=1
    result=amplifier(inputProgram,inputParam,i)
    inputProgram=result[3]
    i=result[2]
    print(result[:3])
    if(result=='ended'):
        break
    setColor='#' if result[0]==1 else '.'

    #Step3: Turn Robot
    turningDirection=result[1]
    robot.turn(turningDirection)

    #Step4: Color last position with output and Move Robot 
    l[currentPosition]=setColor
    if currentPosition  in painted:
        painted[currentPosition]+=1
    else:
        painted[currentPosition]=1
    robot.move()
    currentPosition=(robot.position[0],robot.position[1])
    currentColor=l[currentPosition]
    running-=1

#Step 5: Print map
l[currentPosition]=robot.getTicker()
printmap(l)
print(painted)



#1.Take a list as input
#2.Read first char (pointer)
#3.Based on char, perform operation
#4.Move pointer
#5.If char is 99, stop.
#6.If char is 4, output next char. Move pointer
#7.

