"""
12589 Snapper Chain (Small)
12590 Snapper Chain (Large)

구글 코드잼 2010 Qualification Round

맞는 답 vs 틀린 답
1 3
Case #4: ON		Case #4: OFF
Case #5: OFF		Case #5: OFF
1 5
Case #6: ON		Case #6: OFF
Case #7: OFF		Case #7: OFF
1 7
Case #8: ON		Case #8: OFF
Case #9: OFF		Case #9: OFF
1 9
Case #10: ON		Case #10: OFF

Case #117: ON		Case #117: OFF
Case #118: OFF		Case #118: OFF

1 1 이면 ON 임
1 2 이면 OFF
1 3 이면 ON

1은 2^1 - 1 = 1

반례
117 tc
2 15 일 때 정답 on 틀린 답 off

2는 2^2 - 1 = 3
3+1+3+1+3+1+3
= 12 + 3

& mask 하면 맞는 이유
15 = 0b1111
31 = 0b11111
47 = 0b101111

Large 면 N 이 최대 30 이라 long long (2^64) 범위 안에 들어올 것

"""

# input generation
"""
#TC = 1
print(10*100)
for i in range(1, 11):
    for j in range(0, 101):
        #print(TC)
        print(i, j)
        #TC+=1
"""      

# 맞음
"""
for T in range(1, int(input())+1):
    N, K=map(int, input().split())
    Cycle=2**N-1
    if K & Cycle == Cycle:
        print(f'Case #{T}: ON')
    else:
        print(f'Case #{T}: OFF')
"""

# 틀림
"""
for T in range(1, int(input())+1):
    N,K=map(int, input().split())
    Cycle=2**N-1
    Repeat = K // Cycle
    if K == Cycle*Repeat + Repeat-1:
        print(f'Case #{T}: ON')
    else:
        print(f'Case #{T}: OFF')
"""
