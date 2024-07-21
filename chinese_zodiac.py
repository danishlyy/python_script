# 记录生肖，用年份来判断生肖
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

print(chinese_zodiac[0])  # 鼠

print(chinese_zodiac[0:4])  # 鼠牛虎兔

print(chinese_zodiac[-1])  # 猪

year = 2024
print(year % 12)  # 8
print(chinese_zodiac[year % 12])  # 龙

print('狗' in chinese_zodiac)  # True

print('狗' not in chinese_zodiac)  # False

# 序列连接
print(chinese_zodiac + chinese_zodiac)  # 猴鸡狗猪鼠牛虎兔龙蛇马羊猴鸡狗猪鼠牛虎兔龙蛇马羊

print(chinese_zodiac + 'abcd')  # 猴鸡狗猪鼠牛虎兔龙蛇马羊abcd
# 序列重复
print(chinese_zodiac * 3)  # 猴鸡狗猪鼠牛虎兔龙蛇马羊猴鸡狗猪鼠牛虎兔龙蛇马羊猴鸡狗猪鼠牛虎兔龙蛇马羊


