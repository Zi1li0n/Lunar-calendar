import sxtwl

lunar = sxtwl.Lunar()  # 实例化日历库

Gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
Zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
ShX = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
Week = ['日', '一', '二', '三', '四', '五', '六']
numCn = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
jqmc = ['冬至', '小寒', '大寒', '立春', '雨水', '惊蛰', '春分', '清明', '谷雨', '立夏', '小满', '芒种', '夏至', '小暑', '大暑', '立秋', '处暑', '白露',
        '秋分', '寒露', '霜降', '立冬', '小雪', '大雪']
ymc = ['十一', '十二', '正', '二', '三', '四', '五', '六', '七', '八', '九', '十']
rmc = ['初一', '初二', '初三', '初四', '初五', '初六', '初七', '初八', '初九', '初十', '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九',
       '二十', '廿一', '廿二', '廿三', '廿四', '廿五', '廿六', '廿七', '廿八', '廿九', '三十', '卅一']


# 格式化输出
def log(*arg):
    s = ''
    for v in arg:
        s += str(v)
    print(s)


def printDay(day):
    log('===================================================')
    log('公历:', day.y, '年', day.m, '月', day.d, '日')
    if day.Lleap:
        log('农历:', '闰', ymc[day.Lmc], '月', rmc[day.Ldi])
    else:
        log('农历:', ymc[day.Lmc], '月', rmc[day.Ldi])

    if (day.qk >= 0):
        log('当前节气:', jqmc[day.jqmc])
    log('星期', Week[day.week])


while (True):
    line = input('请选择:\n'
                 '1.输入公历查农历\n'
                 '2.输入农历查公历\n'
                 '3.退出\n')
    if line == '1' or line == '2':
        try:
            date = input('请输入日期:(格式为Y.m.d)\n')
            list = date.split('.')
            Y = int(list[0])
            m = int(list[1])
            d = int(list[2])
        except IndexError:
            print("日期格式错误，请重新输入...")
            continue
        # 农历转公历
        if line == '1':
            day1 = lunar.getDayBySolar(Y, m, d)
            printDay(day1)
        # 公历转农历
        if line == '2':
            day2 = lunar.getDayByLunar(Y, m, d)
            printDay(day2)
        # 获取一年的信息
        year = lunar.getYearCal(Y);
        log(Gan[year.yearGan], Zhi[year.yearZhi], '年')
        log('按Enter继续...')
        input()
        continue

    if line == '3':
        break
    else:
        log('erro,请重新输入')
        continue

