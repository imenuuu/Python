import sys



print("떡의 개수와 요청한 떡 길이를 띄어쓰기로 구분하여 입력하세요.")

n, m = list(map(int, sys.stdin.readline().split()))
print("떡의 길이를 띄어쓰기로 구분하여 입력하세요.")
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(array)

# 이진 탐색 반복
result = 0
while start<=end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x>mid:
            total +=x-mid
    if total < m :
        end = mid - 1
    else:
        result = mid
        start = mid+1

print(result)