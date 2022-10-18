import random


for i in range(5):
    # 定义常量数组
    listA = []
    listB = []
    # 定义彩票数组
    listC = []
    listD = []
    listE = []



    # 常量数组赋值
    for x in range(1, 35):
        listA.append(x)

    for y in range(1, 13):
        listB.append(y)

    # 写入彩票数组首元素并在常量数组中删除相同值的元素，目的为了去重
    m = random.randint(1, 35)
    n = random.randint(1, 12)
    # 删除随机数对应常量数组中对应索引的元素
    del listA[m - 1]
    del listB[n - 1]
    # 将随机数加入到彩票数组中
    listC.append(m)
    listD.append(n)

    # 填充彩票数组前五位
    for p in range(4):
        a = listA[random.randint(1, len(listA) - 1)]
        listA.remove(a)
        listC.append(a)

    # 填充彩票数组后两位
    for q in range(1):
        b = listB[random.randint(1, len(listB) - 1)]
        listB.remove(b)
        listD.append(b)

    # 彩票数组排序
    listC.sort()
    listD.sort()

    listE = listC + listD
    print(listC,listD)
    listC.clear()
    listD.clear()
