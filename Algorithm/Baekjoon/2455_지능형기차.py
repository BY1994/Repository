"""
2455 지능형 기차
"""

people = 0
m = 0
for i in range(4):
    down, up = map(int, input().split())
    people += (up-down)
    if m < people:
        m = people
print(m)

# 숏코딩
"""
l=[0];exec('l+=[l[-1]-eval(input().replace(" ","-"))];'*4);print(max(l))
"""
