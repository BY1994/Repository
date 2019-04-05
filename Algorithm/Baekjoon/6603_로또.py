"""BOj"""
"""
로또

190405 PBY 최초작성
"""
def lotto(cur, depth, selected):
    global n
    if selected == depth:
        print(' '.join(list(map(str, perm))))
        return
    if cur >= n: # 접근할 수 없는 인덱스면 끝나도록
        return

    used[cur] = True
    perm[selected] = numbers[cur]
    lotto(cur+1, depth, selected+1)
    used[cur] = False
    lotto(cur+1, depth, selected)

while True:
    temp = list(map(int, input().split()))
    n = temp[0]
    if n == 0:
        break
    numbers = temp[1:]
    used = [False] * n
    perm = [0] * 6
    lotto(0, 6, 0)
    print()