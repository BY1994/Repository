"""
23794 골뱅이 찍기 - 정사각형
"""

N = int(input())
print('@'*(N+2))
for _ in range(N):
    print('@'+' '*N+'@')
print('@'*(N+2))
