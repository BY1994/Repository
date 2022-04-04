"""
1541 잃어버린 괄호

greedy

기호 돌면서 현재 상태에 따라 status 업데이트
기호 돌면서 - 만나면 빼기 시작 -> - 또 만날 때까지
기호가 + 면 계속 더함
"""

expression = input()
len_e = len(expression)
operators = [0]*len_e
oper_num = 0
ans = 0
status = 1

for i in range(len_e):
    if expression[i] == '+':
        operators[oper_num] = i
        oper_num += 1
    elif expression[i] == '-':
        operators[oper_num] = i
        oper_num += 1
operators[oper_num] = len_e
ans += int(expression[:operators[0]])

for i in range(oper_num):
    num = int(expression[operators[i]+1:operators[i+1]])
    if expression[operators[i]] == '-': # - 가 한번이라도 나오면 뒤는 무조건 다 뺄 수 있음
        status = -1
    ans += num * status

print(ans)
