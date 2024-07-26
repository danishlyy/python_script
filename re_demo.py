import re

p = re.compile('a')
print(p.match('a'))  # <re.Match object; span=(0, 1), match='a'>
print(p.match('b'))  # None

p1 = re.compile('cat')
print(p1.match('caat'))  # None

# .:匹配任意的字符
# ^:匹配以什么开头的
# $:匹配以什么结尾的
# *:匹配前面的字符出现0次或者多次
# +:匹配前面的字符出现1次或者多次
# ?:匹配前面的字符出现0次或者1次
# {m}:匹配前面的字符出现指定次数
# {m,n}:匹配前面的字符出现m~n次
# []: |
# \d:匹配包含数字的 0-9
# \D:匹配不包含数字的
# \s:匹配字符串 a-z
# ():进行分组
# ^$
# .*?:不使用贪婪模式

p2 = re.compile('ca*t')
print(p2.match('caaaat'))  # <re.Match object; span=(0, 6), match='caaaat'>
print(p2.match('ct'))  # <re.Match object; span=(0, 2), match='ct'>

p3 = re.compile('.')
print(p3.match('a'))  # <re.Match object; span=(0, 1), match='a'>

p4 = re.compile('^a')
# 匹配以字母a开头的字符串
print(p4.match('a123'))  # <re.Match object; span=(0, 1), match='a'>
print(p4.match('b123'))  # None

p8 = re.compile('ca{2}t')
print(p8.match('caat'))  # <re.Match object; span=(0, 4), match='caat'>
print(p8.match('caaat'))  # None

p9 = re.compile('ca{1,2}t')
print(p9.match('cat'))  # <re.Match object; span=(0, 3), match='cat'>
print(p9.match('ct'))  # None
print(p9.match('caat'))  # <re.Match object; span=(0, 4), match='caat'>
print(p9.match('caaat'))  # None

# p10 = re.compile('c[abc]t]')
# print(p10.match('cat'))
# print(p10.match('cbt'))
# print(p10.match('cct'))
# print(p10.match('ccdt'))
# print(p10.match('cdt'))
# p7 = re.compile('c?t')
# print(p7.match('at'))
# print(p7.match('ct'))
#
# p6 = re.compile('hello+')
# print(p6.match('o'))
# print(p6.match('wo'))
#
# p5 = re.compile('png$')
# # 匹配以png结尾的字符串
# print(p5.match('hello.png'))
# print(p5.match('hello.jpg'))

# 任意的字符出现3次
r = re.compile('.{3}')
print(r.match('abc'))  # <re.Match object; span=(0, 3), match='abc'>
print(r.match('abcd'))  # <re.Match object; span=(0, 3), match='abc'>
print(r.match('ab'))  # None

#
# x
#

print('\nx\n')
# r 防止转义
print(r'\nx\n')  # \nx\n

r1 = re.compile(r'(\d+)-(\d+)-(\d+)')
print(r1.match('2018-05-10'))  # <re.Match object; span=(0, 10), match='2018-05-10'>

print(r1.match('2024-07-26').group(1))  # 2024
print(r1.match('2024-07-26').group(2))  # 07
print(r1.match('2024-07-26').group(3))  # 26
print(r1.match('2024-07-26').groups())  # ('2024', '07', '26')
year, month, day = r1.match('2024-07-26').groups()
print('year %s' % year)  # year 2024
print('month %s' % month)  # month 07
print('day %s' % day)  # day 26
