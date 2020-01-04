#include <stdio.h>

int N;
int sum;
int stack[100001];
int idx;

int main()
{
  int data, i; // for 안에서 쓰는 거랑 메모리 차이 없음
  scanf("%d", &N);
  for (i = 0; i<N; i++)
  {
    scanf("%d", &data);
    if (data) {stack[idx++] = data; sum += data;}
    else {sum -= stack[--idx];}
  }

  printf("%d\n", sum);
}
