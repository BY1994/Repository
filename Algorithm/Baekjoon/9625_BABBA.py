""" 
9625 BABBA
문제 내용)
상근이는 길을 걷다가 신기한 기계를 발견했다. 기계는 매우 매우 큰 화면과 버튼 하나로 이루어져 있다.
기계를 발견했을 때, 화면에는 A만 표시되어져 있었다. 버튼을 누르니 글자가 B로 변했다. 한 번 더 누르니 BA로 바뀌고, 그 다음에는 BAB, 그리고 BABBA로 바뀌었다. 상근이는 화면의 모든 B는 BA로 바뀌고, A는 B로 바뀐다는 사실을 알게되었다.
버튼을 K번 눌렀을 때, 화면에 A와 B의 개수는 몇 개가 될까?

입력)
첫째 줄에 K (1 ≤ K ≤ 45)가 주어진다.

출력)
첫째 줄에 A의 개수와 B의 개수를 공백으로 구분해 출력한다

최초작성 2019.03.03 PBY
"""

K = int(input())

# 반복문으로 짜서 시간 초과 피하기
n2 = [1,0]
n1 = [0,1]
if K == 0:
    print(1, 0)
elif K == 1:
    print(0, 1)
else:
    for i in range(2, K+1):
        n = [n2[0] + n1[0], n2[1] + n1[1]]
        # 업데이트
        n2 = n1[:]
        n1 = n[:]
    print(n[0], n[1])        

# visual studio는 실행시 ctrl + f5

"""
피보나치 규칙 발견
A 1 0
B 0 1
BA 1 1
BAB 1 2
BABBA 2 3
BABBABAB 3 5
BABBABABBABBA 5 8
BABBABABBABBABABBABAB 8 13
"""

"""
# 함수로 짰을 때 시간초과
def fibo(n):
    if n == 0:
        return (1,0)
    elif n == 1:
        return (0,1)
    return (fibo(n-2)[0] + fibo(n-1)[0], fibo(n-2)[1] + fibo(n-1)[1])

ans = fibo(K)
print(ans[0], ans[1])

"""
