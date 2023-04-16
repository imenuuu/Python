import sys

input = sys.stdin.readline
dic = {}

for _ in range(int(input())):
    file_name, extension = (input().rstrip()).split('.')

    if extension not in dic:
        dic[extension] = 1
    else:
        dic[extension] += 1

for key in sorted(dic.keys()):
    print(key, dic[key])