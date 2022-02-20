""" 
백준 알고리즘 2108
백준 Online Judge - 문제 - 단계별로 풀어보기 - 정렬해보기 - 통계학

문제)
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력)
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.

최초 작성 2019.02.27 PBY

# Python Decimal
https://m.blog.naver.com/herbdoc95/221574077380

3
0
0
-1
넣으면 decimal round 값 -0 나옴

dictionary in 체크 때문에 시간초과 나온 것으로 추정됨

업데이트 2022.02.20 PBY
"""
import decimal
import sys
input = sys.stdin.readline
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

num = int(input())
numbers = []

for _ in range(num):
    numbers.append(int(input()))

# 산술평균
# int <- because of -1
print(int(round(decimal.Decimal(sum(numbers)) / decimal.Decimal(num),0)))

# 중앙값
numbers.sort()
print(numbers[num//2])

# 최빈값
count = [0]*8002
for n in numbers:
    count[n+4000] += 1

flag = 0
_max = -1
_max_ind = 0
for n in range(8001):
    if count[n] > _max:
        _max = count[n]
        _max_ind = n-4000
        flag = 0
    elif count[n] == _max and flag == 0:
        _max_ind = n-4000
        flag += 1
print(_max_ind)

# 범위
print(max(numbers)-min(numbers))

# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
