"""
23802 골뱅이 찍기 - 뒤집힌 ㄱ
"""

# 두번째 for 문 N*4 로 바꿀 수 있음!!!!!

N = int(input())
for _ in range(N):
    print('@'*N*5)
for _ in range(N*5 - N):
    print('@'*N)


# https://www.acmicpc.net/source/35955012
"""
n=int(input())
print(('@'*(n*5)+"\n")*n+('@'*n+"\n")*(n*4))
"""
