import datetime
from time import sleep
from urllib import response
import requests
import pandas as pd

kw={'r':0.39235985639499993}

for x in range(1):
    consume,starttime,endtime,hour,day,month=[],[],[],[],[],[]
    DATE,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE,TEN,ELEVEN,TWELVE,THIRTEEN,FOURTEEN,FIFTEEN,SIXTEEN,SEVENTEEN,EIGHTEEN,NINETEEN,TWENTY,TWENTY_ONE,TWENTY_TWO,TWENTY_THREE,TWENTY_FOUR=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    consume0,hour0,day0,month0,DATE0=[],[],[],[],[]
    consume1,hour1,day1,month1,DATE1=[],[],[],[],[]
    response=requests.request("get",'http://sl-api.oray.com/smartplug/powerconsumes/172828683435')
    data=response.json()

    latest_hour=int(datetime.datetime.fromtimestamp(data[0]['endtime']+60).strftime("%H"))
    latest_day=int(datetime.datetime.fromtimestamp(data[0]['endtime']+60).strftime("%d"))
    latest_month=int(datetime.datetime.fromtimestamp(data[0]['endtime']+60).strftime("%m"))
    print(latest_hour)



    for i in range(0,24-latest_hour):
        consume0.append('Null')
        hour0.append(23-i)
        day0.append(latest_day)
        month0.append(latest_month)
        DATE0.append(str(month0[i-1])+'-'+str(day0[i-1]))

    for i in range(0,latest_hour+24*5):
        consume1.append(data[i]['consume'])
        hour1.append(int(datetime.datetime.fromtimestamp(data[i]['starttime']).strftime("%H")))
        day1.append(int(datetime.datetime.fromtimestamp(data[i]['starttime']).strftime("%d")))
        month1.append(int(datetime.datetime.fromtimestamp(data[i]['starttime']).strftime("%m")))
        DATE1.append(str(month1[i])+'-'+str(day1[i]))

    consume=consume0+consume1
    hour=hour0+hour1
    day=day0+day1
    month=month0+month1
    DATE=DATE0+DATE1

    for i in range(0,len(consume)):
        if hour[i]==0:
            ONE.append(consume[i])
        elif hour[i]==1:
            TWO.append(consume[i])
        elif hour[i]==2:
            THREE.append(consume[i])
        elif hour[i]==3:
            FOUR.append(consume[i])
        elif hour[i]==4:
            FIVE.append(consume[i])
        elif hour[i]==5:
            SIX.append(consume[i])
        elif hour[i]==6:
            SEVEN.append(consume[i])
        elif hour[i]==7:
            EIGHT.append(consume[i])
        elif hour[i]==8:
            NINE.append(consume[i])
        elif hour[i]==9:
            TEN.append(consume[i])
        elif hour[i]==10:
            ELEVEN.append(consume[i])
        elif hour[i]==11:
            TWELVE.append(consume[i])
        elif hour[i]==12:
            THIRTEEN.append(consume[i])
        elif hour[i]==13:
            FOURTEEN.append(consume[i])
        elif hour[i]==14:
            FIFTEEN.append(consume[i])
        elif hour[i]==15:
            SIXTEEN.append(consume[i])
        elif hour[i]==16:
            SEVENTEEN.append(consume[i])
        elif hour[i]==17:
            EIGHTEEN.append(consume[i])
        elif hour[i]==18:
            NINETEEN.append(consume[i])
        elif hour[i]==19:
            TWENTY.append(consume[i])
        elif hour[i]==20:
            TWENTY_ONE.append(consume[i])
        elif hour[i]==21:
            TWENTY_TWO.append(consume[i])
        elif hour[i]==22:
            TWENTY_THREE.append(consume[i])
        elif hour[i]==23:
            TWENTY_FOUR.append(consume[i])
        else:
            pass
        if i==len(consume)-1:
            print(datetime.datetime.fromtimestamp(data[i]['endtime']+60).strftime("%Y-%m-%d %H:%M:%S"))

    DATE2=[]
    for i in DATE:
        if i not in DATE2:
            DATE2.append(i)

    df=pd.DataFrame({
        'DATE':DATE2,
        '0:00-1:00': ONE ,
        '1:00-2:00': TWO,
        '2:00-3:00': THREE,
        '3:00-4:00': FOUR,
        '4:00-5:00': FIVE,
        '5:00-6:00': SIX,
        '6:00-7:00': SEVEN,
        '7:00-8:00': EIGHT,
        '8:00-9:00': NINE,
        '9:00-10:00': TEN,
        '10:00-11:00': ELEVEN,
        '11:00-12:00': TWELVE,
        '12:00-13:00': THIRTEEN,
        '13:00-14:00': FOURTEEN,
        '14:00-15:00': FIFTEEN,
        '15:00-16:00': SIXTEEN,
        '16:00-17:00': SEVENTEEN,
        '17:00-18:00': EIGHTEEN,
        '18:00-19:00': NINETEEN,
        '19:00-20:00': TWENTY,
        '20:00-21:00': TWENTY_ONE,
        '21:00-22:00': TWENTY_TWO,
        '22:00-23:00': TWENTY_THREE,
        '23:00-0:00': TWENTY_FOUR,
    })

    print(df)
    df.to_excel(
        excel_writer='用电统计'+'.xlsx',
        sheet_name='data',
        index=False
    )

    sleep(5)