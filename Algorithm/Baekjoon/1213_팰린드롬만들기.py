"""
1213 팰린드롬 만들기

그리디, 문자열
"""
name = input()
n = len(name)
count = [0]*27
middle = -1
A = 65
ans = []
for i in range(n):
    count[ord(name[i]) - A] += 1

for i in range(26):
    if count[i] % 2:
        count[i] -= 1
        if middle != -1:
            print("I'm Sorry Hansoo")
            break
        middle = i
else:
    for i in range(26):
        while count[i]:
            count[i] -= 2
            ans.append(chr(i + 65))
    print(''.join(ans), end="")
    if n % 2:
        print(chr(middle + 65), end="")
    print(''.join(ans[::-1]))
