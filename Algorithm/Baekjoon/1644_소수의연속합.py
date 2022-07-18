"""
1644 소수의 연속합

투 포인터
"""

N = int(input())
check = [0]*(N+1)
for i in range(2, N+1):
    for j in range(2, N//i+1):
        check[i*j] = 1

prime = []
for i in range(2, N+1):
    if check[i] == 0:
        prime.append(i)

lenp = len(prime)
prime.append(0)
left = 0
right = 0
cur = prime[0]

ans = 0
while left <= right and right < lenp:
    if cur == N:
        ans += 1
        right += 1
        cur += prime[right]
    elif cur < N:
        right += 1
        cur += prime[right]
    else:
        cur -= prime[left]
        left += 1

print(ans)


# left, right 로직 한 줄로 짠 예시 코드
# https://www.acmicpc.net/source/8705431
"""
static int countAns(const int primes[], const int primeN, const int N) {
	int sIdx = 0, eIdx = 0, tempSum = 0, ans = 0;
	
	while (eIdx != primeN) {
		if (N > tempSum) 
			tempSum += primes[sIdx++];
		else if (N < tempSum) 
			tempSum -= primes[eIdx++];
		else {
			tempSum -= primes[eIdx++];
			++ans;
		}
	}
	
	return ans;
}
"""
