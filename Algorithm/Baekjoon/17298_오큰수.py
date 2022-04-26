"""
17298 오큰수

stack
"""

N = int(input())
numbers = list(map(int, input().split()))

stack = [[0 for i in range(2)] for j in range(N)]
ans = [0]*N

stack[0][0] = numbers[0]
sp = 0

for i in range(1, N):
    # 크면 내가 오큰수고
    while sp >= 0 and stack[sp][0] < numbers[i]:
        ans[stack[sp][1]] = numbers[i]
        sp -= 1

    # 작거나 같으면 스택에 추가함
    sp += 1
    stack[sp][0] = numbers[i]
    stack[sp][1] = i

# stack 에 남은 것 꺼내기
while sp >= 0:
    ans[stack[sp][1]] = -1
    sp -= 1
    
for i in range(N):
    print(ans[i], end=" ")

# 이렇게 하면 stack 에 들어있는 순서대로 출력이라
# 정답 순서대로가 아님
"""
N = int(input())
numbers = list(map(int, input().split()))

stack = [0]*N
ans = [0]*N

stack[0] = numbers[0]
sp = 0

for i in range(1, N):
    # 크면 내가 오큰수고
    while sp >= 0 and stack[sp] < numbers[i]:
        #print("stack", stack[:10])
        print(numbers[i], end=" ")
        sp -= 1

    # 작거나 같으면 스택에 추가함
    #print("stack", stack[:10])
    sp += 1
    stack[sp] = numbers[i]

# stack 에 남은 것 꺼내기
while sp >= 0:
    #print("stack", stack[:10])
    print(-1, end=" ")
    sp -= 1
"""
    
    
