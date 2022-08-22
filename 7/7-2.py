

def binary_search(start, end, target, array):
    if start > end:
        return "None"
    mid = (start+end) // 2
    # 찾은 경우 인덱 스 반환
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(start, mid-1, target, array)
    else :
        return binary_search(mid+1, end, target, array)



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

