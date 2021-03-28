'''
2021 Codejam Qualification Round
05_Cheating Detection
'''

# Cheating 하면 답을 맞출 확률이 올라가니까 정답 개수가 제일 높은 사람 선택
# Test Set 1 성공
T = int(input())
P = int(input())

for t in range(T):
    answer = 0
    max_value = 0
    #players = []
    for line in range(100):
        temp = input().count('1')
        if temp > max_value:
            max_value = temp
            answer = line

    print(f"Case #{t+1}: {answer+1}")
    
''' Run Time Error => Input을 잘못 이해

T = int(input())

for t in range(T):
    answer = 0
    max_value = 0
    P = int(input())
    #players = []
    for line in range(100):
        temp = input().count('1')
        if temp > max_value:
            max_value = temp
            answer = line
        #players += [input()]
    print(f"Case #{t+1}: {answer+1}")
'''
