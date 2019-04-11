"""
17134 르모앙의 추측

2019.04.10 PBY 최초작성
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
