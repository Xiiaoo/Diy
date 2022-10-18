import time
import check
import time_analysis
import filter
import sys
import os
import scene


def main():
    xiangmu=input("请输入项目号(如K6S):")
    jieduan=input("请输入所处阶段(如P2):")
    zuhe=input("请输入组合号(如ZUHE1):")
    bianhao=input("请输入机器数字编号(如55555):")
    default_path='D:\\Work'
    file_path=xiangmu+'\\'+jieduan
    file_name=zuhe+'-'+bianhao+'-'+str(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(int(time.time()))))
    path=default_path+'\\'+file_path
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
    os.system('adb root')
    os.system('adb pull /data/local/tmp/1 '+path)
    
    """重命名导出的1文件夹为 组合-编号 形式"""
    os.system('ren '+path+'\\'+'1 '+file_name)
    print('文件存放路径:'+path+'\\'+file_name+'\\'+'SOCdata'+'.csv')
    
    tmp=scene.which_temp(path+'\\'+file_name+'\\'+'SOCdata'+'.csv')
    charge_type=scene.which_type(path+'\\'+file_name+'\\'+'SOCdata'+'.csv')
    c_or_disc=scene.whether_charge_or_discharge(path+'\\'+file_name+'\\'+'SOCdata'+'.csv')
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time()))))
    check.check_can_charge_to_full(path+'\\'+file_name+'\\'+'SOCdata'+'.csv')
    check.check_charger_full(path+'\\'+file_name+'\\'+'SOCdata'+'.csv')
    check.check_charger_type(path+'\\'+file_name+'\\'+'SOCdata'+'.csv')
    check.check_current_stable(path+'\\'+file_name+'\\'+'SOCdata'+'.csv')
    check.check_cut_off_current(path+'\\'+file_name+'\\'+'SOCdata'+'.csv')
    time_analysis.analysis(path+'\\'+file_name+'\\'+'SOCdata'+'.csv')
    
    filter.data_output(path+'\\'+file_name+'\\'+'SOCdata'+'.csv').to_excel(
        excel_writer=path+'\\'+file_name+'-'+tmp+'-'+charge_type+'-'+c_or_disc+'-'+'.xlsx',
        sheet_name='data',
        index=False
    )
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time()))))

if __name__ == '__main__':
    main()