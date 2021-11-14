n = int(input())
guess = list(map(int, input().split()))


#ans = [-1 for _ in range(4006001)]
ans = []

for i in range(1,1001):
    for j in range(1,1001):
        ans.append(4*i*j + 3*i + 3*j)
        #ans[4*i*j + 3*i + 3*j] = 1

people = 0
for meter in guess:
    if meter in ans:
        people += 1

print(n-people)


# wrong
# 0 부터 시작하면 안 됨, a, b는 무조건 1부
"""
n = int(input())
guess = list(map(int, input().split()))


ans = [-1 for _ in range(4006001)]

for i in range(1001):
    for j in range(1001):
        ans[4*i*j + 3*i + 3*j] = 1

people = 0
for meter in guess:
    if ans[meter] == -1:
        people += 1

print(people)
"""
