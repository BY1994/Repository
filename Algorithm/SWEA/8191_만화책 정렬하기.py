"""
8191 만화책 정렬하기

input)
2
3
3 2 1
6
4 3 5 1 2 6

2019.08.07 PBY 최초작성
"""

# c로 변환해서 제출하였으나 재귀함수 에러인지 runtime error로 실패
def moveBook(baseline):
    global ans, index, N
    ans += 1
    while True:
        if index+1 < N:
            index += 1
            if Books[index] == baseline+1:
                baseline += 1
                continue
            elif Books[index] < baseline + 1:
                moveBook(Books[index])
            else:
                return
        else:
            return
    
for testcase in range(int(input())):
    ans = 0
    index = -1
    N = int(input())
    Books = list(map(int, input().split()))
    while True:
        if index+1 < N:
            index += 1
            moveBook(Books[index])
        else:
            break
    print("#%d %d" %(testcase+1, ans))
