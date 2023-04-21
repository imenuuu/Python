import sys

n=int(input())

# A 수열 입력 받기
a_Array = list(map(int, sys.stdin.readline().split()))

b_Array = []

for i in range(n):
    b_Array.append(a_Array[i])
# A 수열을 오름차 순으로 정렬
b_Array.sort()

# P 수열 선언
p_array=[]

for i in a_Array:
    # A 수열을 오름차순으로 정렬 한 것을
    p_array.append(b_Array.index(i))
    # 이미 할당한 숫자는 sorted_A에서 -1로 대채해 재탐색되지 않도록 함.
    b_Array[b_Array.index(i)] = -1


for x in p_array:
    sys.stdout.write(str(x)+' ')