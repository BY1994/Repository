"""
9576 책 나눠주기

회의실 배정하기 그리디류
* 증명 방법 찾아봐야할 듯
풀이 설명 https://steadev.tistory.com/14

반례
https://www.acmicpc.net/board/view/65542
1
3 3
1 3
1 3
2 2
답 3
내 오답 2
"""

# break 를 한 번 빼먹어서 틀렸음
# 테스트한 예제와 반례들로는 검출하지 못했던 실수
for tc in range(int(input())):
    N, M = map(int, input().split())
    request = []
    books = [0]*(N+1)
    for i in range(M):
        a, b = map(int, input().split())
        request.append([a,b])
    handout = 0
    request.sort(key = lambda x: (x[1],x[0]))
    for i in range(M):
        for j in range(request[i][0], request[i][1]+1):
            if books[j] == 0:
                books[j] = 1
                handout += 1
                break
    print(handout)

# 반례 있음
"""
for tc in range(int(input())):
    N, M = map(int, input().split())
    request = []
    for i in range(M):
        a, b = map(int, input().split())
        request.append([a,b])
    book = 0
    handout = 0
    request.sort(key = lambda x: (x[0],x[1]))
    for i in range(M):
        if book >= request[i][0] and book + 1 <= request[i][1]:
            book += 1
            request[i][0] = book
            handout += 1
        elif request[i][0] > book:
            book = request[i][0]
            handout += 1
    print(handout)
"""
