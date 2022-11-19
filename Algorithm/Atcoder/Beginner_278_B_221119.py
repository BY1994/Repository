H, M = map(int, input().split())
while 1:
    if H - (H % 10) + (M // 10) < 24 and M % 10 + (H % 10)*10 < 60:
        print(H, M)
        break
    else:
        M += 1
        if M >= 60:
            M = 0
            H += 1
            if H >= 24:
                H = 0
