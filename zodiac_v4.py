chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
zodiac_name = ['摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座']
zodiac_days = (
    (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

z_num = {}
for i in zodiac_name:
    z_num[i] = 0

while True:
    int_year = int(input('用户输入年份:'))
    int_month = int(input('用户输入月份:'))
    int_day = int(input('用户输入日:'))

    n = 0
    while zodiac_days[n] < (int_month, int_day):
        if int_month == 12 and int_day > 23:
            break
        n = n + 1
    print(zodiac_name[n])

    # 输出生肖和星座
    # print('%s 年的生肖是 %s ' % (int_year, zodiac_name[int_year % 12]))

    # 输出生肖和星座统计信息
    cz_num[chinese_zodiac[int_year % 12]] += 1
    z_num[zodiac_name[n]] += 1

    for each_key in cz_num.keys():
        print('生肖 %s 有 %d 个' % (each_key, cz_num[each_key]))

    for each_key in z_num.keys():
        print('星座 %s 有 %d 个' % (each_key, z_num[each_key]))
