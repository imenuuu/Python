n,m =map(int, input().split())
sum = []

for i in range(n):
    data=list(map(int, input().split()))
    sum.append(min(data))

print(max(sum))


