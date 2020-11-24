import itertools

master=[3,8,1001,8,10,8,105,1,0,0,21,34,51,64,73,98,179,260,341,422,99999,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,1001,9,4,9,1002,9,3,9,1001,9,5,9,4,9,99,3,9,101,5,9,9,102,5,9,9,4,9,99,3,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,1001,9,3,9,102,2,9,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]

a=master

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

def increment(nextDigit):
    if nextDigit==4:
        nextDigit=0
    else:
        nextDigit+=1
    return nextDigit

def amplifier(nextD,x1,x2):
    output=0
    input1=True
    i=0
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
                    output=a[i+1]
                    nextD=increment(nextD)
                    print(output)
                    amplifier(nextD,x1,output)
                    #return(a[i+1])
                else:
                    output=a[a[i+1]]
                    nextD=increment(nextD)
                    print(output)
                    amplifier(nextD,x1,output)
                    #return(a[a[i+1]])
                i=i+2
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
                if(input1):
                    x=x1[nextD]
                else:
                    x=x2
                a[int(a[i+1])]=x
                i=i+2
                input1=False
            elif(a[i]==4):
                output= a[int(a[i+1])]
                nextD=increment(nextD)
                print(output)
                amplifier(nextD,x1,output)
                #return(a[int(a[i+1])])
                i=i+2
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
    return output
            
# def a1(d1,d2,d3,d4,d5):
#     start=True
#     running=True
#     result5=0
#     while(running):
#         if(start):
#             result1=amplifier(d1,0)
#             start=False
#         else:
#             result1=amplifier(d1,result5)
#             result2=amplifier(d2,result1)
#             result3=amplifier(d3,result2)
#             result4=amplifier(d4,result3)
#             result5=amplifier(d5,result4)
#             if(result5==-1):
#                 running =False
#     return result5

    
    

possibleDigits=[5,6,7,8,9]
l1=set(itertools.permutations(possibleDigits))
d={}
for item in l1:
    d[item]=0

for item in d:
    # digit1=item[0]
    # digit2=item[1]
    # digit3=item[2]
    # digit4=item[3]
    # digit5=item[4]

    result = amplifier(0,item,0)
    d[item]=result

highest=0
for item in d:
    if(d[item]>highest):
        highest=d[item]

print(highest)