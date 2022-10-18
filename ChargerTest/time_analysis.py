import string
import filter as fil

def analysis(file_path:string):
    data=fil.data_output(file_path)
    min,sec=[],[]
    length=len(data['TIME'])
    origin_time=data.TIME[0]
    for i in range(0,length):
        min.append((data.TIME[i]-origin_time)//60)
        sec.append((data.TIME[i]-origin_time)%60)

    # 5min soc
    def time_soc(MIN:int,SEC:int):
        print('起始电量: '+str(data.SOC[0])+'%')
        print('起始温度: '+str(data.TEMP[0])+'℃')
        print('起始电压: '+str(data.VOLTAGE_NOW[0])+'V')
        if data.SOC[0]<=1:
            print('Perfect')
        elif data.SOC[0]>1 and data.SOC[0]<=3:
            print('数据有较小偏差')
        elif data.SOC[0]>5:
            print('数据偏差较大')
        for i in range(0,length):
            if min[i]==MIN and sec[i]==SEC:
                print(' '+str(MIN)+'min SOC: '+str(data.SOC[i]))
            elif min[i]==MIN+5 and sec[i]==SEC:
                print(str(MIN+5)+'min SOC: '+str(data.SOC[i]))
            elif min[i]==MIN+10 and sec[i]==SEC:
                print(str(MIN+10)+'min SOC: '+str(data.SOC[i]))
            elif min[i]==MIN+15 and sec[i]==SEC:
                print(str(MIN+15)+'min SOC: '+str(data.SOC[i]))
            elif min[i]==MIN+20 and sec[i]==SEC:
                print(str(MIN+20)+'min SOC: '+str(data.SOC[i]))
            elif min[i]==MIN+25 and sec[i]==SEC:
                print(str(MIN+25)+'min SOC: '+str(data.SOC[i]))
            elif min[i]==MIN+30 and sec[i]==SEC:
                print(str(MIN+30)+'min SOC: '+str(data.SOC[i]))
            elif min[i]==MIN+35 and sec[i]==SEC:
                print(str(MIN+35)+'min SOC: '+str(data.SOC[i]))
            elif min[i]==MIN+40 and sec[i]==SEC:
                print(str(MIN+40)+'min SOC: '+str(data.SOC[i])+' STATUS: '+data.STATUS[i])
            elif min[i]==MIN+45 and sec[i]==SEC:
                print(str(MIN+45)+'min SOC: '+str(data.SOC[i])+' STATUS: '+data.STATUS[i])
            elif min[i]==MIN+50 and sec[i]==SEC:
                print(str(MIN+50)+'min SOC: '+str(data.SOC[i])+' STATUS: '+data.STATUS[i])
            elif min[i]==MIN+55 and sec[i]==SEC:
                print(str(MIN+55)+'min SOC: '+str(data.SOC[i])+' STATUS: '+data.STATUS[i])
            elif min[i]==MIN+60 and sec[i]==SEC:
                print(str(MIN+60)+'min SOC: '+str(data.SOC[i])+' STATUS: '+data.STATUS[i])
            elif min[i]==MIN+65 and sec[i]==SEC:
                print(str(MIN+65)+'min SOC: '+str(data.SOC[i])+' STATUS: '+data.STATUS[i])
            elif min[i]==MIN+70 and sec[i]==SEC:
                print(str(MIN+70)+'min SOC: '+str(data.SOC[i])+' STATUS: '+data.STATUS[i])
            elif min[i]==MIN+75 and sec[i]==SEC:
                print(str(MIN+75)+'min SOC: '+str(data.SOC[i])+' STATUS: '+data.STATUS[i])
            elif min[i]==MIN+85 and sec[i]==SEC:
                print(str(MIN+85)+'min SOC: '+str(data.SOC[i])+' STATUS: '+data.STATUS[i])
            elif min[i]==MIN+175 and sec[i]==SEC:
                print('3h SOC: '+str(data.SOC[i])+' STATUS: '+data.STATUS[i])
            elif min[i]==MIN+235 and sec[i]==SEC:
                print('4h SOC: '+str(data.SOC[i])+' STATUS: '+data.STATUS[i])


    def soc_time(SOC:int):
        for i in range(1,length):
            if data.SOC[i]==SOC and data.SOC[i-1]==SOC-1:
                print(' '+str(SOC)+'% 充电时长: '+str(min[i])+'min '+str(sec[i])+'s')
            elif data.SOC[i]==SOC+5 and data.SOC[i-1]==SOC+4:
                print(str(SOC+5)+'% 充电时长: '+str(min[i])+'min '+str(sec[i])+'s')
            elif data.SOC[i]==SOC+15 and data.SOC[i-1]==SOC+14:
                print(str(SOC+15)+'% 充电时长: '+str(min[i])+'min '+str(sec[i])+'s')
            elif data.SOC[i]==SOC+25 and data.SOC[i-1]==SOC+24:
                print(str(SOC+25)+'% 充电时长: '+str(min[i])+'min '+str(sec[i])+'s')
            elif data.SOC[i]==SOC+35 and data.SOC[i-1]==SOC+34:
                print(str(SOC+35)+'% 充电时长: '+str(min[i])+'min '+str(sec[i])+'s')
            elif data.SOC[i]==SOC+45 and data.SOC[i-1]==SOC+44:
                print(str(SOC+45)+'% 充电时长: '+str(min[i])+'min '+str(sec[i])+'s')
            elif data.SOC[i]==SOC+55 and data.SOC[i-1]==SOC+54:
                print(str(SOC+55)+'% 充电时长: '+str(min[i])+'min '+str(sec[i])+'s')
            elif data.SOC[i]==SOC+65 and data.SOC[i-1]==SOC+64:
                print(str(SOC+65)+'% 充电时长: '+str(min[i])+'min '+str(sec[i])+'s')
            elif data.SOC[i]==SOC+75 and data.SOC[i-1]==SOC+74:
                print(str(SOC+75)+'% 充电时长: '+str(min[i])+'min '+str(sec[i])+'s')
            elif data.SOC[i]==SOC+85 and data.SOC[i-1]==SOC+84:
                print(str(SOC+85)+'% 充电时长: '+str(min[i])+'min '+str(sec[i])+'s')
            elif data.SOC[i]==100 and data.STATUS[i]=='Charging' and data.SOC[i-1]==SOC+94:
                print('100% 充电时长: '+str(min[i+1])+'min '+str(sec[i+1])+'s')
            elif data.SOC[i]==100 and data.STATUS[i]=='Full' and data.STATUS[i-1]=='Charging':
                print('FULL'+' 充电时长: '+str(min[i])+'min '+str(sec[i])+'s  截止电压：'+str(data.VOLTAGE_NOW[i-3])+'V  截止电流：'+str(data.CURRENT_NOW[i-3])+'mA')


    time_soc(5,0)
    soc_time(5)