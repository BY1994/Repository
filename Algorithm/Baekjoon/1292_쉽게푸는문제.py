A, B = map(int, input().split())
arr = [0]*5051

ind = 0
for i in range(1,100):
    for j in range(i):
        arr[ind+j] = i
    ind += j+1

print(sum(arr[A-1:B]))    
