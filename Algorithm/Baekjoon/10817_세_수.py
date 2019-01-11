""" 
백준 알고리즘 10817
백준 Online Judge - 문제 - 단계별로 풀어보기 - if문 사용해보기 - 세 수

문제)
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

입력)
첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
20 30 10

출력)
두 번째로 큰 정수를 출력한다.
20

최초 작성 2019.01.11 PBY
"""

numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[1])

# visual studio는 실행시 ctrl + f5