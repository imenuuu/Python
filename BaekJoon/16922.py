from itertools import *

n = int(input())

ans = []

roma_num = {'I', 'V', 'X', 'L'}

result = list(combinations_with_replacement(roma_num, n))

for i in range(len(result)):
    sum=0
    for j in range(n):
        if result[i][j] == 'I':
            sum += 1
        if result[i][j] == 'V':
            sum += 5
        if result[i][j] == 'X':
            sum += 10
        if result[i][j] == 'L':
            sum += 50
    if sum not in ans:
        ans.append(sum)

print(len(ans))