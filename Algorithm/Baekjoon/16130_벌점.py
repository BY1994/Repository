"""
16130 벌점
"""

for _ in range(int(input())):
    point = 0
    m = 0
    ans = 0
    for i in input():
        if ord(i) >= 65: # A
            val = ord(i)-65+10
        else: # 0
            val = ord(i)-48
        point += val
        temp = point // 10
        if temp == 4:
            print(f"{ans}(weapon)")
            break
        elif temp > 4:
            print(f"{ans}(09)")
            break
        if temp > m:
            ans += temp
            m = temp
    else:
        print(f"{ans}")

# ans 를 찍고
# 추가적으로 weapon 과 09 를 붙여서 찍는 것도 가능
