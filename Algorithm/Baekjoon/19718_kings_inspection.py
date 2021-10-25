"""
19718 King's Inspection

# case 1 => 223

# case 2 => 124 or 122
(num[1] - num[0])*2 + num[2] - num[1]
"""


num = [int(input()) for _ in range(3)]
num.sort()
print(num[1] + num[2] - num[0]*2)

# 헉 하나로 합칠 수 있음
# case 2로 다 커버됨....
# 잘못 생각함...

"""
num = [int(input()) for _ in range(3)]
num.sort()

# 1 case
if num[0] == num[1]:
    print(num[2] - num[1])
else:
    print(num[1] + num[2] - num[0]*2)
"""
