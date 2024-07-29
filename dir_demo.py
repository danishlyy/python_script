import os

# 当前位置绝对路径
print(os.path.abspath('.'))  # /Users/liyongyong/ym_project/python_script
print(os.path.abspath('..'))  # /Users/liyongyong/ym_project
print(os.path.exists('/Users'))  # True
print(os.path.isdir('/Users'))  # True
print(os.path.isfile('/Users'))  # False
# 路径链接
print(os.path.join('/Temp/a', 'b/c'))  # /Temp/a/b/c

from pathlib import Path

p = Path('.')
print(p.resolve())  # /Users/liyongyong/ym_project/python_script

pa = Path('/tmp/a')
Path.mkdir(pa, parents=True)
