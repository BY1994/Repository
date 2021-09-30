"""
17134 르모앙의 추측

2019.04.10 PBY 최초작성
이분탐색 코드
https://velog.io/@madfinger/Binary-Search%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC

2021.09.30 PBY
찾아보니 FFT 알고리즘 문제라고 한다.
FFT 알고리즘 공부 후에 다시 풀이 필요
"""

# 규칙성 찾아서 꼼수 부리려고 했는데 아래 방법은 안 통했다. (규칙성 틀림)
"""
# 소수 미리 찾아두기
check = [False] * 1000001
check[0] = True; check[1] = True
primes = []

# 에라토스테네스의 체
for start in range(2, 1000001):
    for cae in range(start+start, 1000001, start):
        check[cae] = True # 거르기

for start in range(2, 1000001):
    if check[start] == False:
        primes.append(start)
        
for _ in range(int(input())):
    N = int(input())
    target = (N-3)//2
    
    left = 0 
    right = len(primes)-1

    ans = 0
    while left<=right:
        mid = (left+right)//2
        if primes[mid] == target:
            ans = mid
            break
        elif primes[mid]>target:
            right = mid-1
            ans = right
        else :
            left = mid+1

    print(ans + 1) # index 가 곧 개수 (2 ~ 지금 이분탐색으로 찾은 홀수...)
"""

"""
#@profile
def main():
    

    # 소수 미리 찾아두기
    check = [False] * 1000001
    check[0] = True; check[1] = True

    # 에라토스테네스의 체
    for start in range(2, 1000000):
        for cae in range(start+start, 1000000, start):
            check[cae] = True # 거르기
    print(sum(check))        
        
    T = int(input())
    
    for tc in range(T):
        cnt = 0 # 르모앙의 추측 방법의 수
        N = int(input())
        # 홀수 소수 하나를 빼고,
        for prime in range(3, N, 2):
            if check[prime] == False:# 소수이면,
                temp = N - prime
                # 그 temp를 가지고 소수 곱인지 확인
                if temp % 2 == 0 and check[temp//2] == False:
                    cnt += 1
        print(cnt)
  
if __name__ == "__main__":
    main()
"""

# 시간초과
"""
import math

T = int(input())

def checkPrime(number):
    if number == 1: # 1인 경우가 잘못 체크될 수 있다
        return False
    for i in range(2,int(math.sqrt(number)+1)):
        if (number%i == 0): # 나누어 떨어진다는 것은 소수가 아니라는 것!
            return False
    return True
                   
for tc in range(T):
    cnt = 0 # 르모앙의 추측 방법의 수
    N = int(input())
    # 홀수 소수 하나를 빼고,
    for prime in range(3, N, 2):
        if checkPrime(prime) == True:# 소수이면,
            temp = N - prime
            # 그 temp를 가지고 소수 곱인지 확인
            if temp % 2 == 0 and checkPrime(temp//2) == True:
                cnt += 1
    print(cnt)
"""        
   

# 시간초과
"""
T = int(input())

# 소수 미리 찾아두기
check = [False] * 1000001
check[0] = True; check[1] = True

# 에라토스테네스의 체
for start in range(2, 1000000):
    for cae in range(2, 1000000//start+1): # 본인 수는 뛰어넘어야해서 2부터
        check[start*cae] = True # 거르기
        
        


for tc in range(T):
    cnt = 0 # 르모앙의 추측 방법의 수
    N = int(input())
    # 홀수 소수 하나를 빼고,
    for prime in range(3, N, 2):
        if check[prime] == False:# 소수이면,
            temp = N - prime
            # 그 temp를 가지고 소수 곱인지 확인
            if temp % 2 == 0 and check[temp//2] == False:
                cnt += 1
    print(cnt)
        
        
"""
