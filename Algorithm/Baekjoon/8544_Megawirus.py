"""
8544 Megairus

k 가 2의 지수인데, 512까지 되어서 엄청 큼
=> 파이썬으로 풀이
C라면 이진법으로 수정하는 것까지 들어갈 듯

부모 중 제일 큰 값은 x | (x-1) 로 계산하면 된다고 생각했는데,
그러면 1010.. 이런 식이면 중간에 0 있는게 1로 안 바뀜
=> 아님. 부모 중 제일 큰 값이 아니라 단순 세대 수 출력이었음
가장 큰 세대수를 세대의 가장 마지막 수라고 생각해서 틀림
=> 수정 후 통과
"""

virus = []
k, n = map(int, input().split())
for i in range(n):
    virus.append(int(input()))
for i in range(1,k+1):
    for j in range(1,n):
        if (virus[j] >> i) != (virus[j-1] >> i):
            break
    else:
        #print(2**(k-i)-1)
        print(k-i) # 문제 잘못 이해해서 틀림 # 가장 큰 세대 수
        break
