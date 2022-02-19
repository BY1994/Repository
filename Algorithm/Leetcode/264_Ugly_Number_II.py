# 성공 풀이 1
"""
Runtime: 179 ms, faster than 69.97% of Python3 online submissions for Ugly Number II.
Memory Usage: 14 MB, less than 83.97% of Python3 online submissions for Ugly Number II.
"""

"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]

        idx2 = 0
        idx3 = 0
        idx5 = 0

        while len(ans) < n:
            num = min(ans[idx2]*2, ans[idx3]*3, ans[idx5]*5)
            ans.append(num)
            if num == ans[idx2]*2: idx2 += 1
            if num == ans[idx3]*3: idx3 += 1
            if num == ans[idx5]*5: idx5 += 1

        return ans[n-1]
        
problem = Solution()
print(problem.nthUglyNumber(1690))
"""

# 성공 풀이 2
"""
반례
10 -> 12 나와야하는데 15
heappop, heappush 할 때만 자기 자리 찾는 건데,
[n-1] 로 바로 프린트하면 되는 줄 착각함

10 -> 12 나와야하는데 10
똑같은 숫자가 정답 배열에 들어감
인덱스가 밀림
set 으로 넣고 나중에 sort 해야할 듯

Runtime: 380 ms, faster than 21.17% of Python3 online submissions for Ugly Number II.
Memory Usage: 14 MB, less than 73.03% of Python3 online submissions for Ugly Number II.
"""
"""
import heapq

class Solution:    
    def nthUglyNumber(self, n: int) -> int:
        h = []
        ans = []
        heapq.heappush(h, 1)
        while len(ans) < n:
            cur = heapq.heappop(h)
            if len(ans) > 0 and ans[-1] == cur:
                continue
            heapq.heappush(h, cur*2)
            heapq.heappush(h, cur*3)
            heapq.heappush(h, cur*5)
            ans.append(cur)

        return ans[n-1]

problem = Solution()
print(problem.nthUglyNumber(1690))
"""

# 시간이 너무 느리고 1690 은 못 나옴
"""
ans = set()
def dfs(number):
    if number > 100000000:
        return
    ans.add(number)

    dfs(number*2)
    dfs(number*3)
    dfs(number*5)

class Solution:    
    def nthUglyNumber(self, n: int) -> int:
        #min(number*2, number*3, number*5)
        dfs(1)

        ans2 = list(ans)
        ans2.sort()
        return ans2[n-1]

problem = Solution()
print(problem.nthUglyNumber(1690))
"""

# 시간이 너무 느림
"""
import sys
#sys.setrecursionlimit(10000000)

#a = [0] * 100000001
#def dfs(i, j, k, number):
def dfs(number):
    #number = (2**i)*(3**j)*(5**k)
    if number > 10000:
        return
    a[number] = 1
    #dfs(i+1, j, k, number*2)
    #dfs(i, j+1, k, number*3)
    #dfs(i, j, k+1, number*5)
    dfs(number*2)
    dfs(number*3)
    dfs(number*5)

class Solution:
    
        
    def nthUglyNumber(self, n: int) -> int:
        for i in range(100000001):
            a[i] = 0
        #dfs(0, 0, 0, 1)
        dfs(1)
        
        cnt = 0
        for i in range(1, 100000000):
            if a[i] == 1:
                cnt += 1
            if cnt == n:
                return i
        return 0

problem = Solution()
print(problem.nthUglyNumber(1))
"""
