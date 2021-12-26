import math

X = input()
length = len(X)
X = int(X)
ans = X*(1- (1/10)**(10**100)) / (1- 1/10) # 10-1
sub = 0
for _ in range(length):
    sub += (X % 10) *0.1 # 소수점 0.1 만이 아니라 뒤까지 다 써야함
    X //= 10
#    print(sub, (X%10)*0.1)
    
print(math.floor(ans-sub))
#print(ans, sub)

# TLE
"""
X = int(input())
ans = X
while(True):
    if X <= 0: break
    X //= 10
    ans += X
print(ans)
"""
