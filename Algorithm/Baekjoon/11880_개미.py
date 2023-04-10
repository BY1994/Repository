"""
11880 개미

기하학, 피타고라스 정리

python3 로 제출하면 시간초과
input 받는 시간이 오래 걸리기 때문으로 보임

그림으로 도형을 그려보고, 한번에 답을 찾기는 어려울 것으로 보여
가능한 모든 조합을 구해서 min 값을 찾기로 결정
"""

for t in range(int(input())):
    a,b,c = map(int, input().split())
    print(min((a+c)**2+b**2, (a+b)**2+c**2, (b+c)**2+a**2))
