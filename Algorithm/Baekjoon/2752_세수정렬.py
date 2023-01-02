"""
2752 세수정렬

정렬

bubble sort 구현
"""
numbers = list(map(int, input().split()))
n = len(numbers)

for i in range(n-1, -1, -1):
    ind = 0
    for j in range(1, i+1):
        if numbers[ind] < numbers[j]:
            ind = j
    numbers[ind], numbers[i] = numbers[i], numbers[ind]

print(*numbers)
