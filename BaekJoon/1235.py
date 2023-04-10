n=int(input())
array =[input() for i in range(n)]

cnt=1
while 1:
    if len(set(map(lambda x : x[-cnt:], array)))==n:
        print(cnt)
        break
    cnt+=1
