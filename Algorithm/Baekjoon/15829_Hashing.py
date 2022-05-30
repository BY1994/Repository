"""
15829 Hashing

ar^i 일 때 r^i 부분을 정직하게 구현
"""
L = int(input())
string = input()

ans = 0
for i in range(L):
    cur = (ord(string[i]) - 96)
    for j in range(i):
        cur = (cur*31) % 1234567891
    ans = (ans + cur) % 1234567891
print(ans)
