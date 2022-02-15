"""
4948 베르트랑 공준
"""

prime = [1]*246913
prime[0] = 0
prime[1] = 0

for i in range(2, 246913):
    for j in range(2, 246913):
        if i*j > 246912:
            break
        prime[i*j] = 0

for i in range(246912):
    prime[i+1] += prime[i]

while True:
    n = int(input())
    if n == 0:
        break

    print(prime[2*n] - prime[n])
