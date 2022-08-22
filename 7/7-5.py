import sys


def binary_search(array, target, start, end):
    # 반복문을 통해 해당 원소를 찾으면 값을 리턴하고 아니라면 None을 리턴한다.
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

print("보유하고 있는 부품 갯수를 입력하세요.")
n = int(input())
print("보유하고 있는 부품 번호를 입력하세요.")
number = list(map(int, sys.stdin.readline().split()))
number.sort()

print("요청받은 부품 갯수를 입력하세요.")
m = int(input())
print("요청받은 부품 번호를 입력하세요.")
requestNumber = list(map(int, sys.stdin.readline().split()))




for i in requestNumber:
    result = binary_search(number, i, 0, n-1)
    if result is not None:
        print("Yes", end=' ')
    else:
        print("No", end=' ')