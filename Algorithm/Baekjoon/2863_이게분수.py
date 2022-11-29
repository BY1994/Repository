"""
2863 이게 분수?

총 4번 돌리게 되고, 분모를 통분함
(1)
1 2
3 4
(2)
3 1
4 2
(3)
4 3
2 1
(4)
2 4
1 3
"""
A, B = map(int, input().split())
C, D = map(int, input().split())

index = 0
value = A*A*B*D + B*A*B*C

cur = C*A*B*C + A*A*C*D
if value < cur:
    index = 1
    value = cur

cur = D*A*C*D + C*B*C*D
if value < cur:
    index = 2
    value = cur

cur = B*C*B*D + D*A*B*D
if value < cur:
    index = 3
    value = cur

print(index)
