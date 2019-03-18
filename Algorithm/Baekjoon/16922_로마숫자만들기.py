"""
BJ 16922. 로마 숫자 만들기
SW 7287. 로마 숫자 만들기

2019-03-18 PBY 최초작성
"""

N = int(input())
numbers = []
# 백준 선생님 방법
for i in range(N+1): # 이걸 range(N)으로 해버리면 (0,1)의 경우 1개를 선택 못함
    for v in range(N-i+1):
        for x in range(N-i-v+1):
            l = N - i - v - x
            cur_number = i + v*5 + x*10 + l*50
            if cur_number not in numbers:
                numbers.append(cur_number)
print(len(numbers))


"""
# 아닛 sw는 python을 안 받아주는데!

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = []
    # 백준 선생님 방법
    for i in range(N+1): # 이걸 range(N)으로 해버리면 (0,1)의 경우 1개를 선택 못함
        for v in range(N-i+1):
            for x in range(N-i-v+1):
                l = N - i - v - x
                cur_number = i + v*5 + x*10 + l*50
                if cur_number not in numbers:
                    numbers.append(cur_number)
    print('#{} {}'.format(tc+1, len(numbers)))
"""
