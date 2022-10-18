import string
from read import meta_data
import scene as sc


# filepath='D:\\Work\\K6S\\P2\\new-SOCdata.csv'


# 常温充电数据过滤器
def normal_charging_data_filter(file_path:string):
    origin_data=meta_data(file_path)
    true_type=sc.which_type(file_path)
    for i in range(0,len(origin_data['DATE'])):
        if origin_data['TYPE'][i]=='USB' or origin_data['TYPE'][i]=='Unknown' and origin_data['SOC'][i]<=3 :
            origin_data.drop([i],inplace=True)
        elif  origin_data['TYPE'][i] != true_type or origin_data['TYPE'][i]=='Unknown' and origin_data['SOC'][i]==100 :
            origin_data.drop([i],inplace=True)
        elif  origin_data['STATUS'][i]=='Charging' and origin_data['CURRENT_NOW'][i]<=0 and origin_data['SOC'][i]<=5:
            origin_data.drop([i],inplace=True)
    return origin_data.reset_index(drop=True)

# 高、低温回归充电数据过滤器
def back_charging_data_filter(file_path:string):
    origin_data=meta_data(file_path)
    true_type=sc.which_type(file_path)
    for i in range(0,len(origin_data['DATE'])):
        if origin_data['TYPE'][i]=='USB' or origin_data['TYPE'][i]=='Unknown' and origin_data['SOC'][i]<=10 :
            origin_data.drop([i],inplace=True)
        elif  origin_data['TYPE'][i] != true_type or origin_data['TYPE'][i]=='Unknown' and origin_data['SOC'][i]==100 :
            origin_data.drop([i],inplace=True)
        elif  origin_data['STATUS'][i]=='Charging' and origin_data['CURRENT_NOW'][i]<=0 and origin_data['SOC'][i]<=5:
            origin_data.drop([i],inplace=True)
    return origin_data.reset_index(drop=True)

# 低温充电数据过滤器
def cold_charging_data_filter(file_path:string):
    origin_data=meta_data(file_path)
    true_type=sc.which_type(file_path)
    for i in range(0,len(origin_data['DATE'])):
        if origin_data['TYPE'][i]=='USB' and origin_data['SOC'][i]<=10 or origin_data['TYPE'][i]=='Unknown' or origin_data['CURRENT_NOW'][i]<0:
            origin_data.drop([i],inplace=True)
        elif  origin_data['TYPE'][i] != true_type or origin_data['TYPE'][i]=='Unknown' and origin_data['SOC'][i]>=99 :
            origin_data.drop([i],inplace=True)
        elif  origin_data['STATUS'][i]=='Charging' and origin_data['CURRENT_NOW'][i]<=0 and origin_data['SOC'][i]<=5:
            origin_data.drop([i],inplace=True)
    return origin_data.reset_index(drop=True)

# 高温充电数据过滤器
def hot_charging_data_filter(file_path:string):
    origin_data=meta_data(file_path)
    true_type=sc.which_type(file_path)
    for i in range(0,len(origin_data['DATE'])):
        if origin_data['TYPE'][i]=='USB' or origin_data['TYPE'][i]=='Unknown' and origin_data['SOC'][i]<=10 :
            origin_data.drop([i],inplace=True)
        elif  origin_data['TYPE'][i] != true_type or origin_data['TYPE'][i]=='Unknown' and origin_data['SOC'][i]>=50 :
            origin_data.drop([i],inplace=True)
        elif  origin_data['STATUS'][i]=='Charging' and origin_data['CURRENT_NOW'][i]<=0 and origin_data['SOC'][i]<=5:
            origin_data.drop([i],inplace=True)
    return origin_data.reset_index(drop=True)

# 放电数据过滤器
def discharging_data_filter(file_path:string):
    origin_data=meta_data(file_path)
    for i in range(0,len(origin_data['DATE'])):
        if origin_data['STATUS'][i]=='Charging' or origin_data['TYPE'][i]!='Unknown' and origin_data['CURRENT_NOW'][i]>0:
            origin_data.drop([i],inplace=True)
    print(origin_data)
    return origin_data.reset_index(drop=True)

# 输出过滤后的数据
def data_output(file_path:string):
    status=sc.whether_charge_or_discharge(file_path)
    temp=sc.which_temp(file_path)
    # 根据场景识别，选择对应过滤器
    if status=='Charging' and temp=='normal-25' or temp=='normal-35':
        new_data=normal_charging_data_filter(file_path)
        # print(new_data)
        return new_data
    elif status=='Charging' and temp=='cold--15' or temp=='cold--10' or temp=='cold-0' or temp=='cold-5' or temp=='cold-10':
        new_data=cold_charging_data_filter(file_path)
        # print(new_data)
        return new_data
    elif status=='Charging' and temp=='hot':
        new_data=hot_charging_data_filter(file_path)
        # print(new_data)
        return new_data
    elif status=='Charging' and temp=='cold-back' or temp=='hot-back':
        new_data=back_charging_data_filter(file_path)
        # print(new_data)
        return new_data
    elif status=='Discharging':
        new_data=discharging_data_filter(file_path)
        # print(new_data)
        return new_data
