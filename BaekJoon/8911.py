n = int(input())
size = []
for i in range(n):

    distance = 0  # 북 = 0 서 = 1 남 = 2 동 = 3
    data = list(input().rstrip())
    num_x = 0
    num_y = 0
    dx=[0]
    dy=[0]

    for j in range(len(data)):
        if data[j] == 'F':
            if distance==0:
                num_y+=1
                dy.append(num_y)
            elif distance == 1:
                num_x+=1
                dx.append(num_x)
            elif distance == 2:
                num_y-=1
                dy.append(num_y)
            elif distance ==3:
                num_x-=1
                dx.append(num_x)

        elif data[j] == 'B':
            if distance==0:
                num_y-=1
                dy.append(num_y)
            elif distance == 1:
                num_x-=1
                dx.append(num_x)
            elif distance == 2:
                num_y+=1
                dy.append(num_y)
            elif distance ==3:
                num_x+=1
                dx.append(num_x)

        elif data[j] == 'L':
            if distance==3:
                distance-=3
            else:
                distance+=1
        elif data[j] == 'R':
            if distance==0:
                distance+=3
            else :
                distance-=1

    min_x = min(dx)
    max_x = max(dx)
    min_y = min(dy)
    max_y = max(dy)
    sum = (max_x-min_x) * (max_y-min_y)
    size.append(abs(sum))

print('\n'.join(map(str, size)))