"""
1550 16진수

16진수 10진수로 변환
"""

num = input()
m = 1
ans = 0
for i in num[::-1]:
    if ord(i) >= 65:
        ans += (ord(i)-55) * m
    else:
        ans += (ord(i)-48) * m
    m *= 16
print(ans)


# 파이썬 답안
"""
print(int(input(), 16))
"""

# C언어 답안
"""
main(a){scanf("%x",&a);printf("%d",a);}
"""
