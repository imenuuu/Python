def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in range(len(reserve)):
        if reserve[i] not in lost:
            print(lost)
            if reserve[i] + 1 in lost:
                answer += 1
                lost.remove(reserve[i] + 1)
            elif reserve[i] - 1 in lost:
                answer += 1
                lost.remove(reserve[i] - 1)
        else:
            answer+=1

    return answer


print(solution(13, [1, 2, 5, 6, 10, 12, 13], [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]))
