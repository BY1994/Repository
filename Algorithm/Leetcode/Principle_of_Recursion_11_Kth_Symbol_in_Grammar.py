"""
K-th Symbol in Grammar

Runtime: 35 ms
Memory Usage: 14 MB
"""

"""
a = [[0,],]

for i in range(1, 10):
    b = []
    for j in range(0, len(a[i-1])):
        b += [a[i-1][j], int(not a[i-1][j])]
    a.append(b)


for i in range(0, 10):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
"""

class Solution:
    def recursion(self, k: int) -> int:
        if k == 1:
            return 0
        if k % 2 == 0: # 짝수
            return int(not self.recursion((k+1)//2))
        else: # 홀수
            return self.recursion((k+1)//2)


    def kthGrammar(self, n: int, k: int) -> int:
        return self.recursion(k)

"""
(k+1)/2 했을 때 소수가 넘어가서 n=3, k=4일 때 0이 나와야하는데 1이 나왔다....
2.5 % 2 는 0.5가 나온다...;;;;
"""
