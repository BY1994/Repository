"""
20922 겹치는 건 싫어

내가 만든 반례
5 1
1 1 1 1 2
내 오답 1
정답 2
"""

import sys

N, K = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))
p1 = 0
p2 = 0
check = [0]*100001
check[a[p1]] += 1
ans = 1

while p1 <= p2:
    # p2 먼저 옮기고
    p2 += 1
    if p2 >= N:
        break
    check[a[p2]] += 1

    # p1 을 가능한 지점까지 옮기기
    while check[a[p2]] > K:
        check[a[p1]] -= 1
        p1 += 1

    # 답 체크
    if ans < p2-p1+1:
        ans = p2-p1+1

print(ans)

"""
import sys

N, K = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))
p1 = 0
p2 = 0
check = [0]*100001
check[a[p1]] += 1
ans = 1

while p1 <= p2 and p2 < N-1:
    #print(p1, p2, p2-p1+1)
    #print("##", p2+1, check[p2+1])
    if check[a[p2+1]] >= K:
        check[a[p1]] -= 1
        p1 += 1
    else:
        p2 += 1
        #if p2 >= N:
        #    break
        check[a[p2]] += 1
        if ans < p2-p1+1:
            ans = p2-p1+1

print(ans)
"""

# https://www.acmicpc.net/source/36455277
"""
	int st = 0, en = 0, cnt=0, ans=0;
	while (en<n) {
		if (ch[arr[en]] < k) {
			cnt++;
			ch[arr[en]]++;
			en++;
		}
		else {
			cnt--;
			ch[arr[st]]--;
			st++;
		}
		ans = max(ans, cnt);
	}
"""

# https://www.acmicpc.net/source/26604609
"""
MIS = lambda: map(int,input().split())

n, k = MIS()
A = list(MIS())

occ = [0] * 100001
occ[A[0]]+= 1
ans = -1

j = 0
for i in range(n):
    while j < n-1 and occ[A[j+1]] < k:
        j+= 1
        occ[A[j]]+= 1
    ans = max(ans, j-i+1)
    occ[A[i]]-= 1
print(ans)
"""
