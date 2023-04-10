def sequential_search(n, target, array):
    for i in range(n):
        if array[i]==target:
            return i+1;


print("생성할 원소 개수를 임력한다음 한 칸 띄고 찾을 문자열을 입력하시오")

input_data = input().split()
n = int(input_data[0])
target = input_data[1]


print("앞서 적은 원소 개수만큼 문자열을 입력하세요 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

while(True):
    if(len(array) != n ):
        print("앞 서 적은 원소 갯수와 같지 않습니다. 다시 입력해주세요.")
        array = input().split()
    else:
        break


print ("찾는 문자열의 순서 : ")
print (sequential_search(n, target, array))

