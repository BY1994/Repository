for tc in range(int(input())):
    cloth = {}
    for i in range(int(input())):
        name, ctype = input().split()
        if ctype in cloth:
            cloth[ctype] += 1
        else:
            cloth[ctype] = 1

    result = 1
    for ctype in cloth:
        result *= (cloth[ctype]+1)

    print(result-1)
