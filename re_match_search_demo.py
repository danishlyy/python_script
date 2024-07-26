import re

r = re.compile(r'(\d+)-(\d+)-(\d+)')
print(r.match('aaa2024-07-28'))  # None

print(r.search('aaa2024-07-28'))  # <re.Match object; span=(3, 13), match='2024-07-28'>

phone = '123-456-789 # 电话号码'
r2 = re.sub(r'#.*$', '', phone)
print(r2)  # 123-456-789
r3 = re.sub(r'\D', '', r2)
print(r3)  # 123456789
