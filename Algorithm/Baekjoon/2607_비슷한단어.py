"""
2607 비슷한 단어 (AD)

2019-03-18 PBY 최초작성

반례
2
ABA
A
답은 0

https://www.acmicpc.net/board/view/17702

"""

# 반례들을 못 잡으면 그냥 진짜로 구현하는 건 어떨까
# find 써서 그 위치를 빼고 ' ' + ' '  이런 식으로 잘라내기로

N = int(input())
word1 = input()
word1_set = set(word1) # 각 단어별 개수
cnt = 0
for _ in range(N-1):
    word2 = input()
    word2_set = set(word2)
    union = word1_set | word2_set
    count = []
    flag = 0
    for u in union:
        temp = abs(word1.count(u)-word2.count(u))
        if temp > 1:
            break
        elif temp == 1:
            if flag 
            flag = 1
        count.append(temp)
    else:
        if sum(count) <= 2: # 차이가 2개 이하 AB, CB의 경우 차이가 2개일 것.
            cnt += 1
print(cnt)

# 틀렸습니다.
"""
N = int(input())
word1 = input()
word1_set = set(word1) # 각 단어별 개수
cnt = 0
for _ in range(N-1):
    word2 = input()
    word2_set = set(word2)
    union = word1_set | word2_set
    count = []
    for u in union:
        temp = abs(word1.count(u)-word2.count(u))
        if temp > 1:
            break
        count.append(temp)
    else:
        if sum(count) <= 2: # 차이가 2개 이하 AB, CB의 경우 차이가 2개일 것.
            cnt += 1
print(cnt)
"""

"""        
# 이렇게 하면 반례 통과하고 예제 케이스 통과 못함
    if abs(len(word1) - len(word2)) <= 1:
        if word1_set == word2_set: # DOG와 DOOG
            cnt += 1
        elif len((word1_set - word2_set) | (word2_set - word1_set)) == 1:# 단어 하나를 넣거나 빼서 똑같은지 AB와 A
            cnt += 1# 차집합을 둘다 구해서 합집합을 한 개 1개여야함.
        elif len(word1_set-word2_set) == 1 and len(word2_set-word1_set)==1:
            cnt += 1
"""

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
