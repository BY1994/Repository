T = int(input())
for tc in range(1, T+1):
    E, W = map(int, input().split())
    exercise = []
    total_min = [999]*W
    local_min = [999]*W

    # total overlap
    for e in range(E):
        exercise.append(list(map(int,input().split())))
        for w in range(W):
            total_min[w] = min(total_min[w], exercise[e][w])

    ans = sum(total_min)*2
    for w in range(W):
        local_min[w] = exercise[0][w]-total_min[w]
        ans += local_min[w]

    for e in range(1,E):
        # right next overlap
        for w in range(W):
            ans += abs(local_min[w] - (exercise[e][w]-total_min[w]))
            local_min[w] = exercise[e][w] - total_min[w]

    ans += sum(local_min)
    print(f"Case #{tc}: {ans}")
