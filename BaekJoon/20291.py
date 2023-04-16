import collections

n = int(input())

file = []

for i in range(8):
    m = list(input().split('.'))
    file.append(m[1])

file_element = collections.Counter(file)

for key, value in sorted(list(file_element.items())):
    print(key+' '+str(value))

