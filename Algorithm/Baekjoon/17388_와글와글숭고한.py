"""
17388 와글와글 숭고한
"""

name = ["Soongsil", "Korea", "Hanyang"]
rate = list(map(int, input().split()))
min_rate = 101
min_ind = 0
sum_rate = 0

for i in range(3):
    if rate[i] < min_rate:
        min_rate = rate[i]
        min_ind = i
    sum_rate += rate[i]

if sum_rate >= 100:
    print("OK")
else:
    print(name[min_ind])
