"""
23253 자료구조는 정말 최고야
힙 자료구조
트리 형태에서 하나씩 힙을 pop 하는 형태를 생각하면 될 것으로 보임
각 더미가 오름차순으로 배열되어있다면 작은 값이 절대 밑에 있을 수 없다는
그리디한 생각으로도 풀이 가능할 것
"""
N,M=map(int,input().split())
ans=True
for i in range(M):
    k=int(input())
    prev = 200000
    for b in map(int, input().split()):
        if b > prev:
            ans=False
            break
        prev=b
print(["No","Yes"][ans])
