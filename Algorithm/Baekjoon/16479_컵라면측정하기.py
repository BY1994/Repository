"""
16479 컵라면 측정하기

기하학
피타고라스 정리

채점시스템에서 float 결과를 채점할 때
소수점이 엄청 길면 input 을 어떻게 받을까?
"""

K = int(input())
D1, D2 = map(int, input().split())

print(K**2 - ((D1 - D2)/2)**2)
