import random

f = open("2729_input.txt", "w")
f.write('1000\n')
#print(1000)
for i in range(1000):
    lenA = random.randint(1, 80)
    lenB = random.randint(1, 80)
    for j in range(lenA):
        f.write('0' if random.randint(0, 1) == 0 else '1')
        #print('0', end='') if random.randint(0, 1) == 0 else print('1', end='')
    f.write(' ')
    #print(' ', end='')
    for j in range(lenB):
        f.write('0' if random.randint(0, 1) == 0 else '1')
        #print('0', end='') if random.randint(0, 1) == 0 else print('1', end='')
    f.write('\n')
    #print()
f.close()
