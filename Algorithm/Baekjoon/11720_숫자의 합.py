""" 
백준 알고리즘 11720
백준 Online Judge - 문제 - 단계별로 풀어보기 - for문 사용해보기 - 숫자의 합

문제)
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력)
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
5
54321

출력)
입력으로 주어진 숫자 N개의 합을 출력한다.
15

최초 작성 2019.01.10 PBY
"""

length = int(input())
number = input()
result = 0

for i in number:
    result += int(i)
print(result)

# visual studio는 실행시 ctrl + f5