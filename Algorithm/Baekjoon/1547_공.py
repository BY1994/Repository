"""
1547 공

기본 구현 문제

문제 이해를 어렵게 만든 듯
-1 을 출력하는 상황이 있다는 건 문제의 위트를 의도한 것이고,
이동시킬 때 주어지는 X, Y 번호는 컵의 번호여서
그 컵이 있는 위치가 어디인지 매번 찾아야한다 (-> 매번 순차 탐색하지 않고 배열 인덱스로 바로 찾게 구현)
"""

cup_id = [0, 1, 2, 3] # 컵이 있는 위치 (x, y 교환용)
cup_loca = [0, 1, 2, 3] # 로케이션에 무슨 컵이 있는지 (정답 출력용)
M = int(input())
for i in range(M):
    X, Y = map(int, input().split())
    cup_loca[cup_id[X]], cup_loca[cup_id[Y]] = cup_loca[cup_id[Y]], cup_loca[cup_id[X]]
    cup_id[X], cup_id[Y] = cup_id[Y], cup_id[X]

print(cup_loca[1])

# 예제 틀림
# 컵의 위치만 교환하면 안 됨
"""
cup_id = [0, 1, 2, 3]
M = int(input())
for i in range(M):
    X, Y = map(int, input().split())
    cup_id[X], cup_id[Y] = cup_id[Y], cup_id[X]

print(cup_id[1])
"""
