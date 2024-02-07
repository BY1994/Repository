"""
30993 자동차 주차

빨간차 A대, 초록차 B대, 파란차 C대를 N칸 주차장에 주차하는 경우의 수
"""

import math
n,a,b,c=map(int,input().split())
print(math.factorial(n)//(math.factorial(a)*math.factorial(b)*math.factorial(c)))
