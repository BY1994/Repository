for tc in range(int(input())):
    ans = 'IMPOSSIBLE'

    # relative distance
    myx, myy = 0, 0
    x, y, directions = input().split()
    px, py = myx+int(x), myy-int(y)

    # convert direction to distance
    for turn in range(len(directions)):
        if directions[turn] == 'S':
            py += 1
        elif directions[turn] == 'N':
            py -= 1
        elif directions[turn] == 'E':
            px += 1
        else:
            px -= 1
            
        if abs(myx-px) + abs(myy-py) <= turn+1:
            ans = turn+1
            break
   
    print("Case #%d:" %(tc+1), ans)


"""
잘못 생각한 경우, 이렇게 하면 최소 거리를 모름
for tc in range(int(input())):
    ans = 'IMPOSSIBLE'

    # relative distance
    myx, myy = 0, 0
    x, y, directions = input().split()
    px, py = myx+int(x), myy-int(y)

    # convert direction to distance
    turns = len(directions)
    py += directions.count('S')
    py -= directions.count('N')
    px += directions.count('E')
    px -= directions.count('W')

    # diff between me and p
    if turns >= abs(myx-px) + abs(myy-py):
        ans = "POSSIBLE"
    
    print("Case #%d:" %(tc+1), ans)
"""
