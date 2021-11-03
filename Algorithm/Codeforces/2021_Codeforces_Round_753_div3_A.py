"""
Codeforce 753 A
"""

for t in range(int(input())):
    keyboard = input()
    s = input()
    ans = 0
    
    last = keyboard.index(s[0])
    for i in range(1, len(s)):
        cur = keyboard.index(s[i])
        ans += abs(last - cur)
        last = cur
    print(ans)
