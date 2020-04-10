counting = [0]*10001
t = int(input())
for _ in range(t):
	counting[int(input())]+=1

for i in range(10001):
	if (counting[i]):
		print(f"{i}\n"*counting[i], end='')
