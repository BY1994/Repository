"""
1002 터렛

원의 교점의 개수
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=junhyuk7272&logNo=221139170814

반례
1
1 2 3 1 2 3
정답
-1
"""

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = (x1-x2)**2 + (y1-y2)**2
    rsum = (r1+r2)**2
    rsub = (r1-r2)**2

    if dist > rsum:
        print(0)
    elif dist == rsum:
        print(1)
    elif rsub < dist < rsum:
        print(2)
    elif dist == rsub:
        if dist == 0:
            print(-1)
        else:
            print(1)
    elif dist < rsub:
        print(0)

# 틀렸습니다 코드 계산식에서 오차가 났나 생각했다 => 원의 위치 관계를 제대로 고려 x
"""
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        xdiff = (x1-x2)**2
        ydiff = (y1-y2)**2
        dist = (r1+r2)**2
        if xdiff + ydiff == dist:
            print(1)
        elif xdiff + ydiff < dist:
            print(2)
        else:
            print(0)
"""


# https://www.acmicpc.net/source/29060855
"""
		int x1 = 0, y1 = 0, r1 = 0; readInt(x1); readInt(y1); readInt(r1);
		int x2 = 0, y2 = 0, r2 = 0; readInt(x2); readInt(y2); readInt(r2);
		int dist = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
		int t1 = (r1 + r2) * (r1 + r2), t2 = (r1 - r2) * (r1 - r2), t = 0;
		if (dist == 0 && r1 == r2) t = -1;
		else if (t1 > dist && t2 < dist) t = 2;
		else if (t1 > dist && t2 == dist || t1 == dist) t = 1;
		if (t < 0) w[i++] = '-', t = -t;
		w[i++] = t | 48, w[i++] = '\n';
"""

# https://www.acmicpc.net/source/14697561
"""
T=int(input())
import sys
num=sys.stdin.readlines()
for i in num:
    x1,y1,r1,x2,y2,r2=map(int,i.split())
    dist=(((x1-x2)**2)+((y1-y2)**2))**0.5
    if dist>r1+r2: print(0)
    elif dist==r1+r2: print(1)
    elif abs(r1-r2)<dist<r1+r2:print(2)
    elif abs(r2-r1)==dist and r2==r1: print(-1)
    elif abs(r2-r1)==dist: print(1)
    else: print(0)
"""
