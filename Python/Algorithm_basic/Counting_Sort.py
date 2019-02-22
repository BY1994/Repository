def Counting_Sort(A, B, k):
    # A [1 .. n] -- 입력 배열 (1 to k)
    # B [1 .. n] -- 정렬된 배열
    # C [1 .. k] -- 카운트 배열

    C = [0] * k

    for i in range(0, len(B)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

A = [4, 1, 3, 2]
B = [0] * len(A) 
k = 5 # 0~5
Counting_Sort(A, B, k)
print(B)
