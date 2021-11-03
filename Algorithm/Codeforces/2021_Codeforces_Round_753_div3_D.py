"""
Codeforce 753 D

Wrong Answer
"""
# 한번이라도 true 나오면 true를 리턴하도록

def backtracking(value, index):
    global n

    #print(index, value)
    
    if len(numbers[index]) == 0:
        return False

    #if index == n-1:
    #    return True

    for j in numbers[index]:
        if not visited[j]:
            if index == n-1:
                return True
            visited[j] = 1
            ret = backtracking(j, index+1)
            visited[j] = 0

            if ret:
                return True
    else: return False
        

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = input()

    numbers = [[] for _ in range(n)]
    visited = [0] * n
    
    for i in range(n):
        if c[i] == 'B':
            if a[i] > n:
                a[i] = n
            if a[i] < 1:
                continue
            for j in range(a[i]):
                numbers[j].append(i)
        else:
            if a[i] > n:
                continue
            if a[i] < 1:
                a[i] = 1
            for j in range(a[i]-1, n):
                numbers[j].append(i)

    print("YES" if backtracking(0, 0) else "NO")

    
