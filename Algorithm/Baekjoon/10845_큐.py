"""
10845 큐

큐 연습

readline 쓰면 마지막에 \n 추가되어서 -1 잘라줘야함
시간초과 나서 readline 꼭 써야할 듯
"""

import sys
input = sys.stdin.readline

q = [0]*100000
qs = 0
qe = 0

N = int(input())
for i in range(N):
    cmd = input()[:-1]

    if cmd == "pop":
        if qs == qe:
            print(-1)
        else:
            print(q[qs])
            qs += 1
    elif cmd == "size":
        print(qe - qs)
    elif cmd == "empty":
        if qs == qe:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if qs == qe:
            print(-1)
        else:
            print(q[qs])
    elif cmd == "back":
        if qs == qe:
            print(-1)
        else:
            print(q[qe-1])
    else:
        #x = int(cmd.split()[1])
        x = int(cmd[5:])
        q[qe] = x
        qe += 1

# https://www.acmicpc.net/source/17633612
"""
#include <stdio.h>
int main() {int q[10000];int*p=q;int s=0;int n,x;char c[6];scanf("%d",&n);
	while (n-->0){scanf("%s",c);switch(c[0]){
		case 'p':switch(c[1]){
		case 'u':scanf("%d",&x);*(p+s)=x;s++;break;
		case 'o':if(s){printf("%d\n",*p);p++;s--;}else printf("-1\n");break;}break;
		case 's':printf("%d\n",s);break;
		case 'e':printf("%d\n",s?0:1);break;
		case 'f':printf("%d\n",s?*p:-1);break;
		case 'b':printf("%d\n",s?*(p+s-1):-1);break;}}}
"""
