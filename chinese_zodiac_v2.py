# 记录生肖，用年份来判断生肖
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

year = int(input('请用户输入出生年份'))

# print(chinese_zodiac[year % 12])
if chinese_zodiac[year % 12] == '狗':
    print(str(year) + '是狗年')  # 2018是狗年
