"""
11294 Numbers

진수 변환
"""

while True:
    name = input()
    if name == '#':
        break
    digit = int(input())
    number = int(input())
    print(name, end=", ")
    print(number, end=", ")
    ans = []
    while number > 0:
        if number % digit > 9:
            ans.append(chr(ord('A') + (number % digit)-10))
        else:
            ans.append(number % digit)
        number //= digit
    print(*ans[::-1],sep='')
