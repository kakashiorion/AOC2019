r=['2 LGNW, 1 FKHJ => 3 KCRD',
'5 FVXTS => 5 VSVK',
'1 RBTG => 8 FKHJ',
'2 TLXRM, 1 VWJSD => 8 CDGX',
'1 MVSL, 2 PZDR, 9 CHJRF => 8 CLMZ',
'11 BMSFK => 5 JMSWX',
'10 XRMC => 1 MQLFC',
'20 ZPWQB, 1 SBJTD, 9 LWZXV => 4 JFZNR',
'2 FVXTS => 3 FBHT',
'10 ZPWQB => 8 LGNW',
'5 WBDGL, 16 KZHQ => 2 FVXTS',
'124 ORE => 7 BXFVM',
'5 KCRD => 1 RNVMC',
'5 CGPZC, 4 WJCT, 1 PQXV => 8 VKQXP',
'4 KFVH => 4 FGTKD',
'11 QWQG => 6 LWZXV',
'9 ZMZPB, 8 KFVH, 5 FNPRJ => 3 VKVP',
'1 LFQW, 8 PQXV, 2 TLXRM, 1 VKQXP, 1 BMSFK, 1 QKJPV, 3 JZCFD, 8 VWJSD => 6 WXBC',
'2 SLDWK, 32 JZCFD, 10 RNVMC, 1 FVXTS, 34 LGTX, 1 NTPZK, 1 VKQXP, 1 QTKL => 9 LDZV',
'31 FBHT => 2 BMSFK',
'35 KZHQ, 3 ZPWQB => 3 PCNVM',
'6 DRSG, 1 TDRK, 1 VSVK => 2 VWJSD',
'3 DGMH => 3 ZPWQB',
'162 ORE => 9 RBTG',
'11 LFQW, 1 LPQCK => 8 LGTX',
'8 MQLFC => 1 SBJTD',
'1 KGTB => 9 TGNB',
'1 BXFVM, 1 ZMZPB => 8 FNPRJ',
'1 PCNVM, 15 ZSZBQ => 4 PQXV',
'15 XRMC => 9 ZSZBQ',
'18 VWJSD, 12 CHJRF => 6 KTPH',
'8 RBTG, 5 ZMZPB => 6 KFVH',
'6 SLDWK => 1 XVTRS',
'3 VSVK, 6 BMSFK, 3 NTPZK => 1 JZCFD',
'3 FVXTS, 2 MTMKN => 5 CHJRF',
'9 FNPRJ => 2 QWQG',
'1 FBHT, 1 MVSL, 1 FNPRJ => 1 DRSG',
'35 LPQCK, 19 LWZXV, 28 LGNW => 5 TLXRM',
'5 NKMV => 3 QKJPV',
'3 MGZM, 2 TGNB => 8 PZDR',
'2 FKHJ => 2 WBDGL',
'1 NKMV => 1 KGTB',
'129 ORE => 7 ZMZPB',
'3 LMNQ, 2 BMSFK, 4 RNVMC, 4 KGTB, 4 DRSG, 2 JFZNR, 7 QTKL => 4 CKQZ',
'1 MQLFC => 7 MGZM',
'7 SLDWK, 2 KCRD => 4 WJCT',
'1 QKJPV => 4 LPQCK',
'1 JFZNR => 6 TDRK',
'4 CLMZ, 1 LGTX => 9 PMSZG',
'6 QWQG => 8 CGPZC',
'10 QWQG => 6 LMNQ',
'2 PMSZG, 1 VKVP => 3 QTKL',
'2 DGMH => 8 KZHQ',
'14 RBTG => 9 DGMH',
'62 RNVMC, 4 KTPH, 20 XVTRS, 7 JZCFD, 18 CDGX, 13 WXBC, 14 LDZV, 2 CKQZ, 33 FNPRJ => 1 FUEL',
'8 KGTB, 1 JMSWX => 7 NTPZK',
'1 VKVP, 7 DGMH => 7 NKMV',
'4 LPQCK => 5 MVSL',
'6 KGTB => 2 LFQW',
'2 FGTKD => 9 SLDWK',
'1 WBDGL, 1 ZMZPB, 1 DGMH => 6 XRMC',
'4 VKVP => 7 MTMKN']

#Store reactions as
#{(product_item,product_qty):[(reactant_item,reactant_qty)]}
reactions={}
for j in r:
    x=j.split("=>")
    
    product=x[1]
    y=product.split(" ")
    product_item=y[2]
    product_qty=int(y[1])
    product=(product_item,product_qty)

    z=x[0].split(",")
    reactants=[]
    for i in range(len(z)):
        y=z[i].split(" ")
        if i==0:
            reactant_qty=int(y[0])
            reactant_item=y[1]
        else:
            reactant_qty=int(y[1])
            reactant_item=y[2]
        item=(reactant_item,reactant_qty)
        reactants.append(item)
    reactions[product]=reactants

startingOre=1000000000000
inventory={'ORE':startingOre}
for v in reactions:
    w=v[0]
    inventory[w]=0

#print(inventory)
def getOre(item,qty):
    #global ore
    if(inventory[item]<qty):
        t=1
        for p in reactions:
            raw_mat=[]
            if p[0]==item:
                while((inventory[item]+p[1]*t)<qty):
                    t+=1
                raw_mat=reactions[p]
                for k in raw_mat:
                    if k[0]=='ORE':
                        inventory['ORE']-= (k[1]*t)
                    else:
                        getOre(k[0],k[1]*t)
                inventory[item]+=p[1]*t
    inventory[item]-=qty

#Part 1
getOre('FUEL',1)
print(inventory)
print(startingOre-int(inventory['ORE']))
#443537

#Part 2
count=0

while (inventory['ORE']>0):
    getOre('FUEL',1)
    count+=1

print(startingOre-int(inventory['ORE']))

