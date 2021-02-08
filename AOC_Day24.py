import math

start=[
['B','B','.','.','.'],
['B','.','B','B','B'],
['.','B','.','B','.'],
['B','.','.','.','.'],
['.','.','B','B','B']
]

#21211
#14131
#30312
#02121
#11121

#.BBBB
#B.B.B
#...BB
#.BBBB
#BBB.B

def setSpace(field, scoreField):
        if field==0:
            if scoreField>0 and scoreField<3:
                field=1
        else:
            if scoreField!=1:
                field=0
        return field

class BugGeneration:
    #1 for bug, 0 for empty
    a11=a12=a13=a14=a15=a21=a22=a23=a24=a25=a31=a32=a33=a34=a35=a41=a42=a43=a44=a45=a51=a52=a53=a54=a55=0

    def nextGeneration(self):
        #a11
        score11=self.a12+self.a21
        #a12
        score12=self.a11+self.a13+self.a22
        #a13
        score13=self.a12+self.a14+self.a23
        #a14
        score14=self.a13+self.a15+self.a24
        #a15
        score15=self.a14+self.a25
        #a21
        score21=self.a11+self.a22+self.a31
        #a22
        score22=self.a12+self.a21+self.a21+self.a32
        #a23
        score23=self.a13+self.a22+self.a24+self.a33
        #a24
        score24=self.a14+self.a23+self.a25+self.a34
        #a25
        score25=self.a15+self.a24+self.a35
        #a31
        score31=self.a21+self.a32+self.a41
        #a32
        score32=self.a22+self.a31+self.a33+self.a42
        #a33
        score33=self.a23+self.a32+self.a34+self.a43
        #a34
        score34=self.a24+self.a35+self.a44+self.a33
        #a35
        score35=self.a25+self.a34+self.a45
        #a41
        score41=self.a31+self.a42+self.a51
        #a42
        score42=self.a32+self.a41+self.a43+self.a52
        #a43
        score43=self.a33+self.a42+self.a44+self.a53
        #a44
        score44=self.a34+self.a45+self.a54+self.a43
        #a45
        score45=self.a35+self.a44+self.a55
        #a51
        score51=self.a52+self.a41
        #a52
        score52=self.a51+self.a53+self.a42
        #a53
        score53=self.a52+self.a54+self.a43
        #a54
        score54=self.a53+self.a55+self.a44
        #a55
        score55=self.a54+self.a45

        self.a11=setSpace(self.a11,score11)
        self.a12=setSpace(self.a12,score12)
        self.a13=setSpace(self.a13,score13)
        self.a14=setSpace(self.a14,score14)
        self.a15=setSpace(self.a15,score15)
        self.a21=setSpace(self.a21,score21)
        self.a22=setSpace(self.a22,score22)
        self.a23=setSpace(self.a23,score23)
        self.a24=setSpace(self.a24,score24)
        self.a25=setSpace(self.a25,score25)
        self.a31=setSpace(self.a31,score31)
        self.a32=setSpace(self.a32,score32)
        self.a33=setSpace(self.a33,score33)
        self.a34=setSpace(self.a34,score34)
        self.a35=setSpace(self.a35,score35)
        self.a41=setSpace(self.a41,score41)
        self.a42=setSpace(self.a42,score42)
        self.a43=setSpace(self.a43,score43)
        self.a44=setSpace(self.a44,score44)
        self.a45=setSpace(self.a45,score45)
        self.a51=setSpace(self.a51,score51)
        self.a52=setSpace(self.a52,score52)
        self.a53=setSpace(self.a53,score53)
        self.a54=setSpace(self.a54,score54)
        self.a55=setSpace(self.a55,score55)

    def printGeneration(self):
        print(self.a11,self.a12,self.a13,self.a14,self.a15)
        print(self.a21,self.a22,self.a23,self.a24,self.a25)
        print(self.a31,self.a32,self.a33,self.a34,self.a35)
        print(self.a41,self.a42,self.a43,self.a44,self.a45)
        print(self.a51,self.a52,self.a53,self.a54,self.a55)

    def calculateRating(self):
        rating= (self.a11*1+
        self.a12*2+
        self.a13*4+
        self.a14*8+
        self.a15*16+
        self.a21*32+
        self.a22*64+
        self.a23*128+
        self.a24*256+
        self.a25*512+
        self.a31*1024+
        self.a32*math.pow(2,11)+
        self.a33*math.pow(2,12)+
        self.a34*math.pow(2,13)+
        self.a35*math.pow(2,14)+
        self.a41*math.pow(2,15)+
        self.a42*math.pow(2,16)+
        self.a43*math.pow(2,17)+
        self.a44*math.pow(2,18)+
        self.a45*math.pow(2,19)+
        self.a51*math.pow(2,20)+
        self.a52*math.pow(2,21)+
        self.a53*math.pow(2,22)+
        self.a54*math.pow(2,23)+
        self.a55*math.pow(2,24))
        return int(rating)

g1=BugGeneration()
g1.a11=1
g1.a12=1
g1.a21=1
g1.a23=1
g1.a24=1
g1.a25=1
g1.a32=1
g1.a34=1
g1.a41=1
g1.a53=1
g1.a54=1
g1.a55=1
i=1
scoreHistory={g1.calculateRating():i}

g1.nextGeneration()
while(g1.calculateRating() not in scoreHistory):
    i+=1
    scoreHistory[g1.calculateRating()]=i
    g1.nextGeneration()

g1.printGeneration()
print(scoreHistory)
print(g1.calculateRating())
