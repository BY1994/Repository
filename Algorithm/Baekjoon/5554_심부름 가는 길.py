"""
5554 심부름 가는 길

시간 출력 문제 (입출력 연습용 문제)

python의 divmod
https://programmers.co.kr/learn/courses/4008/lessons/12732
"""
t = sum([int(input()) for _ in range(4)])
print(t // 60, t % 60, sep='\n')



# 숏코딩 샘플 코드
"""
https://www.acmicpc.net/source/24003061
print(*divmod(sum(map(int,open(0))),60))
"""
