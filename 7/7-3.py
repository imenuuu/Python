def binary_search(start, end, target, array):
    while start<=end:
        mid = (start+end) // 2
         # 찾은 경우 중간 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은경우 왼쪽 확인
        elif array[mid] > target:
            end = mid-1
        # 중간점의 값보다 찾고자 하는 값이 큰경우 오른쪽확인
        else :
            start = mid+1



print("생성할 원소 개수를 임력한다음 한 칸 띄고 찾을 원소를 입력하시오.")
n, target = list(map(int, input().split()))


print("앞서 적은 원소 개수 만큼 문자열을 입력 하세요 구분은 띄어 쓰기 한 칸으로 합니다.")
array = list(map(int, input().split()))

while(True):
    if(len(array) != n ):
        print("앞 서 적은 원소 갯수와 같지 않습니다. 다시 입력해 주세요.")
        array = list(map(int, input().split()))
    else:
        break

result = binary_search(0, n-1, target, array)

if result == "None" :
    print("원소 존재 하지 않습니다.")
else:
    print("찾는 원소의 순서 : ", result+1)

