# 读取三国人物名字
f = open('person.txt')
print(f.read().split('|'))#['諸葛亮', '關羽', '劉備', '曹操', '孫權', '關羽', '張飛', '呂布', '周瑜', '趙雲', '龐統', '司馬懿', '黃忠', '馬超']

# 读取兵器
weapon = open('weapon.txt')
i = 1
for line in weapon.readlines():
    if i % 2 == 1:
        print(line.strip("\n"))
    i += 1
# 青龍偃月刀
# 丈八點鋼矛
# 鐵脊蛇矛
# 涯角槍
# 諸葛槍
# 方天畫戟
# 長柄鐵錘
# 鐵蒺藜骨朵
# 大斧
# 蘸金斧
# 三尖刀
# 截頭大刀
# 馬岱寶刀
# 古錠刀
# 衠鋼槊
# 丈八長標
# 王雙大刀
# 呂虔刀
# 龍泉劍
# 倚天劍
# 青釭
# 七寶刀
# 雙股劍
# 松紋廂寶劍
# 孟德劍
# 思召劍
# 飛景三劍
# 文士劍
# 蜀八劍
# 鎮山劍
# 吳六劍
# 皇帝吳王劍
# 日月刀
# 百辟寶刀
# 龍鱗刀
# 百辟匕首二
# 鐵鞭
# 鋼鞭
# 四楞鐵簡
# 雙鐵戟
# 諸葛連弩
# 寶雕弓
# 鵲畫弓
# 虎筋弦弓
# 兩石力之弓
# 手戟
# 短戟
# 飛石
# 流星錘
# 銅撾

f3 = open('sanguo.txt',encoding='GB18030')
print(f3.read().replace('\n','')) # 'utf-8' codec can't decode byte 0xa1 in position 0: invalid start byte