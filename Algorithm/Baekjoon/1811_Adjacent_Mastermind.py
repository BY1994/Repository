"""
1811 Adjacent Mastermind

그리디

# 2. grey 부분에서 두번째 if 문 continue 안 넣어주면
그 아래 if 문까지 거쳐서 grey 가 중복 체크되는 문제 있었다.
주어진 예제로 검출 가능했다.
"""
A = 65

while True:
    arrange = input()
    if arrange[0] == '#':
        break
    black, grey, white = 0, 0, 0
    target, guess = arrange.split()
    n = len(target)
    check = [0] * 51
    count = [0] * 128

    # 1. black
    for i in range(n):
        if target[i] == guess[i]:
            check[i] = 1
            black += 1
        else:
            count[ord(target[i]) - A] += 1

    # 2. grey
    for i in range(n):
        if check[i] == 1:
            continue
        if i - 1 >= 0:
            if target[i] == guess[i-1] and check[i-1] == 0:
                grey += 1
                check[i-1] = 2
                count[ord(target[i]) - A] -= 1
                continue
        if i + 1 < n:
            if target[i] == guess[i+1] and check[i+1] == 0:
                grey += 1
                check[i+1] = 2
                count[ord(target[i]) - A] -= 1

    # 3. white
    for i in range(n):
        if check[i] > 0:
            continue
        if count[ord(guess[i]) - A] > 0:
            count[ord(guess[i]) - A] -= 1
            white += 1

    print(f"{guess}: {black} black, {grey} grey, {white} white")
