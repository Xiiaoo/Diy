import time
from time import sleep
import requests
import pandas as pd
import datetime


origin_url='https://api3.binance.com/api/v3/'


interval_enums=['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w']
coins=['BTC','ETH','DOT','FTM','LUNA','BNB','DOGE','SHIB','SAND','GALA','ADA','CAKE','UNI']
stable='USDT'

def time_convert(target_time):
        dt=target_time
        timeArray=time.strptime(dt,"%Y-%m-%d %H:%M:%S")
        timestamp=time.mktime(timeArray)
        return(int(timestamp*1000))

def timestamp_convert(millisecond):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(millisecond)/1000))

def timestamp_convert_second(second):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(second)/1000))


def loopcount_48H(detail_time):
        #分钟时间戳
        base_time=time_convert(detail_time)/60000
        time_year=str(datetime.datetime.now().year)
        time_month=str(datetime.datetime.now().month)
        time_day=str(datetime.datetime.now().day)
        time_hour='00'
        time_minute='00'
        time_second='00'
        time_str=time_year+'-'+time_month+'-'+time_day+' '+time_hour+':'+time_minute+':'+time_second
        #转换当天零点为时间戳
        a=int(time.mktime(time.strptime(time_str,"%Y-%m-%d %H:%M:%S"))/60)
        #距指定日期的小时数
        interval=int(a-base_time)
        #距今48小时数
        loop_count=interval//2880
        print('需要循环：'+str(loop_count)+'次')
        return loop_count
        
        

def get_serval_time():
        response=requests.request(
                url=origin_url+'time',
                method='get',
                proxies={'https':'http://127.0.0.1:10001'},
        )
        print(response.status_code)

def request_klines(request_catalogue,symbol,interval,startTime,endTime,limit):
        response=requests.request(
                method="get",
                url=origin_url+request_catalogue,
                proxies={'https':'http://127.0.0.1:10001'},
                params={
                        'symbol':symbol,
                        'interval':interval,
                        'startTime':startTime,
                        'endTime':endTime,
                        'limit':limit,
                }
        )
        return response.json()

# 16H
def klines_data_1m(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[0],
                        startTime=base_time,
                        endTime=base_time+57600000,
                        limit=960
                )
                base_time=base_time+57600000
                for j in data:
                        all_data.append(j)
        return(all_data)
        
# 48H
def klines_data_3m(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[1],
                        startTime=base_time,
                        endTime=base_time+172800000,
                        limit=960
                )
                base_time=base_time+172800000
                for j in data:
                        all_data.append(j)
        return(all_data)

# 48H
def klines_data_5m(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[2],
                        startTime=base_time,
                        endTime=base_time+172800000,
                        limit=576
                )
                base_time=base_time+172800000
                for j in data:
                        all_data.append(j)
        return(all_data)

# 48H
def klines_data_15m(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[3],
                        startTime=base_time,
                        endTime=base_time+172800000,
                        limit=192
                )
                base_time=base_time+172800000
                for j in data:
                        all_data.append(j)
        return(all_data)

# 48H
def klines_data_30m(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[4],
                        startTime=base_time,
                        endTime=base_time+172800000,
                        limit=96
                )
                base_time=base_time+172800000
                for j in data:
                        all_data.append(j)
        return(all_data)

# 48H
def klines_data_1h(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[5],
                        startTime=base_time,
                        endTime=base_time+172800000,
                        limit=48
                )
                base_time=base_time+172800000
                for j in data:
                        all_data.append(j)
        return(all_data)

# 48H
def klines_data_2h(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[6],
                        startTime=base_time,
                        endTime=base_time+172800000,
                        limit=24
                )
                base_time=base_time+172800000
                for j in data:
                        all_data.append(j)
        return(all_data)

# 48H
def klines_data_4h(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[7],
                        startTime=base_time,
                        endTime=base_time+172800000,
                        limit=12
                )
                base_time=base_time+172800000
                for j in data:
                        all_data.append(j)
        return(all_data)

# 48H
def klines_data_6h(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[8],
                        startTime=base_time,
                        endTime=base_time+172800000,
                        limit=8
                )
                base_time=base_time+172800000
                for j in data:
                        all_data.append(j)
        return(all_data)

# 48H
def klines_data_8h(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[9],
                        startTime=base_time,
                        endTime=base_time+172800000,
                        limit=6
                )
                base_time=base_time+172800000
                for j in data:
                        all_data.append(j)
        return(all_data)

# 48H
def klines_data_12h(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[10],
                        startTime=base_time,
                        endTime=base_time+172800000,
                        limit=4
                )
                base_time=base_time+172800000
                for j in data:
                        all_data.append(j)
        return(all_data)

# 48H
def klines_data_1d(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[11],
                        startTime=base_time,
                        endTime=base_time+172800000,
                        limit=2
                )
                base_time=base_time+172800000
                for j in data:
                        all_data.append(j)
                print(i)
        return(all_data)

# 72h
def klines_data_3d(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[12],
                        startTime=base_time,
                        endTime=base_time+259200000,
                        limit=1
                )
                base_time=base_time+259200000
                for j in data:
                        all_data.append(j)
        return(all_data)

# 168h
def klines_data_7d(symbol,detail_time,loop_count):
        all_data=[]
        base_time=time_convert(detail_time)
        for i in range(loop_count):
                data=request_klines(
                        request_catalogue='klines',
                        symbol=symbol,
                        interval=interval_enums[13],
                        startTime=base_time,
                        endTime=base_time+604800000,
                        limit=1
                )
                base_time=base_time+604800000
                for j in data:
                        all_data.append(j)
        return(all_data)


def datas_to_excel_1m(symbol,detail_time,loop_count):
        meta_data=klines_data_1m(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_1m'+'.xlsx',
                sheet_name='data',
                index=False
        )

def datas_to_excel_3m(symbol,detail_time,loop_count):
        meta_data=klines_data_3m(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_3m'+'.xlsx',
                sheet_name='data',
                index=False
        )

def datas_to_excel_5m(symbol,detail_time,loop_count):
        meta_data=klines_data_5m(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_5m'+'.xlsx',
                sheet_name='data',
                index=False
        )

def datas_to_excel_15m(symbol,detail_time,loop_count):
        meta_data=klines_data_15m(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_15m'+'.xlsx',
                sheet_name='data',
                index=False
        )

def datas_to_excel_30m(symbol,detail_time,loop_count):
        meta_data=klines_data_30m(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_30m'+'.xlsx',
                sheet_name='data',
                index=False
        )
        
def datas_to_excel_1h(symbol,detail_time,loop_count):
        meta_data=klines_data_1h(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_1h'+'.xlsx',
                sheet_name='data',
                index=False
        )
        
def datas_to_excel_2h(symbol,detail_time,loop_count):
        meta_data=klines_data_2h(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_2h'+'.xlsx',
                sheet_name='data',
                index=False
        )
        
def datas_to_excel_4h(symbol,detail_time,loop_count):
        meta_data=klines_data_4h(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_4h'+'.xlsx',
                sheet_name='data',
                index=False
        )
        
def datas_to_excel_6h(symbol,detail_time,loop_count):
        meta_data=klines_data_6h(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_6h'+'.xlsx',
                sheet_name='data',
                index=False
        )
        
def datas_to_excel_8h(symbol,detail_time,loop_count):
        meta_data=klines_data_8h(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_8h'+'.xlsx',
                sheet_name='data',
                index=False
        )
        
def datas_to_excel_12h(symbol,detail_time,loop_count):
        meta_data=klines_data_12h(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_12h'+'.xlsx',
                sheet_name='data',
                index=False
        )
        
def datas_to_excel_1d(symbol,detail_time,loop_count):
        meta_data=klines_data_1d(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_1d'+'.xlsx',
                sheet_name='data',
                index=False
        )

def datas_to_excel_3d(symbol,detail_time,loop_count):
        meta_data=klines_data_3d(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_3d'+'.xlsx',
                sheet_name='data',
                index=False
        )
        
def datas_to_excel_7d(symbol,detail_time,loop_count):
        meta_data=klines_data_7d(symbol,detail_time,loop_count)
        opentime,open,high,low,close=[],[],[],[],[]
        for i in range(0,len(meta_data)):
                opentime.append(timestamp_convert(meta_data[i][0]))
                open.append(float(meta_data[i][1]))
                high.append(float(meta_data[i][2]))
                low.append(float(meta_data[i][3]))
                close.append(float(meta_data[i][4]))
        df=pd.DataFrame({
                'opentime':opentime,
                'open':open,
                'high':high,
                'low':low,
                'close':close,
        })
        df.to_excel(
                excel_writer=str(symbol)+'_7d'+'.xlsx',
                sheet_name='data',
                index=False
        )
        

def main():
        t_time='2017-10-01 00:00:00'
        loop_count_48H=loopcount_48H(t_time)
        datas_to_excel_1m('BTCUSDT',t_time,loop_count_48H*3)
        print(1)
        # datas_to_excel_3m('BTCUSDT',t_time,loop_count_48H)
        # print(2)
        # datas_to_excel_5m('BTCUSDT',t_time,loop_count_48H)
        # print(3)
        # datas_to_excel_15m('BTCUSDT',t_time,loop_count_48H)
        # print(4)
        # datas_to_excel_30m('BTCUSDT',t_time,loop_count_48H)
        # print(5)
        # datas_to_excel_1h('BTCUSDT',t_time,loop_count_48H)
        # print(6)
        # datas_to_excel_2h('BTCUSDT',t_time,loop_count_48H)
        # print(7)
        # datas_to_excel_4h('BTCUSDT',t_time,loop_count_48H)
        # print(8)
        # datas_to_excel_6h('BTCUSDT',t_time,loop_count_48H)
        # print(9)
        # datas_to_excel_8h('BTCUSDT',t_time,loop_count_48H)
        # print(10)
        # datas_to_excel_12h('BTCUSDT',t_time,loop_count_48H)
        # print(11)
        # datas_to_excel_1d('BTCUSDT',t_time,loop_count_48H)
        # print(12)
        # datas_to_excel_3d('BTCUSDT',t_time,5)
        # print(13)
        # datas_to_excel_7d('BTCUSDT',t_time,5)
        # print(14)
        

        # datas_to_excel_1d('BTCUSDT',t_time,loop_count_48H)
        get_serval_time()

if __name__ == '__main__':
    main()
