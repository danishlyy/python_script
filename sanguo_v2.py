import re


def find_item(name):
    with open('sanguo.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        name_count = re.findall(name, data)  # 在data中匹配name,并返回统计的次数
        # print('主角 %s 出现了 %s 次' % (name, len(name_count)))
    return len(name_count)


# 读取人物信息
name_dict = {}
with open('person.txt') as f:
    for line in f:
        names = line.split('|')
        for name in names:
            name_count = find_item(name)
            name_dict[name] = name_count

# 根据出现次数进行排序
name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)

print(name_sorted[
      0:10])  # [('曹操', 940), ('張飛', 364), ('呂布', 342), ('孫權', 321), ('趙雲', 313), ('劉備', 297), ('司馬懿', 287), ('周瑜', 240), ('馬超', 219), ('黃忠', 189)]
