"""
2607 비슷한 단어 (AD)

2019-03-18 PBY 최초작성
"""

from collections import Counter

N = int(input())
std = input()
letters = Counter(std) # 각 단어별 개수
cnt = 0
for _ in range(N-1):
    c = 0
    compare = input()
    compare_letters = Counter(std+compare)
    for letter in compare_letters:
        print(compare_letters)
        compare_letters[letter] -= letters[letter]
        check = abs(compare_letters[letter] - letters[letter])
        print(compare_letters)
        print(letters)
        if check > 1: # 차이가 크면 가능성이 없음
            break
        c += check
        if c > 1: # 누적된 차이가 크면 비슷한 단어 아님
             break
    else: # 문제 없으면
        cnt += 1
print(cnt)

"""
제출 전 질문 검색에서 반례찾음
2
ABCD
CDCD
0이라고 나와야하는데 내 거가 1이 나옴
=> 해결

또다른 반례 찾음
5
AB
A
BB
CB
P

정답은 3인데
내꺼는 A밖에 인식 못함...
AB, BB의 경우를 확인할 수 없는 로직이다. A 개수가 하나 다르고,  B가 2개라서 총 3개의 차이가 나므로 틀리다고 나온다.
"""
