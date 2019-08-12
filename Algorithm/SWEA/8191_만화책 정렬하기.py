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

# 1권 2권이 멀리 떨어져있는 경우 2번 훑어야 한다고 생각했는데, 1번만 훑는 것이었다.
# 통과! 런타임 에러가 또 났는데 배열을 전역변수로 설정해서 해결하였다.
ans = 0
N = int(input())
Books = list(map(int, input().split()))
Book_Check = [0] * (N+1)
for i in range(N):
    if Book_Check[Books[i]-1] == 0: # 내 앞에 내 이전 수가 없으면
        ans += 1
    Book_Check[Books[i]] = 1
print(ans)
        

# c로 변환해서 제출하였으나 재귀함수 에러인지 runtime error로 실패
"""
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
"""
