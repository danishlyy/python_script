f = open('name.txt')
try:
    for line in f:
        print(line)
finally:
    f.close()


with open('name.txt') as f:
    for line in f:
        print(line)