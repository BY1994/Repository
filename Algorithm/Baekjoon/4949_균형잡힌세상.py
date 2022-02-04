"""
4949 균형잡힌 세상
"""

stack = [0] * 101

while True:
    string = input()
    if string == '.':
        break
    sp = 0
    for s in string:
        if s == '(':
            stack[sp] = 1
            sp += 1
        elif s == '[':
            stack[sp] = 2
            sp += 1
        elif s == ')':
            if sp < 1 or stack[sp-1] != 1:
                print("no")
                break
            else:
                sp -= 1
        elif s == ']':
            if sp < 1 or stack[sp-1] != 2:
                print("no")
                break
            else:
                sp -= 1
    else:
        if sp > 0:
            print("no")
        else:
            print("yes")

# 여러 줄에 걸쳐 쓴 거를 아래 처럼 짧게 쓸 수도 있음
# https://www.acmicpc.net/source/14057717
"""
from sys import stdin, stdout

def isvalid(s):
    stack = []
    for c in s:
        if c in '([':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                return False
        elif c == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack

strings = stdin.readlines()
strings.pop()
for string in strings:
    stdout.write("yes\n" if isvalid(string) else "no\n")
"""
