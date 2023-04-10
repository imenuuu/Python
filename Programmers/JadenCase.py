s = input()

value = s.split()

answer=""
for i in value:
    if i[0].isalpha():
        answer += i.title() + " "
    else:
        answer += i.lower()+ " "

answer=answer.rstrip()

print(answer)