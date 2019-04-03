"""BOJ"""
"""
1074_Z

2019.04.03 PBY 최초작성

1. 재귀로 만들려고 했더니 3만 x 3만 배열은 메모리 초과가 났다. (2**15는 로컬에서 안 돌아가길래 시간 초과가 날 거라고 생각했다) => 실패!
2. 크게 만들고 거꾸로 들어가는 것을 생각했다. => 성공!
8 x 8 을 기본으로 그려보았다. 0 ~ 63 까지 숫자가 들어있을 때, 내가 왼쪽 위에 해당하면 0~15가 들어있고,
오른쪽 위에 해당하면 16에서 31에 해당하고, 왼쪽 아래면 32~47, 오른쪽 아래면 48~63에 해당한다.
그것을 찾아가려면 4 x 4 를 계속 더하고 빼줘야하기 때문에 공식이 복잡해보이게 되었다.
"""

# 수학적으로 접근해보기

def smallZ(N, start, end, r, c):
#    print(N, start, end)
    if end - start == 3:
#        print(r, c)
        print(default[r][c]+start)
    else:
        if c >= (2**N)//2:
            c -= (2**N)//2
            start += (2**(N-1))**2
        else:
            end -= (2**(N-1))**2
        if r >= (2**N)//2:
            r -= (2**N)//2
            start += ((2**(N-1))**2)*2
        else:
            end -= ((2**(N-1))**2)*2
        # r, c, start, end 업데이트 끝났으면
        smallZ(N-1, start, end, r, c)

N, r, c = map(int, input().split())
start = 0
end = 4**N-1
default = [[0, 1], [2, 3]]
if end - start == 3:
    print(default[r][c])
else:
    smallZ(N, start, end, r, c)
#    print(smallZ(N, start, end, r, c))

# 메모리 초과
"""
def expand(cur, depth):
    global pattern
    # pattern을 붙여나간다.
    if cur == depth:
        return

    add = 4**cur # 4
    # pattern을 오른쪽, 왼쪽 아래, 오른쪽 아래에 붙여간다.
    pattern = [[pattern[i][j] for j in range(2**cur)]+[pattern[i][j]+add for j in range(2**cur)] for i in range(2**cur)]
    # pattern 2를 붙였음
    # 그 밑에 add*2를 한 걸 더 붙여나감
    add2 = add*2
    pattern2 = [[pattern[i][j] + add2 for j in range((2**cur)*2)] for i in range(2**cur)]
    # pattern2를 복사
    pattern += pattern2 # 밑에 붙이면 새 패턴 완성
    expand(cur+1, depth)

# input
N, r, c = map(int, input().split())
pattern = [[0, 1], [2, 3]]
if N == 1:
    print(pattern[r][c])
else:
    expand(1,N)
    print(pattern[r][c])
"""