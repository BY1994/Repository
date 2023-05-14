"""
25166 배고픈 아리의 샌드위치 구매하기

비트마스킹 문제
숏코딩 도전
"""

S,M=map(int,input().split())
if not(S&~1023):print("No thanks")
elif not((S-1023)&~M):print("Thanks")
else:print("Impossible")

# 숏코딩 1등
# https://www.acmicpc.net/source/51002141
"""
a,b=map(int,input().split())
a-=1023
print([['Impossible','Thanks'][a|b==b],'No thanks'][a<1])
"""
