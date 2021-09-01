"""
2021 Facebook Hackercup
Problem A1

6
ABC
F
BANANA
FBHC
FOXEN
CONSISTENCY

제출할 때 Case: 이렇게 잘못 프린트했더니 나온 에러
Presentation Error
Your submission's output is improperly formatted and could not be evaluated for correctness.
"""

T = int(input())
m = ['A', 'E', 'I', 'O', 'U']
a = [0]*26
norm = ord('A')

for char in m:
    a[ord(char) - norm] = 1


for tc in range (T):
    ans = 0
    s = input()
    temp = [0]*26
    mo = 0
    ja = 0
    max_mo_num = 0
    max_mo = 0
    max_ja_num = 0
    max_ja = 0
    # 이미 통일이면?
    # 모음을 자음으로 바꿨을 때랑
    # 자음을 모음으로 바꿨을 때랑
    # 언제가 더 이득인지 => 자음에서 (모음 거치고) 자음 오려면 2 가 걸려서


    # 자음 중에서 제일 많은 글자, 모음 중에서 제일 많은 글자
    for char in s:
        index = ord(char) - norm
        temp[index] += 1
        if a[index] == 1:
            mo += 1
            if temp[index] >= max_mo_num:
                max_mo = char
                max_mo_num = temp[index]
        else:
            ja += 1
            if temp[index] >= max_ja_num:
                max_ja = char
                max_ja_num = temp[index]

    # 1 자음을 다 모음으로
    # 모음이 없으면? => 값이 0이 되니까 괜찮을 듯
    # 2 모음을 다 자음으로
    #print(f"### left ja {ja} mo {mo} max_mo {max_mo_num}_{max_mo}")
    left = ja + (mo - max_mo_num) * 2
    #print(f"### right mo {mo} ja {ja} max_ja {max_ja_num}_{max_ja}")
    right = mo + (ja - max_ja_num) * 2
    ans = right if left > right else left
        
    print(f"Case #{tc+1}: {ans}")
