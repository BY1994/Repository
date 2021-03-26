"""
result : FAIL
"""

for tc in range(1, int(input())+1):
    ans = 0
    N, D = map(int, input().split())
    cakes = dict()
    cake_input = input().split()
    for _ in range(N):
        cake = int(cake_input[_])
        if cakes.get(cake):
            cakes[cake] += 1
        else:
            cakes[cake] = 1

    # 제일 많은 케이크 크기 기준으로 자르기

    cakes = list(cakes.items())
    cakes.sort(key = lambda x: x[1], reverse = True)

    cut = 0
    for cake in range(len(cakes)):
    # 근데 필요한 케이크보다 더 큰 케익이 부족하면

        if cakes[cake][1] >= D:
            ans = cut
            break
        else:
            temp = 0
            tempcut = 0
            flag = 0
            for bigger in range(0, cake):
                # 나보다 큰 거 자르면 이 크기 나오는지
                temp += bigger // cakes[cake][0]
                tempcut += bigger // cakes[cake][0] - ~bool(bigger % cakes[cake][0])
                if temp + cakes[cake][1] == D or temp + cakes[cake][1] -1 == D:
                    # 최소 크기로만 저장하기...
                    ans = cut + tempcut
                    flag = 1
                    break
                elif temp + cakes[cake][1] > D:
                    ans = cut + D - temp
                    flag = 1
                    break
            if flag == 1:
                break
        cut += 1
    else:
        ans = D
    # 정렬된 순으로 내려가면서 더 작은 애
    
    print("Case #%d: %d" %(tc, ans))
