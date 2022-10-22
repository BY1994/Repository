"""
10101 삼각형 외우기
"""

degree = [0]*3
degree[0] = int(input())
degree[1] = int(input())
degree[2] = int(input())

if sum(degree) != 180:
    print("Error")
else:
    if degree[0] == degree[1] and degree[1] == degree[2]:
        print("Equilateral")
    elif degree[0] != degree[1] and degree[0] != degree[2] and degree[1] != degree[2]:
        print("Scalene")
    else:
        print("Isosceles")
