import pandas as pd

filePath='D:\\Letto.xlsx'
data=pd.read_excel(filePath)

rowList1=[]
rowList2=[]
listA=[]
listB=[]
listC=[]
listD=[]
listE=[]
listF=[]
listG=[]
listH=[]
listI=[]
CountA=[]
CountB=[]
MinusOne=[]
MinusTwo=[]
MedianSeventeen=[]
Odd1Count=[]
Odd2Count=[]
x=y=0
z=1

for i in range(len(data.IndexZero)):
    listA.append(data.IndexZero[i])
    listB.append(data.IndexOne[i])
    listC.append(data.IndexTwo[i])
    listD.append(data.IndexThree[i])
    listE.append(data.IndexFour[i])
    listF.append(data.IndexFive[i])
    listG.append(data.IndexSix[i])
    rowList1=[listA[i],listB[i],listC[i],listD[i],listE[i]]
    rowList2=[listF[i],listG[i]]
    for m in range(5):
        if rowList1[m]%2==1:
            x=x+1
        else:
            pass
    for n in range(2):
        if rowList2[n]%2==1:
            y=y+1
        else:
            pass
    listH.append(data.FirstPrize[i])
    listI.append(data.SecondPrize[i])
    CountA.append(data.IndexZero[i]+data.IndexOne[i]+data.IndexTwo[i]+data.IndexThree[i]+data.IndexFour[i])
    CountB.append(data.IndexFive[i]+data.IndexSix[i])
    MinusOne.append(data.IndexFour[i]-data.IndexZero[i])
    MinusTwo.append(data.IndexSix[i]-data.IndexFive[i])
    if listC[i]==17:
        MedianSeventeen.append('Yes')
    else:
        MedianSeventeen.append('No')
    Odd1Count.append(x)
    Odd2Count.append(y)
    x=y=0

newdata=pd.DataFrame(
    {
        'IndexZero':listA,
        'IndexOne':listB,
        'IndexTwo':listC,
        'IndexThree':listD,
        'IndexFour':listE,
        'IndexFive':listF,
        'IndexSix':listG,
        'FirstPrize':listH,
        'SecondPrize':listI,
        'CountA':CountA,
        'CountB':CountB,
        'MinusOne':MinusOne,
        'MinusTwo':MinusTwo,
        'MedianSeventeen':MedianSeventeen,
        'Odd1Count':Odd1Count,
        'Odd2Count':Odd2Count
    }
)

newdata.to_excel(
    excel_writer='D:\\Letto2.xlsx',
    sheet_name='Sheet1',
    index=False
)

writer=pd.ExcelWriter('D:\\Letto3.xlsx')
newdata.to_excel(writer)
writer.save