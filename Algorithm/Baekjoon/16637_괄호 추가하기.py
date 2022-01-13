"""
16637 괄호 추가하기

input)
9
3+8*7-9*2

5
8*3+5

7
8*3+5+2

19
1*2+3*4*5-6*7*8*9*0

19
1*2+3*4*5-6*7*8*9*9

19
1-9-1-9-1-9-1-9-1-9

output)
136
64
66
0
426384
24


음수를 고려안하는 반례 (https://www.acmicpc.net/board/view/40321)
19
2*1-1*1+2*2-9*8-9*9

답
189 = 2x1-1x(1+2)x(2-9)x(-1)x9
3 -> -21 -> 21 - > 189

27 = 2x1-1x(1+2)x2-9x(8-9)x9
6 -> -3 -> 3 -> 27
// 코드: https://www.acmicpc.net/board/view/41866

비슷하게 내가 만들어본 반례
19
3-2*8-9*9+9*8-9*9+9

답
7128 = (3-2*8-9)*(9+9)*(-1)*(18)
972 = ((3-2)*(8-9)*9+9*8-9)*(9+9)
// 코드: https://www.acmicpc.net/board/view/42187

    3-2 * 8 - 9*9 + 9 x 8 - 9 x 9 + 9
[0] 3 1 8   -1 -9  0    0  54  486 494
[1] 3 1 -13 -1 -73 -18  63  18 -18 972


음수 최대값 고려 반례
19
0-9*9*9*9*9*9*9*9*4

-172186884


이 문제에서 고려해야하는 부분

1) N이 1인 경우를 반드시 처리
2) max_value를 0으로 초기화하지 말 것
3) 음수끼리 곱해서 커지는 경우를 고려해야함
 

2019.10.11 PBY
"""

# 틀렸던 이유가 두 가지 있었음
# 1) N이 1인 경우를 처리하지 않음
# 2) max_value를 처음에 0으로 초기화하면 안 됨


# 4개씩 묶어서 비교하면 뒤의 숫자가 () 를 치는 것의 영향이 없다?

# 3+8*7-9 비교
# (3+8)*7-9  3+(8*7)-9  3+8*(7-9)
# 첫번째꺼는 괄호를 치나마나....

# for문으로 하는 것보다 queue로 구현하는 게 나을 듯

def calc(a, b, op):
    if op == "+":
        return int(a)+int(b)
    elif op == "-":
        return int(a)-int(b)
    else:
        return int(a)*int(b)

N = int(input())
equation = input()

# max_value가 - 가장 큰 값으로 초기화되어야
max_value = -10**10

if N > 1:
    queue = [[int(equation[0]), 0, 0], [calc(equation[0], equation[2], equation[1]), 2, 1]]
    qlen = 2
else:
    qlen = 0
    max_value = equation[0]
start = 0

while qlen > 0:
    cur, ind, ans = queue[start]
    start += 1
    qlen -= 1
    
    # 하나 한 거랑 두 개 한 거랑 넣기
    # ind 길이 체크 => 종료 조건
    if ind == N-3:
        cur = calc(cur, equation[N-1], equation[N-2])
        # ind가 N-1에 도달할 때마다 cur값과 max_value를 비교
        if max_value < cur:
            max_value = cur
        continue
    if ind == N-1:
        if max_value < cur:
            max_value = cur
        continue

    # 하나만 계산하거나
    queue.append([calc(cur, equation[ind+2], equation[ind+1]), ind+2, ans])
    # 뒤에 두 개를 먼저 계산하거나
    queue.append([calc(cur, calc(equation[ind+2], equation[ind+4], equation[ind+3]), equation[ind+1]), ind+4, ans+1])

    qlen += 2
    

print(max_value)
