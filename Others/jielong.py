import pandas as pd


path='D:\\Projects\\dingdan20220413_1057_7e32be7a86e74e70a3293539853440aa.xlsx'
data=pd.read_excel(path,sheet_name='顾客商品表')

excel_data={
    
}

# unit:单位   cost:成本   single_price:卖出单价
detail={
    '电子消杀枪':{
        '一份数量':1,
        'unit':'只',
        'cost':'',
        'singe_price':180
    },
    '酒精喷雾100ml':{
        '一份数量':3,
        'unit':'瓶',
        'cost':'',
        'singe_price':15
    },
    '一次性隔离服':{
        '一份数量':5,
        'unit':'件',
        'cost':'',
        'singe_price':28
    },
    '医用外科口罩':{
        '一份数量':2,
        'unit':'盒',
        'cost':'',
        'singe_price':46
    },
    '84消毒液': {
        '一份数量':3,
        'unit':'瓶',
        'cost':'',
        'singe_price':18
    },
    '连体防护服':{
        '一份数量':2,
        'unit':'套',
        'cost':'',
        'singe_price':118
    } ,
    '蓝色定型手套':{
        '一份数量':2,
        'unit':'盒',
        'cost':'',
        'singe_price':54
    } ,
    '医用隔离眼镜':{
        '一份数量':3,
        'unit':'只',
        'cost':'',
        'singe_price':25
    } ,
    '医用隔离防护面罩':{
        '一份数量':3,
        'unit':'个',
        'cost':'',
        'singe_price':13
    } ,
    '免水抑菌洗手凝胶500ml':{
        '一份数量':2,
        'unit':'瓶',
        'cost':'',
        'singe_price':22
    } ,
    '二氧化氯消毒片':{
        '一份数量':3,
        'unit':'瓶',
        'cost':'',
        'singe_price':18
    } ,
    '医用N95口罩':{
        '一份数量':1,
        'unit':'盒',
        'cost':'',
        'singe_price':260
    } ,
    '医生PVC检查手套':{
        '一份数量':2,
        'unit':'盒',
        'cost':'',
        'singe_price':58
    } ,
    '空喷壶':{
        '一份数量':2,
        'unit':'个',
        'cost':'',
        'singe_price':8
    } ,
    '免洗手消毒液1L':{
        '一份数量':1,
        'unit':'瓶',
        'cost':'',
        'singe_price':60
    } ,
    '酒精带喷头':{
        '一份数量':2,
        'unit':'瓶',
        'cost':'',
        'singe_price':25
    } ,
    '酒精不带喷头':{
        '一份数量':2,
        'unit':'套',
        'cost':'',
        'singe_price':22
    } ,
    '空喷壶2L装': {
        '一份数量':1,
        'unit':'个',
        'cost':'',
        'singe_price':25
    }
}

print(detail['84消毒液']['unit'])

for i in range (0,len(data.微信名称)):
    if data.订单状态[i] == '已取消接龙':
        data.drop([i],inplace=True)

excel_data.to_excel(
        excel_writer=path,
        sheet_name='data',
        index=False
)