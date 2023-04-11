import collections

data = list(input().rstrip())
data = sorted(data)

data_element = collections.Counter(data)

cnt = 0
mid = ''

word_list={}

for word, j in list(data_element.items()):
    if j % 2 == 1:
        mid = word
        if j/2>1:
            word_list[word] = j-1
        cnt += 1
    else:
        word_list[word]=j
    if cnt >= 2:
        print("I'm Sorry Hansoo")
        exit()
palindrome = []
for word, j in word_list.items():
    palindrome.append(word*int(j/2))

print(''.join(palindrome)+mid+''.join(palindrome[::-1]))


