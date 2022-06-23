"""
1212 8진수 2진수

진법 변환
"""

numbers = input()
ans = ''
zero = ord('0')
# 맨 앞의 0 제거
ans += bin(ord(numbers[0])-zero)[2:]
# 다음 수부터 계산
for i in range(1, len(numbers)):
    cur = ord(numbers[i]) - zero
    ans += str(cur // 4)
    cur %= 4
    ans += str(cur // 2)
    cur %= 2
    ans += str(cur)

print(ans)

# 룩업 테이블도 가능
"""
char lookuptable[8][3] = {
    {'0', '0', '0'},
    {'0', '0', '1'},
    {'0', '1', '0'},
    {'0', '1', '1'},
    {'1', '0', '0'},
    {'1', '0', '1'},
    {'1', '1', '0'},
    {'1', '1', '1'},
};
"""
