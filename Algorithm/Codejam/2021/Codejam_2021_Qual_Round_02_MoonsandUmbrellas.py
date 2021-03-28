'''
2021 Codejam Qualification Round
02_Moons and Umbrellas

Sample Input
4
2 3 CJ?CC?
4 2 CJCJ
1 3 C?J
2 5 ??J???

(hidden)
1
2 -5 ??JJ??

Sample Output
Case #1: 5
Case #2: 10
Case #3: 1
Case #4: 0

(hidden)
Case #1: -8
'''

# ? 가 연속된 문자라 생각하고 간단하게 짜는 버전
# TC 1, 2 정답
'''
T = int(input())
for t in range(T):
    answer = 0
    x, y, input_list = input().split()
    x = int(x)
    y = int(y)
    my_list = input_list.replace("?", "")
    last = 0
    for i in my_list:
        if last == 'C' and i == 'J':
            answer += x
        elif last == 'J' and i == 'C':
            answer += y
        last = i        
    print(f"Case #{t+1}: {answer}")
'''



#동적 프로그래밍을 생각해서 짜려고 했던 코드

T = int(input())
for t in range(T):
    answer = 0
    x, y, input_list = input().split()
    x = int(x)
    y = int(y)
    c = [0]*1000 # ? 에서 c를 선택하면 여기
    j = [0]*1000 # ? 에서 j를 선택하면 여기
    # ? 를 만날 때마다 두 갈래 선택지로 넘기기
    
# 아래 방법을 포기한 이유는 -100 <= x <= 100 조건 때문에
# 답이 정해져 있는 건 -1로 체크하고, 다음 애가 선택하지 않도록
#    if input_list[0] == 'C':
#        c[0] = -1
#    elif input_list[0] == 'J':
#        j[0] = -1
    input_len = len(input_list)
    
    for i in range(1, input_len):
        if input_list[i-1] == 'C':
            c[i] = c[i-1]
            j[i] = c[i-1] + x
        elif input_list[i-1] == 'J':
            c[i] = j[i-1] + y
            j[i] = j[i-1]
        else:
            # ? 의 경우에는 부모가 C인 거랑 J인 거 중에 cost가 더 작은거
            if (c[i-1] < j[i-1] + y): # CC랑 JC
                c[i] = c[i-1]
            else:
                c[i] = j[i-1] + y

            if (j[i-1] < c[i-1] + x): # JJ랑 CJ
                j[i] = j[i-1]
            else:
                j[i] = c[i-1] + x

    if (input_list[-1] == 'C'):
        answer = c[input_len-1]
    elif (input_list[-1] == 'J'):
        answer = j[input_len-1]
    else: # '?'
        if (c[input_len-1] < j[input_len-1]):
            answer = c[input_len-1]
        else:
            answer = j[input_len-1]
        
    print(f"Case #{t+1}: {answer}")

