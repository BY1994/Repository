"""
4153 직각 삼각형
"""

while(True):
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        break
    numbers.sort()
    print("right" if numbers[0]**2 + numbers[1]**2 == numbers[2]**2 else "wrong")
    
