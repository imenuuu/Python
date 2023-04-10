n = int(input())

data=list(input().split())

x = 1
y = 1

for i in range(len(data)):
    if data[i]== 'L':
        if y>1:
            y-=1
    if data[i]=='R':
        if y<5:
            y+=1
    if data[i]=='U':
        if x>1:
            x-=1
    if data[i]=='D':
        if x<5:
            x+=1

print(x,' ',y)


