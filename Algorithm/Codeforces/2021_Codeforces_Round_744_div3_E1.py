"""
Codeforces Round #744 (Div.3)

E1

lexicographically: 사전순으로 증가
들어오는 input을 덱에 앞 뒤로 넣는데,
최종 나오는 결과가 가능한 결과들 중 사전순으로 제일 작아야한다.

처음에 사전순 증가만 이해하고
1~n을 print해버렸다...

"""
from collections import deque

tc = int(input())
for _ in range(tc):
    n = int(input())
    array = map(int, input().split())
    mydeq = deque()

    for element in array:
        if mydeq:
            left = mydeq.popleft()
            if left >= element:
                mydeq.appendleft(left)
                mydeq.appendleft(element)
            else:
                mydeq.appendleft(left)
                mydeq.append(element)
        else:
           mydeq.appendleft(element)
    print(*mydeq, sep = " ")
    # print(*range(1, n+1)) # wrong understanding
