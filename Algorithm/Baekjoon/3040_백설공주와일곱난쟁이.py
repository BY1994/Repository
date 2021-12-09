"""
3040 백설공주와 일곱 난쟁이
"""

dwarf = [0] * 9
total = 0
for i in range(9):
    dwarf[i] = int(input())
    total += dwarf[i]

a = 0
b = 0
# 2을 제외하면 됨
for i in range(9):
    for j in range(i+1, 9):
        if total - dwarf[i] - dwarf[j] == 100:
            a = i
            b = j
            break

for i in range(9):
    if i == a or i == b: continue
    print(dwarf[i])
