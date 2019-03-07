"""
2559 수열

2019.03.07 PBY 최초작성
"""

totaldays, stddays = list(map(int, input().split()))
temps = list(map(int, input().split()))

# 기초가 될 sum을 저장해두고,
ans = sum(temps[:stddays])

# max도 저장
maxvalue = ans # 시작점 안 들어가서 한 번 틀렸다 ㅠㅠㅠㅠ!!!

for i in range(stddays, totaldays):
    ans -= temps[i-stddays]
    ans += temps[i]
    if maxvalue < ans:
        maxvalue = ans

print(maxvalue)

"""
# 시간초과 1
빈 리스트를 만들고 append해서 max값을 구하게 했더니 시간 초과가 났다.

totaldays, stddays = list(map(int, input().split()))
temps = list(map(int, input().split()))
tempsum = []
for start in range(totaldays-stddays+1):
    tempsum.append(sum(temps[start:start+stddays]))
print(max(tempsum))

"""

"""
# 시간초과 2
maxvalue를 업데이트하도록 바꾼다고 시간 초과가 해결되는 것이 아니었다!

totaldays, stddays = list(map(int, input().split()))
temps = list(map(int, input().split()))
maxvalue = 0
for start in range(totaldays-stddays+1):
    cur_sum = sum(temps[start:start+stddays])
    if cur_sum > maxvalue:
        maxvalue = cur_sum
print(maxvalue)

# 
메모이제이션을 필요로 하는 문제인가 보다. => 성공!

"""