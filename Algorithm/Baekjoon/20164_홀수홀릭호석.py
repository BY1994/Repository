"""
20164 홀수 홀릭 호석

부분 성공
"""

def recur(st, cur):
    global _min, _max

    temp = 0
    for s in st:
        if int(s) % 2:
            temp += 1

    _len = len(st)
    #print("###", st, temp, _len)
    
    if _len <= 1:
        _min = min(_min, cur + temp)
        _max = max(_max, cur + temp)
        return

    if _len <= 2:
        recur(str(int(st[0])+int(st[1])), cur+temp)
        return

    for i in range(_len-2):
        for j in range(i+1, _len-1):
            for k in range(j+1, _len):
                recur(str(int(st[i:j])+int(st[j:k])+int(st[k:])), cur+temp)
            

N = input()
_min = 1000
_max = 0 # 9 * log 9 ?

recur(N, 0)
print(_min, _max)
