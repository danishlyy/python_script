print(zip((1, 2, 3), (4, 5, 6)))  # <zip object at 0x1027766c0>

# (1,2,3)
# (4,5,6)
for i in zip((1, 2, 3), (4, 5, 6)):
    # (1, 4)
    # (2, 5)
    # (3, 6)
    print(i)

dict_a = {'a': 'aa', 'b': 'bb'}
dict_b = zip(dict_a.values(), dict_a.keys())
print(dict_b)  # <zip object at 0x1066af940>
# {'aa': 'a', 'bb': 'b'}
print(dict(dict_b))
