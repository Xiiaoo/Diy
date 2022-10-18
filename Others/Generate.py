import random
import pandas as pd

listA=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
listB=[1,2,3,4,5,6,7,8,9,10,11,12]
ini=[11,13,17,19,25,2,9]
listC=[]
listD=[]
x=0

newdata=pd.DataFrame(columns=['IndexZero',
                              'IndexOne',
                              'IndexTwo',
                              'IndexThree',
                              'IndexFour',
                              'IndexFive',
                              'IndexSix',
                              'CountA',
                              'CountB',
                              'Award',
                              'Prize'
                              ])


for i in range(5):

    # m[1,35]  
    # len(listA)=35
    # listA[34]=35
    # m是listA的索引
    m = random.randint(0, len(listA)-1)

    # listA的第m个索引加入到listC中
    listC.append(listA[m])

    # 删除listA中已随机元素
    for k in listA:
        if listA[m]==k:
            listA.remove(listA[m])
    listC.sort()

for i in range(2):
    n = random.randint(0, len(listB)-1)
    listD.append(listB[n])

    for k in listB:
        if listB[n]==k:
                listB.remove(listB[n])
    listD.sort()

listE=listC+listD

y=0

# while listE != ini:
# 循环10000次
while y<10000:
    listA=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    listB=[1,2,3,4,5,6,7,8,9,10,11,12]
    listC=[]
    listD=[]
    award=0
    prize=0
    countA=0
    countB=0
    x+=1
    for i in range(5):
        m = random.randint(0, len(listA)-1)
        listC.append(listA[m])

        for k in listA:
            if listA[m]==k:
                listA.remove(listA[m])
        listC.sort()

    for i in range(2):
        n = random.randint(0, len(listB)-1)
        listD.append(listB[n])

        for k in listB:
            if listB[n]==k:
                listB.remove(listB[n])
        listD.sort()

    listE=listC+listD

    for i in range(0,len(listC)):
        for j in range(5):
            if listC[i]==ini[j]:
                countA+=1

    for i in range(0,len(listD)):
        for j in range(5,7):
            if listD[i]==ini[j]:
                countB+=1
    if listE==ini:
        break

    if   countA==0 and countB==2:
        award=9
        prize=5
    elif countA==1 and countB==2:
        award=9
        prize=5
    elif countA==2 and countB==1:
        award=9
        prize=5
    elif countA==3 and countB==0:
        award=9
        prize=5
    elif countA==2 and countB==2:
        award=8
        prize=15
    elif countA==3 and countB==1:
        award=8
        prize=15
    elif countA==4 and countB==0:
        award=7
        prize=100
    elif countA==3 and countB==2:
        award=6
        prize=200
    elif countA==4 and countB==1:
        award=5
        prize=300
    elif countA==4 and countB==2:
        award=4
        prize=3000
    elif countA==5 and countB==0:
        award=3
        prize=10000
    elif countA==5 and countB==1:
        award=2
        prize=100000
    elif countA==5 and countB==2:
        award=1
        prize=10000000
    else:
        award=10
        prize=0

    print(x,listE,countA,countB,award,prize)
    newdata.loc[y]=[listE[0],listE[1],listE[2],listE[3],listE[4],listE[5],listE[6],countA,countB,award,prize]

    y+=1


newdata.to_excel(
    excel_writer='D:\\Letto4.xlsx',
    sheet_name='Sheet1',
    index=False
)

writer=pd.ExcelWriter('D:\\Letto5.xlsx')
newdata.to_excel(writer)
writer.save