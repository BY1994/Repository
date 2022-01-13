for _ in range(int(input())):
    n, l = map(int, input().split())
    numbers = list(map(int, input().split()))
    ans = 0
    for i in range(l):
        one = 0
        zero = 0
        for j in range(n):
            if numbers[j] & 1:
                one += 1
            else:
                zero += 1
            numbers[j] >>= 1

        if one > zero:
            ans |= 1 << i
        else:
            ans |= 0 << i
    print(ans)
        
