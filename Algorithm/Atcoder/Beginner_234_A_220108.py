# 234 A

def f(t):
    return t*t + 2*t + 3

t = int(input())
print(f(f(f(t)+t)+f(f(t))))
