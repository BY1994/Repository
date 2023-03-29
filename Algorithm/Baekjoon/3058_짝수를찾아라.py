"""
3058 짝수를 찾아라

수학, 구현, 사칙연산
7개의 자연수 중 짝수의 합과 최솟값 구하기
"""


for tc in range(int(input())):
    num = [x for x in map(int, input().split()) if x%2 == 0]
    print(sum(num), min(num))
