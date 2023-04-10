def solution(n):
    cnt = 0
    answer = calculate(1, cnt, n)
    return answer


def calculate(last_number, cnt, n):
    answer = 0
    for last_number in range(n):
        answer += last_number
        if answer == n:
            cnt+=1
            calculate(last_number, cnt, n)
            break

    if last_number==n:
        return cnt



print(solution(15))
