import collections

data = list(input().rstrip())
data = sorted(data)

data_element = collections.Counter(data)

odd_count = 0
odd_char = ''
palindrome = []

for char, count in list(data_element.items()):
    if count % 2 == 1:
        odd_count += 1
        odd_char = char
    palindrome.extend([char] * (count // 2))

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    palindrome_str = ''.join(palindrome)
    result = palindrome_str + odd_char + palindrome_str[::-1]
    print(result)