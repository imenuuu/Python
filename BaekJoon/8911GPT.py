n = int(input())
size = []

for i in range(n):

    distance = 0  # 북 = 0 서 = 1 남 = 2 동 = 3
    data = list(input().rstrip())
    pos = [0, 0]  # (x, y) 좌표
    min_x, max_x, min_y, max_y = 0, 0, 0, 0  # 좌표의 최소/최대값

    for j in range(len(data)):
        if data[j] == 'F':
            if distance == 0:
                pos[1] += 1
            elif distance == 1:
                pos[0] -= 1
            elif distance == 2:
                pos[1] -= 1
            elif distance == 3:
                pos[0] += 1
        elif data[j] == 'B':
            if distance == 0:
                pos[1] -= 1
            elif distance == 1:
                pos[0] += 1
            elif distance == 2:
                pos[1] += 1
            elif distance == 3:
                pos[0] -= 1
        elif data[j] == 'L':
            distance = (distance + 1) % 4
        elif data[j] == 'R':
            distance = (distance - 1) % 4

        # 좌표의 최소/최대값 갱신
        min_x = min(min_x, pos[0])
        max_x = max(max_x, pos[0])
        min_y = min(min_y, pos[1])
        max_y = max(max_y, pos[1])

    size.append((max_x - min_x) * (max_y - min_y))

print('\n'.join(map(str, size)))