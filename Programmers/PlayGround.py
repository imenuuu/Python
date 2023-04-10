def solution(price, money, count):

    sum=0

    for i in range(count):
        sum += price*(i+1)

    if sum>money:
        return sum-money

    return 0

print(solution(3,20,4))