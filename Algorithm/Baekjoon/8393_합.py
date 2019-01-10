""" 
백준 알고리즘 8393
백준 Online Judge - 문제 - 단계별로 풀어보기 - for문 사용해보기 - 합

문제)
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
3

출력)
1부터 n까지 합을 출력한다.
6

최초 작성 2019.01.10 PBY
"""

number = int(input())
result = 0
for i in range(1, number+1):
    result += i
print(result)    

# visual studio는 실행시 ctrl + f5