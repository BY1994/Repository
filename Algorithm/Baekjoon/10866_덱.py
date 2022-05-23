"""
10866 덱

시간초과가 났는데 ans 문자열 배열에 합해서 마지막에 한 번에 출력하는 거로 통과했다.
"""

ans = ""
deq = [0]*20010
fr = 10000
re = 10001

for i in range(int(input())):
    cmd = input()
    if cmd[:4] == "push":
        cmd, value = cmd.split()
        value = int(value)

    if cmd == "push_front":
        deq[fr] = value
        fr -= 1
    elif cmd == "push_back":
        deq[re] = value
        re += 1
    elif cmd == "pop_front":
        if fr+1 == re:
            ans += "-1\n"
        else:
            fr += 1
            ans += str(deq[fr])+"\n"
    elif cmd == "pop_back":
        if fr+1 == re:
            ans += "-1\n"
        else:
            re -= 1
            ans += str(deq[re])+"\n"
    elif cmd == "size":
        ans += str(re-fr-1) + "\n"
    elif cmd == "empty":
        if fr+1 == re:
            ans += "1\n"
        else:
            ans += "0\n"
    elif cmd =="front":
        if fr+1 == re:
            ans += "-1\n"
        else:
            ans += str(deq[fr+1]) + "\n"
    elif cmd =="back":
        if fr+1 == re:
            ans += "-1\n"
        else:
            ans += str(deq[re-1]) + "\n"

print(ans, end="")
"""
deq = [0]*20010
fr = 10000
re = 10001

for i in range(int(input())):
    cmd = input()
    if cmd[:4] == "push":
        cmd, value = cmd.split()
        value = int(value)

    if cmd == "push_front":
        deq[fr] = value
        fr -= 1
    elif cmd == "push_back":
        deq[re] = value
        re += 1
    elif cmd == "pop_front":
        if fr+1 == re:
            print(-1)
        else:
            fr += 1
            print(deq[fr])
    elif cmd == "pop_back":
        if fr+1 == re:
            print(-1)
        else:
            re -= 1
            print(deq[re])
    elif cmd == "size":
        print(re - fr-1)
    elif cmd == "empty":
        if fr+1 == re:
            print(1)
        else:
            print(0)
    elif cmd =="front":
        if fr+1 == re:
            print(-1)
        else:
            print(deq[fr+1])
    elif cmd =="back":
        if fr+1 == re:
            print(-1)
        else:
            print(deq[re-1])
"""
