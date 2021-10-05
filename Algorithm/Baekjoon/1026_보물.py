"""
1026 보물

greedy simple math
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

print(sum([A[i]*B[i] for i in range(N)]))

# C언어로 시간 제일 짧은 코드는 버블 정렬
"""
swap(int *a,int *b){
	int t = *a;
	*a = *b;
	*b = t;
}
main() {
	int A[100]={0},B[100]={0},N,i,sum=0;
	scanf("%d",&N);
	for(i=0;i<N;i++) scanf("%d",&A[i]);
	for(i=0;i<N;i++) scanf("%d",&B[i]);
	for(i=0;i<N;i++){
		for(int j=0;j<N-1;j++){
			if(A[j]>A[j+1]) swap(&A[j],&A[j + 1]);
			if (B[j]<B[j+1]) swap(&B[j], &B[j + 1]);
		}
	}
	for(i=0;i<N;i++) sum += (A[i] * B[i]);
	printf("%d",sum);
}
"""

# python 시간 제일 짧은 코드
"""
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
def min(A,B):
    sum = 0
    A.sort()
    for i in A:
        t = max(B)
        sum += i*t
        B.pop(B.index(t))
    return print(sum)
min(A,B)
"""
