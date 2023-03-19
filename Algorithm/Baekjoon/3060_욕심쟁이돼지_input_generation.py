import random

f = open("3060_input2.txt", "w")
f.write('1000\n')
for i in range(1000):
    #N = random.randint(1, 500000000)
    N = random.randint(1, 500)
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)
    d = random.randint(1, 100)
    e = random.randint(1, 100)

    f.write(f'{N}\n')
    f.write(f'{a} {b} {c} {d} {e}\n')
f.close()
