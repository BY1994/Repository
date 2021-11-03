"""
Codeforce 753 B

4마다 돌아오기 때문에
거기서부터 계산하도록 하면 됨

10^14 승
"""

# 짝수 왼쪽, 홀수 오른쪽

# 0 -> 왼쪽으로 1 : -1
# -1 -> 오른쪽으로 2: 1
# 1 -> 오른쪽으로 3: 4
# 4 -> 왼쪽으로 4: 0
# 0 -> 왼쪽으로 5: -5
# -5 -> 오른쪽으로 6: 1
# 1 -> 오른쪽으로 7: 8
# 8 -> 왼쪽으로 8: 0
# 0 ->

# 10 -> 왼쪽으로 1: 9
# 9 -> 오른쪽으로 2: 11
# 11 -> 오른쪽으로 3: 14
# 14 -> 왼쪽으로 4: 10
# 10 -> 오른쪽으로 5: 15
# 15 -> 오른쪽으로 6: 16
# 16 -> 왼쪽으로 7: 9
# 9 -> 오른쪽으로 8: 17

# 1 -> 오른쪽으로 1: 2
# 2 -> 왼쪽으로 2: 0
# 0 -> 왼쪽으로 3: -3
# -3 -> 오른쪽으로 4: 1
# 1 -> 오른쪽으로 5: 6
# 6 -> 왼쪽으로 6: 0
# 0 ->


for t in range(int(input())):
    start, step = map(int, input().split())
    ans = start

    for i in range(step % 4):
        if ans % 2:
            ans += step - (step % 4) + i+1 # i 는 0이니까 1부터 더하도록
        else:
            ans -= step - (step % 4) + i+1
    print(ans)
