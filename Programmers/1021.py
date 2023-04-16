from collections import deque

n, m = map(int,input().split())

number = list(map(int, input().split()))

cnt=0

deq = deque([i for i in range(1, n+1)])

for i in number:
    while True:
        if deq[0]==i:
            deq.popleft()
            break
        else:
            if deq.index(i) < len(deq) / 2:  # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 작을때는 왼쪽으로 움직여야 최소
                while deq[0] != i:  # dq의 첫번째 인덱스가 i와 같아질때까지 반복
                    deq.append(deq.popleft())
                    cnt += 1
            else:  # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 클때는 오른쪽으로 움직여야 최소
                while deq[0] != i:
                    deq.appendleft(deq.pop())
                    cnt += 1
print(cnt)

