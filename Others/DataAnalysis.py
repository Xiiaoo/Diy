import os
import shutil
import time
# import xlsxwriter
# pip install pandas
import pandas as pd

origin_path = 'E:\\Work\\C2544.xlsx'

path_str = input("请输入工作目录：")
case_ID = input("请输入用例号：")
machine_num = input("请输入机器型号：")

path = path_str + '\\' + case_ID + '\\' + machine_num

work_path = path.rstrip("\\")

# 创建工作目录
os.makedirs(work_path)

# 复制文件至指定目录
shutil.copy(origin_path, work_path)

# 重命名表格
old_name = path_str + '/' + case_ID + '/' + machine_num + '/' + 'C2544.xlsx'
new_name = path_str + '/' + case_ID + '/' + machine_num + '/' + case_ID + '-' + machine_num + '.xlsx'
print(new_name)

os.rename(old_name, new_name)

cmd0 = 'adb root'
cmd1 = 'adb pull /data/local/tmp/1/SOCdata.csv ' + work_path
cmd2 = 'adb pull /data/local/tmp/1/kernel.log ' + work_path
os.system(cmd0)
os.system(cmd1)
os.system(cmd2)

time.sleep(30)

data = pd.read_excel(new_name)

# 首次通过充电类型过滤数据
list_TYPE = []

for i in data.TYPE:
    list_TYPE.append(i)

# 删除充电类型干扰行
for j in range(0, len(list_TYPE)):
    if list_TYPE[j] == 'USB' or list_TYPE[j] == 'USB_CDP' or list_TYPE[j] == 'USB_DCP' or list_TYPE[j] == 'USB_HVDCP':
        data.drop([j], inplace=True)

# 保存
data.to_excel(excel_writer=new_name)

print('首次过滤完成')

# 第二次通过FFC切换干扰项过滤数据
data_twice = pd.read_excel(new_name)
list_TYPE = []
list_TYPE_INDEX = []
list_FFC_CHG = []
list_CURRENT_NOW = []
list_SOC = []

# 创建新TYPE列:[USB_PD,USB_PD......]
for k in data_twice.TYPE:
    list_TYPE.append(k)

for m in range(0, len(list_TYPE)):
    list_TYPE_INDEX.append(m)

# 创建FFC_CHG列
for p in data_twice.FFC_CHG:
    list_FFC_CHG.append(p)

# 创建电流列
for q in data_twice.CURRENT_NOW:
    list_CURRENT_NOW.append(q)

for s in data_twice.SOC:
    list_SOC.append(s)

for n in list_TYPE_INDEX:
    if list_FFC_CHG[n] == 0 and list_CURRENT_NOW[n] < 0 and list_SOC[n] < 10:
        data_twice.drop([n], inplace=True)

data_twice.to_excel(excel_writer=new_name)

print('第二次过滤完成')
# 第三次删除状态为未充电行
list_STATUS = []
data_third = pd.read_excel(new_name)

for x in data_third.STATUS:
    list_STATUS.append(x)

for y in range(0, len(list_STATUS)):
    if list_STATUS[y] == 'Discharging':
        data_third.drop([y], inplace=True)

data_third.to_excel(excel_writer=new_name)

print('第三次过滤完成')

data_fourth = pd.read_excel(new_name)

list_STATUS = []
list_TIME = []
list_SOC = []
list_SOC_INDEX = []
list_TEMP = []
TIME_POINT = 0

SOC_5_TIME = \
    SOC_10_TIME = \
    SOC_20_TIME = \
    SOC_30_TIME = \
    SOC_40_TIME = \
    SOC_50_TIME = \
    SOC_60_TIME = \
    SOC_70_TIME = \
    SOC_80_TIME = \
    SOC_90_TIME = \
    SOC_100_TIME = \
    SOC_FULL_TIME = 0

# 创建电量列
for i in data_fourth.SOC:
    list_SOC.append(i)

# 创建时间列
for i in data_fourth.TIME:
    list_TIME.append(i)

# 创建状态列
for i in data_fourth.STATUS:
    list_STATUS.append(i)

# 创建温度列
for i in data_fourth.TEMP:
    list_TEMP.append(i)

# 起始时间点
start_TIME = list_TIME[0]

for i in range(0, len(list_SOC)):
    list_SOC_INDEX.append(i)

# 1-10%充电时长
for i in list_SOC_INDEX:
    if list_SOC[i] == 4:
        TIME_POINT = list_TIME[i] + 1
        SOC_5_TIME = (TIME_POINT - start_TIME) / 60
    elif list_SOC[i] == 9:
        TIME_POINT = list_TIME[i] + 1
        SOC_10_TIME = (TIME_POINT - start_TIME) / 60
    elif list_SOC[i] == 19:
        TIME_POINT = list_TIME[i] + 1
        SOC_20_TIME = (TIME_POINT - start_TIME) / 60
    elif list_SOC[i] == 29:
        TIME_POINT = list_TIME[i] + 1
        SOC_30_TIME = (TIME_POINT - start_TIME) / 60
    elif list_SOC[i] == 39:
        TIME_POINT = list_TIME[i] + 1
        SOC_40_TIME = (TIME_POINT - start_TIME) / 60
    elif list_SOC[i] == 49:
        TIME_POINT = list_TIME[i] + 1
        SOC_50_TIME = (TIME_POINT - start_TIME) / 60
    elif list_SOC[i] == 59:
        TIME_POINT = list_TIME[i] + 1
        SOC_60_TIME = (TIME_POINT - start_TIME) / 60
    elif list_SOC[i] == 69:
        TIME_POINT = list_TIME[i] + 1
        SOC_70_TIME = (TIME_POINT - start_TIME) / 60
    elif list_SOC[i] == 79:
        TIME_POINT = list_TIME[i] + 1
        SOC_80_TIME = (TIME_POINT - start_TIME) / 60
    elif list_SOC[i] == 89:
        TIME_POINT = list_TIME[i] + 1
        SOC_90_TIME = (TIME_POINT - start_TIME) / 60
    elif list_SOC[i] == 99:
        TIME_POINT = list_TIME[i] + 1
        SOC_100_TIME = (TIME_POINT - start_TIME) / 60
    elif list_STATUS[i] == 'Charging':
        TIME_POINT = list_TIME[i] + 1
        SOC_FULL_TIME = (TIME_POINT - start_TIME) / 60
    else:
        pass
print('达到各电量点耗费时间：')
print('充至5%时所用时间')
print(SOC_5_TIME)
print('充至10%时所用时间')
print(SOC_10_TIME)
print('充至20%时所用时间')
print(SOC_20_TIME)
print('充至30%时所用时间')
print(SOC_30_TIME)
print('充至40%时所用时间')
print(SOC_40_TIME)
print('充至50%时所用时间')
print(SOC_50_TIME)
print('充至60%时所用时间')
print(SOC_60_TIME)
print('充至70%时所用时间')
print(SOC_70_TIME)
print('充至80%时所用时间')
print(SOC_80_TIME)
print('充至90%时所用时间')
print(SOC_90_TIME)
print('充至100%时所用时间')
print(SOC_100_TIME)
print('充至FULL%时所用时间')
print(SOC_FULL_TIME)

for k in range(0, len(list_TIME)):
    if list_TIME[k] == start_TIME + 300:
        print('5min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 600:
        print('10min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 900:
        print('15min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 1200:
        print('20min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 1500:
        print('25min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 1800:
        print('30min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 2100:
        print('35min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 2400:
        print('40min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 2700:
        print('45min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 3000:
        print('50min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 3300:
        print('55min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 3600:
        print('60min电量为：')
        print(list_SOC[k])
    elif list_TIME[k] == start_TIME + 3900:
        print('65min电量为：')
        print(list_SOC[k])
        print('65min充电状态为：')
        print(list_STATUS[k])
    elif list_TIME[k] == start_TIME + 4200:
        print('70min电量为：')
        print(list_SOC[k])
        print('70min充电状态为：')
        print(list_STATUS[k])
    elif list_TIME[k] == start_TIME + 4500:
        print('75min电量为：')
        print(list_SOC[k])
        print('75min充电状态为：')
        print(list_STATUS[k])

print('3h SOC：')
if list_SOC[10800] is None:
    pass
elif list_SOC[10800] == 100:
    pass
else:
    print(list_SOC[10800])
