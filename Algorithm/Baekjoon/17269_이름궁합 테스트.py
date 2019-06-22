"""
17269 이름궁합 테스트

input)
8 14
LEESIYUN MIYAWAKISAKURA

2019.06.22 PBY 최초작성
"""

strokes = {
    'A':3, 'B':2, 'C':1, 'D':2, 'E':4, 'F':3, 'G':1,
    'H':3, 'I':1, 'J':1, 'K':3, 'L':1, 'M':3, 'N':2,
    'O':1, 'P':2, 'Q':2, 'R':2, 'S':1, 'T':2, 'U':1,
    'V':1, 'W':1, 'X':2, 'Y':2, 'Z':1
    }

N, M = map(int, input().split())
A, B = input().split()
names = [0] * (N+M)

for i in range(0, min(N, M)*2, 2):
    names[i] = strokes[A[i//2]]
    names[i+1] = strokes[B[i//2]]

for i in range(min(N, M)*2, N+M):
    if N > M:
        names[i] = strokes[A[-(N+M-i)]]
    else:
        names[i] = strokes[B[-(N+M-i)]]

length = N+M
while length > 2:
    length -= 1
    new_names = [0] * length
    for j in range(length):
        new_names[j] = (names[j] + names[j+1]) % 10
    names = new_names

print(names[0]*10+names[1],'%', sep='')
    
