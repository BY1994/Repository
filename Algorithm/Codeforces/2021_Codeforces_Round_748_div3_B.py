"""
Codeforces #748
"""

for _ in range(int(input())):
    number = input()
    numbers = int(number)
    numbers2 = numbers
    a = 0
    
    # 25 75
    start = 0
    for i in range(len(number)-1, -1, -1):
        if numbers % 10 == 5:
            start = i
            numbers //= 10
            break
        else:
            numbers //= 10
            a += 1
    else:
        a = 20
    
    for i in range(start-1, -1, -1):
        if numbers % 10 == 2 or numbers % 10 == 7:
            numbers //= 10
            break
        else:
            numbers //= 10
            a += 1

    # 50 100
    b = 0
    start = 0
    numbers = numbers2
    for i in range(len(number)-1, -1, -1):
        if numbers % 10 == 0:
            start = i
            numbers //= 10
            break
        else:
            numbers //= 10
            b += 1
    else:
        b = 20

    for i in range(start-1, -1, -1):
        if numbers % 10 == 5 or numbers % 10 == 0:
            numbers //= 10
            break
        else:
            numbers //= 10
            b += 1

    print(b if b < a else a)
    
# 문제 잘못 이해 중간에 있는 000들도 사라지는 거라고 착각함
# 시작 부분만 그런 거고 그런 경우는 문제 풀 때 없음!
"""
for _ in range(int(input())):
    numbers = input()
    a = 0    
    zero = 0
    flag = 0
    # 25 75
    for i in range(len(numbers)-1, -1, -1):
        n = int(numbers[i])
        if flag == 0 and n != 5:
            a += 1
            if n == 0:
                zero += 1
            elif zero > 0:
                a -= zero
                zero = 0
        if flag == 0 and n == 5:
            flag = 1
            zero = 0
            
        if flag == 1 and (n!=2 and n!=7):
            a += 1
            if n == 0:
                zero += 1
            elif zero > 0:
                a -= zero
                zero = 0
    # 50
    b = 0
    flag = 0
    zero = 0
    for i in range(len(numbers)-1, -1, -1):
        n = int(number[i])
        if flag == 0 and n != 0:
            b += 1
            if n == 0:
                zero += 1
            elif zero > 0:
                b -= zero
                zero = 0
        if flag == 0 and n == 0:
            flag = 1
            zero = 0
        if flag == 1 and n != 5:
            
    # 100
"""
