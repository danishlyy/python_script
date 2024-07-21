# 记录生肖，用年份来判断生肖
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

for cz in chinese_zodiac:
    print(cz)

for i in range(1, 13):
    print(i)  # 1...12

# 2000~2018 年对应的生肖
for year in range(2000, 2019):
    print('%s 年是 %s 年' % (year, chinese_zodiac[year % 12]))
