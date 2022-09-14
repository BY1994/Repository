"""
1485 정사각형

기하학

바깥에 4점을 연결해서 만든 변의 길이가 같은지만 봤더니 틀렸다
=> 마름모나 평행사변형 등 정사각형이 아닌 다른 도형이 만들어지는 것으로 보인다.
내부에 대각선 길이까지 같은지 확인하니까 맞았다.

혹은 직교나 cos 등을 이용해서 90 도인지 확인하는 방법도 가능할 것 같다.

네 점을 무조건 바깥 방향으로 연결하기 위해서 정렬을 하고 양 끝점을 잡아서 선을 그었는데,
반례는 없는 듯하다.

1등 풀이 이해 안 됨...
"""

# 대각선 길이 확인 추가
def get_len(x, y):
    return (x[0] - y[0])**2 + (x[1] - y[1])**2

for tc in range(int(input())):
    coord = []
    length = [0]*4
    for c in range(4):
        coord.append(list(map(int, input().split())))
    coord.sort(key = lambda x: (x[0], x[1]))
    
    length[0] = get_len(coord[0], coord[1])
    length[1] = get_len(coord[0], coord[2])
    length[2] = get_len(coord[3], coord[1])
    length[3] = get_len(coord[3], coord[2])

    flag = 1
    for l in range(3):
        if length[l] != length[l+1]:
            flag = 0
            break

    if flag:
        if get_len(coord[1], coord[2]) != get_len(coord[0], coord[3]):
            flag = 0

    print(flag)

# 마름모, 평행사변형 등을 못 잡아내는 코드
"""
import math

def get_len(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

for tc in range(int(input())):
    coord = []
    length = [0]*4
    for c in range(4):
        coord.append(list(map(int, input().split())))
    coord.sort(key = lambda x: (x[0], x[1]))
    
    length[0] = get_len(coord[0], coord[1])
    length[1] = get_len(coord[0], coord[2])
    length[2] = get_len(coord[3], coord[1])
    length[3] = get_len(coord[3], coord[2])

    for l in range(3):
        if length[l] != length[l+1]:
            print(0)
            break
    else:
        print(1)
"""

# 1등 풀이
# https://www.acmicpc.net/source/14097780
"""
#include <cstdio>
#include <algorithm>

long long x[4],y[4],s[6];

int main ()
{
	int i,j,k,t;

	scanf ("%d",&t);
	while (t--)
	{
		for (i=0;i<4;i++)
			scanf ("%lld%lld",x+i,y+i);
		for (k=i=0;i<4;i++)
			for (j=i+1;j<4;j++)
				s[k++]=(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]);
		std::sort (s,s+6);
		printf ("%d\n",s[0]==s[3]&&s[4]==s[5]);
	}
}
"""
