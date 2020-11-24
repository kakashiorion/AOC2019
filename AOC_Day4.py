low = 153517
high = 630395
count = 0

for k in range(low,high):
    digits = [int(x) for x in str(k)]
    increasing = True
    repeating = False
    meetsCriteria=False
    f={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

    for i in range(len(digits)-1):
        if (digits[i]>digits[i+1]):
            increasing=False
        if (digits[i]==digits[i+1]):
            repeating =True
            f[digits[i]]+=1
    
    for j in range(0,10):
        if (f[j]==1):
            meetsCriteria=True

    if (increasing and repeating and meetsCriteria):
        count+=1

print(count)
