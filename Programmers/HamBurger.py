def solution(ingredient):
    answer = 0
    burger = [1, 2, 3, 1]
    arr = []
    for i in range(len(ingredient)-1):
        for j in range(0, 4):
            if i+j==len(ingredient):
                break
            arr.append(ingredient[i+j])
        if arr==burger:
            arr.remove(ingredient[0])
            answer+=1

    return answer

print(solution([1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 3, 1, 2, 3, 1, 3, 3, 3, 2, 1, 2, 3, 1]))