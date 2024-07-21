zodiac_name = ['摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座']
zodiac_days = (
    (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

int_month = int(input('用户输入月份:'))
int_day = int(input('用户输入日:'))

print(type(int_day))

for zd_num in range(len(zodiac_days)):
    if zodiac_days[zd_num] >= (int_month, int_day):
        print(zodiac_name[zd_num])
        break
    elif int_month >= 12 and int_day >= 23:
        print(zodiac_name[0])
        break
