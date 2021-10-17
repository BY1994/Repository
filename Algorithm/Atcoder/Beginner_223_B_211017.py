"""
B String Shifting

일일히 구해도 1000 인풋에 2초라서
시간 제한 안 걸릴 듯
"""

s = input()

min_ = s
max_ = s

for i in range(len(s)-1):
    s = s[-1] + s[:-1]
    if min_ > s:
        min_ = s
    if max_ < s:
        max_ = s

print(min_)
print(max_)
