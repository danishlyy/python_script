import re


def find_main_characters(weapon_name):
    with open('sanguo.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        weapon_count = re.findall(weapon_name, data)  # 在data中匹配name,并返回统计的次数
        # print('兵器 %s 出现了 %s 次' % (weapon_name, len(weapon_count)))
    return weapon_name, len(weapon_count)


weapon_dict = {}

# 读取兵器信息
with open('weapon.txt', encoding='utf-8') as f:
    i = 1
    for line in f:
        if i % 2 == 1:
            print(line.strip('\n'))
            weapon_name, weapon_count = find_main_characters(line.strip('\n'))
            weapon_dict[weapon_name] = weapon_count
        i += 1

# 排序
weapon_sorted = sorted(weapon_dict.items(), key=lambda item: item[1], reverse=True)
# [('大斧', 14), ('丈八點鋼矛', 4), ('雙股劍', 3), ('寶雕弓', 3), ('流星錘', 3), ('青龍偃月刀', 2), ('方天畫戟', 2), ('鋼鞭', 2), ('雙鐵戟', 2), ('短戟', 2)]
print(weapon_sorted[0:10])
