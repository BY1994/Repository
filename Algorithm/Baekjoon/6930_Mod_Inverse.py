"""
6930 Mod Inverse

정수론

pow(2,4)%3
pow(2,4,3)
2의 4승을 3으로 나눈 나머지

상위 답안
(1/x) % m
"""

# x * n = m * ? + 1

x = int(input())
m = int(input())

for i in range(1, 100):
    if (x*i - 1)%m == 0:
        print(i)
        break
else:
    print("No such integer exists.")


# https://www.acmicpc.net/source/53505463
"""
try:
    print(pow(int(input()), -1, int(input())))

except ValueError:
    print("No such integer exists.")
"""
