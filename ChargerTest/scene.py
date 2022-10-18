import string
from read import meta_data


# 确定是充电还是放电
# 充电的行数多于放电的行数时，判断为充电，反之为放电
# 参数：file_path  文件路径
def whether_charge_or_discharge(file_path:string):
    origin_data=meta_data(file_path)
    j,k=0,0
    for i in range(0,len(origin_data['DATE'])):
        if origin_data['STATUS'][i]=='Charging':
            j+=1
        elif origin_data['STATUS'][i]=='Discharging':
            k+=1
    if j>k:
        # print('充电测试')
        return 'Charging'
    else:
        # print('放电测试')
        return 'Discharging'
    
# 确定在什么温度下进行了测试
def which_temp(file_path:string):
    max_temp,min_temp=[],[]
    a,b,c,d,e,f,g,h=0,0,0,0,0,0,0,0
    origin_data=meta_data(file_path)
    data_length=len(origin_data['DATE'])-1
    max_temp=origin_data['TEMP'].max()
    min_temp=origin_data['TEMP'].min()
    
    # 遍历所有温度区间内记录的个数
    for i in range(0,data_length+1):
        if origin_data['TEMP'][i]>=-15 and origin_data['TEMP'][i]<-10:
            a+=1
        elif origin_data['TEMP'][i]>=-10 and origin_data['TEMP'][i]<0:
            b+=1
        elif origin_data['TEMP'][i]>=0 and origin_data['TEMP'][i]<5:
            c+=1
        elif origin_data['TEMP'][i]>=5 and origin_data['TEMP'][i]<10:
            d+=1
        elif origin_data['TEMP'][i]>=10 and origin_data['TEMP'][i]<15:
            e+=1
        elif origin_data['TEMP'][i]>=15 and origin_data['TEMP'][i]<35:
            f+=1
        elif origin_data['TEMP'][i]>=35 and origin_data['TEMP'][i]<48:
            g+=1
        elif origin_data['TEMP'][i]>=48 and origin_data['TEMP'][i]<60:
            h+=1
    
    # 温度区间判断
    if f+g==data_length+1 and max_temp<48 and origin_data['TEMP'][data_length]<35:
        # print('15-35度')
        return 'normal-25'
    elif f+g+h==data_length+1 and g*2>f+h and origin_data['TEMP'][data_length]<48:
        # print('35-48度')
        return 'normal-35'
    elif f+g+h==data_length+1 and origin_data['TEMP'][data_length]<45 and max_temp>50:
        # print('高温回归常温')
        return 'hot-back'
    elif f+g+h==data_length+1 and origin_data['TEMP'][data_length]>48 and max_temp>50:
        # print('高温')
        return 'hot'
    elif a+b+c+d+e+f==data_length+1 and min_temp<-10:
        # print('-15~-10度')
        return 'cold--15'
    elif a+b+c+d+e+f==data_length+1 and min_temp<0 and min_temp>=-10:
        # print('-10~0度')
        return 'cold--10'
    elif b+c+d+e+f==data_length+1 and min_temp<5 and min_temp>=0 and c+d>b+e+f and origin_data['TEMP'][data_length]<5:
        # print('0-5度')
        return 'cold-0'
    elif c+d+e+f==data_length+1 and min_temp<10 and min_temp>=5 and d>c+e+f and origin_data['TEMP'][data_length]<10:
        # print('5-10度')
        return 'cold-5'
    elif d+e+f==data_length+1 and min_temp<15 and min_temp>=10 and e>d+f and origin_data['TEMP'][data_length]<15:
        # print('10-15度')
        return 'cold-10'
    elif b+c+d+e+f+g==data_length+1 and min_temp<0 and max_temp>35 and origin_data['TEMP'][data_length]>25:
        # print('低温回归常温')
        return 'cold-back'
    
# 确认充电类型
def which_type(file_path:string):
    origin_data=meta_data(file_path)
    a,b,c,d,e=0,0,0,0,0
    for i in range(0,len(origin_data['DATE'])):
        if origin_data['TYPE'][i]=='USB_PD':
            a+=1
        elif origin_data['TYPE'][i]=='USB_HVDCP':
            b+=1
        elif origin_data['TYPE'][i]=='USB_CDP':
            c+=1
        elif origin_data['TYPE'][i]=='USB_DCP':
            d+=1
        elif origin_data['TYPE'][i]=='USB':
            e+=1
        
    if a>b+c+d+e:
        # print('充电类型是:USB_PD')
        return 'USB_PD'
    elif b>a+c+d+e:
        # print('充电类型是:USB_HVDCP')
        return 'USB_HVDCP'
    elif c>a+b+d+e:
        # print('充电类型是:USB_CDP')
        return 'USB_CDP'
    elif d>a+b+c+e:
        # print('充电类型是:USB_DCP')
        return 'USB_DCP'
    elif e>a+b+c+d:
        # print('充电类型是:USB')
        return 'USB'
    
# 确认电池厂家
def which_battery(file_path:string):
    origin_data=meta_data(file_path)
    a,b=0,0
    for i in range(0,len(origin_data['DATE'])):
        if origin_data['Battery_Name'][i]=='S88006_SWD_4V45_5000mAh':
            a+=1
        elif origin_data['Battery_Name'][i]=='S88006_NVT_4V45_5000mAh':
            b+=1
    if a==len(origin_data['DATE']):
        return 'SWD-5000mAh'
    elif b==len(origin_data['DATE']):
        return 'NVT-5000mAh'
