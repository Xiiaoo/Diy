import pandas as pd

def meta_data(file_path):
    data=pd.read_csv(file_path)
    df=pd.DataFrame({
        'DATE':data.DATE,
        'TIME':data.TIME,
        'SOC':data.SOC,
        'CURRENT_NOW':data.CURRENT_NOW,
        'VOLTAGE_NOW':data.VOLTAGE_NOW,
        'CP_VBAT':data.CP_VBAT,
        'IC_V':data.IC_V,
        # 'CP_VBUS':data.CP_VBUS,
        # 'CP_IBUS':data.CP_IBUS,
        # 'VBUS_VOLTAGE_uV':data.VBUS_VOLTAGE_uV,
        'TEMP':data.TEMP,
        'BOARD_TEMP':data.BOARD_TEMP,
        'Thermal_TEMP':data.Thermal_TEMP,
        'Thermal_point':data.Thermal_point,
        'STATUS':data.STATUS,
        'TYPE':data.TYPE,
        'FFC_VOLTAGE_MAX':data.FFC_VOLTAGE_MAX,
        'FFC_CHG':data.FFC_CHG,
        'Charger_Full':data.Charger_Full,
        'M_CP':data.M_CP,
        'S_CP':data.S_CP,
        'CP_CURRENT':data.CP_CURRENT,
        'SOH':data.SOH,
        'AverageCurrent':data.AverageCurrent,
        'QMAX':data.QMAX,
        'RM':data.RM,
        'TRUE_RM':data.TRUE_RM,
        'FCC':data.FCC,
        'TRUE_FCC':data.TRUE_FCC,
        'CYCLE':data.CYCLE,
        'CURR_MAX':data.CURR_MAX,
        'VOLT_MAX':data.VOLT_MAX,
        'Battery_Name':data.Battery_Name,
        'CHARGER_MDOE':data.CHARGER_MDOE,
    })
    
    # 查看行
    # print(df.iloc[5])
    # 行列转置
    # print(df.T)
    # 列值
    return df