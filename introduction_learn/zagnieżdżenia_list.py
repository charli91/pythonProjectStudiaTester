example_list = ['ex', 12.34, 312, 'abc', 'dwanaście']
print(example_list)
# ['ex', 12.34, 312, 'abc', 'dwanaście']
print(example_list[2]) # drukuje element o indeksie 2
# 312

example_list.append('next element')
print(example_list)
# ['ex', 12.34, 312, 'abc', 'dwanaście', 'next element']

example_list.append(['one more', 'list', True, 3])
print(example_list)
# ['ex', 12.34, 312, 'abc', 'dwanaście', 'next element', ['one more', 'list', True, 3]]

print(example_list[6])
# ['one more', 'list', True, 3]
print(example_list[6][0])
# one more

example_list[6].append('another more')
print(example_list)
# ['ex', 12.34, 312, 'abc', 'dwanaście', 'next element', ['one more', 'list', True, 3, 'another more']]

example_list[6].append(['312.33', 'more', 'key', 312.4555])
print(example_list)
# ['ex', 12.34, 312, 'abc', 'dwanaście', 'next element', ['one more', 'list', True, 3, 'another more', ['312.33', 'more', 'key', 312.4555]]]

print(example_list[6][4][0])
# a
# wyszła pierwsza litera słowa another more
print(example_list[6][5][0])
# 312.33