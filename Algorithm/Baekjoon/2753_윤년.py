"""
2753 윤년
"""

Y = int(input())
if not Y % 400:
    print(1)
elif not Y % 100:
    print(0)
elif not Y % 4:
    print(1)
else:
    print(0)

# C언어
# https://www.acmicpc.net/source/4588287
"""
#import<cstdio>
main(){int x;scanf("%d",&x);printf("%d",x%4?0:x%100?1:x%400?0:1);}
"""

# Python
# https://www.acmicpc.net/source/17611235
"""
a=int(input())
if a%4==0 and a%100!=0 or a%400==0:
    print(1)
else:
    print(0)
"""
