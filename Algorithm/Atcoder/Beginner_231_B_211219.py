S = input()
T = input()

prev = (ord(T[0])-ord('a') - (ord(S[0])-ord('a')) + 26) % 26
for i in range(1,len(S)):
    cur = (ord(T[i])-ord('a') - (ord(S[i])-ord('a')) + 26) % 26
    if prev != cur:
        print("No")
        break
    prev = cur
else:
    print("Yes")
