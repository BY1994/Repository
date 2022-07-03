"""
1252 이진수 덧셈

2022.05.31 통과 PBY
2022.07.02
이전 풀이는 문제 의도와 맞지 않는 잘못된 풀이였다.
자리수가 80 이므로 아무리 긴 자료형을 써도 더할 수 없다.
직접 덧셈을 구현해야하며, 4bit 가산기 접근법으로도 가능하다.
https://blog.naver.com/sehee519/221317979714
https://kyunstudio.tistory.com/217
https://rosettacode.org/wiki/Four_bit_adder
https://rosettacode.org/wiki/Four_bit_adder/C%2B%2B
"""

a, b = input().split()
anum = 0
bnum = 0
for i in a:
    anum *= 2
    anum += ord(i) - 48
for i in b:
    bnum *= 2
    bnum += ord(i) - 48

print(bin(anum+bnum)[2:])
