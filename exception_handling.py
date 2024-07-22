try:
    year = int(input('请输入年份'))
except ValueError:
    print('年份需要输入数字')

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('0不能做除数 %s' % e)  # 0不能做除数 division by zero

try:
    int(input('请输入年份'))  # 请输入年份q123
except (ValueError, KeyError, AttributeError) as e:
    print('%s' % e)  # invalid literal for int() with base 10: 'q123'

try:
    1 / 0
except Exception as e:
    print('%s' % e)  # division by zero

try:
    raise NameError('helloError')
except NameError:
    print('my custom error')  # my custom error


