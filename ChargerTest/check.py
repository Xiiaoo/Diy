import string
import filter as fil
import scene as sc
import math

# 充电类型检查
def check_charger_type(file_path:string):
    new_data=fil.data_output(file_path)
    true_type=sc.which_type(file_path)
    k=0
    for i in range(0,len(new_data['DATE'])):
            if new_data['TYPE'][i]!=true_type:
                print('充电类型识别有异常:  '+new_data['DATE'][i]+'充电类型为: '+new_data['TYPE'][i])
                k+=1
    if k==0:
        print('充电类型识别无异常,该项PASS')

# 自学习容量检查
def check_charger_full(file_path:string):
    new_data=fil.data_output(file_path)
    k=0
    for i in range(0,len(new_data['DATE'])):
            if new_data['Charger_Full'][i] < 4500:
                print('Charger_Full自学习容量过低: '+new_data['DATE'][i]+'Charger_Full为: '+str(new_data['Charger_Full'][i]))
                k+=1
    if k==0:
        print('电池自学习容量无异常,该项PASS')

# 充满电检查
def check_can_charge_to_full(file_path:string):
    new_data=fil.data_output(file_path)
    max_soc=new_data['SOC'].max()
    if max_soc<100:
        print('无法充满电')
    else:
        print('可以充满电,该项PASS')

# 电流跳变检查
def check_current_stable(file_path:string):
    new_data=fil.data_output(file_path)
    for i in range(100,len(new_data['DATE'])):
        if math.fabs(new_data['CURRENT_NOW'][i]-new_data['CURRENT_NOW'][i-1])>1500:
            print('电流有跳变:'+new_data['DATE'][i])

# 截止电流检查
def check_cut_off_current(file_path:string):
    new_data=fil.data_output(file_path)
    for i in reversed(range(len(new_data['DATE']))):
        if new_data['CURRENT_NOW'][i]>200:
            current_now=new_data['CURRENT_NOW'][i]
            cut_temp=new_data['TEMP'][i]
            break
    # 非标充截止电流PASS
    if sc.which_type(file_path)!='USB_PD' and current_now >= 225 and current_now < 275:
        print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止电流为: '+str(current_now)+' mA' )
        return current_now
    # 非标充截止电流偏高
    elif sc.which_type(file_path)!='USB_PD' and  current_now > 275:
        print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止电流为: '+str(current_now)+' mA' +' 高于规格书上限: '+str(current_now-275)+'mA')
        return current_now
    # 非标充截止电流偏低
    elif sc.which_type(file_path)!='USB_PD' and  current_now < 225:
        print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止电流为: '+str(current_now)+' mA' +' 低于规格书上限'+str(225-current_now)+'mA')
        return current_now
    # 标充高低温截止电流
    elif sc.which_type(file_path)=='USB_PD' and cut_temp > 48 or cut_temp < 15:
        if current_now >= 225 and current_now < 275:
            print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止电流为: '+str(current_now)+'截止温度为：'+ str(cut_temp))
            return current_now
    # 标充15-35截止电流判断
    elif sc.which_type(file_path)=='USB_PD' and cut_temp >= 15 and cut_temp < 35:
        if current_now >= 750 and current_now < 920:
            print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+'截止温度为：'+ str(cut_temp)+' 截止电流为: '+str(current_now))
            return current_now
        # 标充截止电流偏低
        elif current_now < 750:
            print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止温度为：'+ str(cut_temp)+' 截止电流为: '+str(current_now)+'mA'+' 低于规格书:'+str(750-current_now)+'mA')
            return current_now
        # 标充截止电流偏高
        elif current_now > 920:
            print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止温度为：'+ str(cut_temp)+' 截止电流为: '+str(current_now)+'mA'+' 高于规格书:'+str(current_now-920)+'mA')
            return current_now
    # 标充35-48截止电流判断   
    elif sc.which_type(file_path)=='USB_PD' and cut_temp > 35 and cut_temp < 48:
        if sc.which_battery(file_path)=='S88006_SWD_4V45_5000mAh':
            # SWD-标充正常截止
            if current_now >= 838 and current_now < 1024:
                print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止电流为: '+str(current_now)+'截止温度为：'+ str(cut_temp))
                return current_now
            # SWD-标充截止电流偏低
            elif current_now < 838:
                print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止温度为：'+ str(cut_temp)+' 截止电流为: '+str(current_now)+'mA'+' 低于规格书:'+str(838-current_now)+'mA')
                return current_now
            # SWD-标充截止电流偏高
            elif current_now > 1024:
                print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止温度为：'+ str(cut_temp)+' 截止电流为: '+str(current_now)+'mA'+' 高于规格书:'+str(current_now-1024)+'mA')
                return current_now
        elif sc.which_battery(file_path)=='S88006_NVT_4V45_5000mAh':
            # NVT-标充正常截止
            if current_now >= 882 and current_now < 1078:
                print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止电流为: '+str(current_now)+'截止温度为：'+ str(cut_temp))
                return current_now
            # NVT-标充截止电流偏低
            elif current_now < 882:
                print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止温度为：'+ str(cut_temp)+' 截止电流为: '+str(current_now)+'mA'+' 低于规格书:'+str(882-current_now)+'mA')
                return current_now
            # NVT-标充截止电流偏高
            elif current_now > 1024:
                print('电池为:'+sc.which_battery(file_path)+' 充电类型为:'+sc.which_type(file_path)+' 截止温度为：'+ str(cut_temp)+' 截止电流为: '+str(current_now)+'mA'+' 高于规格书:'+str(current_now-1078)+'mA')
                return current_now



# check_charger_type('D:\\Work\\K6S\\P2\\new-SOCdata.csv')
# check_charger_full('D:\\Work\\K6S\\P2\\new-SOCdata.csv')
# check_can_charge_to_full('D:\\Work\\K6S\\P2\\new-SOCdata.csv')
# check_current_stable('D:\\Work\\K6S\\P2\\new-SOCdata.csv')
# check_cut_off_current('D:\\Work\\K6S\\P2\\new-SOCdata.csv')