"""
BAKJOON ONLINE JUDGE

1000. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력>
1 2

출력>
3
"""

a, b = list(map(int, input().split()))
print(a+b)

# map(적용하고 싶은 함수, 리스트) 를 써주면 각 인자에 적용할 수 있다.
# a, b = 리스트를 적으면 리스트의 인자들을 a 와 b에 저장할 수 있다.
