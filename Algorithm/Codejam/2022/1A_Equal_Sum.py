"""
python 1A_Equal_Sum_interactive_runner.py python 1A_Equal_Sum_local_testing_tool.py 0 -- python 1A_Equal_Sum.py
"""

def backtracking(cur, _sum, depth):
    global flag, N, total
    if flag > 0:
        return

    if _sum*2 == total:
        flag = depth
        return

    elif _sum * 2 > total:
        return

    for i in range(cur+1, N*2):
        if flag > 0: break
        ans[depth] = numbers[i]
        backtracking(i, _sum+numbers[i], depth+1)
    

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(range(1,N+1))
    print(*numbers)
    numbers.extend(list(map(int, input().split())))
    total = sum(numbers)
    ans = [0]*(N*2)
    flag = 0
    for i in range(N*2):
        if flag > 0: break
        ans[0] = numbers[i]
        backtracking(i, numbers[i], 1)
    print(*ans[:flag])
