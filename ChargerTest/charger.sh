#!/system/bin/sh

PMI_ADC_DIR="/sys/bus/iio/devices/iio:device1"
CP_DIR="/sys/class/charge_pump"

sleep 3

echo "8" > /proc/sys/kernel/printk
xtime=$(date +%H-%M-%S)
if [ -d /data/local/tmp/1 ]; then
	if [ ! -d /data/local/tmp/old ]; then
		mkdir -p /data/local/tmp/old
		chmod 777 /data/local/tmp/old
	fi
    	mkdir -p /data/local/tmp/old/$xtime
    	mv /data/local/tmp/1/* /data/local/tmp/old/$xtime
else
	mkdir -p /data/local/tmp/1
	chmod 777 /data/local/tmp/1/
fi
  cat /proc/kmsg > /data/local/tmp/1/kernel.log &
  echo "DATE,TIME,SOC,CURRENT_NOW,VOLTAGE_NOW,CP_VBAT,IC_V,CP_VBUS,CP_IBUS,VBUS_VOLTAGE_uV,TEMP,BOARD_TEMP,Thermal_TEMP,Thermal_point,STATUS,TYPE,FFC_VOLTAGE_MAX,FFC_CHG,Charger_Full,M_CP,S_CP,CP_CURRENT,SOH,AverageCurrent,QMAX,RM,TRUE_RM,FCC,TRUE_FCC,CYCLE,CURR_MAX,VOLT_MAX,CHARGER_MDOE" >> /data/local/tmp/1/SOCdata.csv

num=100
num2=10
num3=1000
num4=1000000

intialSec=$(date +%s)

while [ "$num" -gt "1" ];do
	timeSec=$(date +%s)
	SOC=$(cat /sys/class/power_supply/battery/capacity)
	cnow=$(echo "scale=3;$(($(cat /sys/class/power_supply/battery/current_now)))/$num3" | bc)
	vnow=$(echo "scale=3;$(($(cat /sys/class/power_supply/battery/voltage_now)))/$num4" | bc)
	vbat=$(echo "scale=3;$(($(cat /sys/class/qcom-battery/cell_voltage)))/$num4" | bc)
                if [$vnow -lt $vbat];then
                                IC_V=$vnow
                else
                                IC_V=$vbat
                fi
	cp_vbus=$(echo "scale=3;$(($(cat /sys/class/qcom-battery/cp_vbus_voltage)))/$num3" | bc)
	cp_ibus=$(cat /sys/class/qcom-battery/cp_ibus_master)
	vvoltage=$(cat /sys/class/qcom-battery/vbus_voltage)
	batteryTemp=$(echo "scale=1;$(($(cat /sys/class/power_supply/battery/temp)))/$num2" | bc)
	board_temp=$(echo "scale=1;$(($(cat /sys/class/thermal/thermal_message/board_sensor_temp)))/$num3" | bc)
                sdm_skin_therm=$(echo "scale=1;$(($(cat /sys/class/thermal/thermal_zone64/temp)))/$num3" | bc)
	Thermal_point=$(cat /sys/class/power_supply/battery/charge_control_limit)
	batteryStatus=$(cat /sys/class/power_supply/battery/status)
	ChargerType=$(cat /sys/class/qcom-battery/real_type)
	FFC=$(echo "scale=1;$(($(cat /sys/class/power_supply/battery/voltage_max)))/$num4" | bc)
	ffc_chg=$(cat /sys/class/qcom-battery/fastcharge_mode)
	charger_full=$(echo "scale=0;$(($(cat /sys/class/power_supply/battery/charge_full)))/$num3" | bc)
	cp_enable=$(cat /sys/class/qcom-battery/fastcharge_mode)
	
	if [ $cp_enable == "1" ];then
		isns1=$(cat /sys/class/qcom-battery/cp_ibus_master)
		isns2=$(cat /sys/class/qcom-battery/cp_ibus_slave)
	else
		isns1=0
		isns2=0
	fi
	input_current=$(cat /sys/class/qcom-battery/input_current)
	avg_current=$(cat /sys/class/power_supply/battery/current_now)
	soh=$(cat /sys/devices/platform/soc/4a80000.i2c/i2c-4/4-0055/soh)
	Qmax=$(cat /sys/devices/platform/soc/4a80000.i2c/i2c-4/4-0055/Qmax)
	rm=$(cat /sys/devices/platform/soc/4a80000.i2c/i2c-4/4-0055/rm)
	truerm=$(cat /sys/devices/platform/soc/4a80000.i2c/i2c-4/4-0055/TRemQ)
	fccdata=$(cat /sys/devices/platform/soc/4a80000.i2c/i2c-4/4-0055/fcc)
	truefcc=$(cat /sys/devices/platform/soc/4a80000.i2c/i2c-4/4-0055/TFullChgQ)
	cyclecount=$(cat /sys/class/power_supply/battery/cycle_count)
	currmax=$(echo "scale=3;$(($(cat /sys/class/power_supply/usb/current_max)))/$num4" | bc)
	voltmax=$(echo "scale=3;$(($(cat /sys/class/power_supply/usb/voltage_max)))/$num4" | bc)
                chargeMode=$(echo "scale=3;$cp_vbus/$vbat" |bc)	

                secNow=$(date +%s)
                sec=$(($secNow-$intialSec))
	deltaTime=$sec
	echo "$(date),$deltaTime,$SOC,$cnow,$vnow,$vbat,$IC_V,$cp_vbus,$cp_ibus,$vvoltage,$batteryTemp,$board_temp,$sdm_skin_therm,$Thermal_point,$batteryStatus,$ChargerType,$FFC,$ffc_chg,$charger_full,$isns1,$isns2,$input_current,$soh,$avg_current,$Qmax,$rm,$truerm,$fccdata,$truefcc,$cyclecount,$currmax,$voltmax,$chargeMode" >> /data/local/tmp/1/SOCdata.csv

done
