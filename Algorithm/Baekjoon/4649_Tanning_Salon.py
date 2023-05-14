"""
4649 Tanning Salon

비트마스킹

자리가 없어서 살롱을 떠나는 사람이 반드시 지금 있는 사람들보다 먼저 떠난다는 조건이 있어서
다행히 bed 처리가 복잡해지지 않았다.
"""

while True:
    _input = input()
    if _input[0] == '0': break
    N, customers = _input.split()
    N = int(N)
    bed, fail, entry = 0, 0, 0
    for i in customers:
        customer = 1 << (ord(i)-65)
        if entry & customer:
            bed -= 1
            entry &= ~customer
        else:
            if bed >= N: fail += 1
            bed += 1
            entry |= customer
    if fail:
        print(f"{fail} customer(s) walked away.")
    else:
        print("All customers tanned successfully.")
