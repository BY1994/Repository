"""
9501 꿍의 우주여행
"""

for t in range(int(input())):
    N, D = map(int, input().split())
    ans = 0
    for _ in range(N):
        v, f, c = map(int, input().split())
        if f >= D * c / v:
            ans += 1
    print(ans)

"""
import sys
input = sys.stdin.readline
만 추가하면 속도 개선될 듯
ex. https://www.acmicpc.net/source/13310896
"""

# 나누기 안 해도 됨
# https://www.acmicpc.net/source/2918618
"""
#include<stdio.h>

int main(){
	int t;
	for(scanf("%d",&t);t--;){
		int n, d, c, v, f, cnt=0;
		for(scanf("%d%d", &n, &d); n--;){
			scanf("%d%d%d", &v, &f, &c);
			if(d*c<=v*f)cnt++;
		}
		printf("%d\n", cnt);
	}
	return 0;
}
"""
