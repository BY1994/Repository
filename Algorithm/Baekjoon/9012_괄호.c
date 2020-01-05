#include <stdio.h>
int N;
char string[51];
int stack;

void check_string(char ps[51])
{
  for (int i = 0; ps[i]; i++)
  {
    if (ps[i] == '(') stack++;
    else stack--;

    if (stack < 0) break;
  }
  if (stack == 0) printf("YES\n");
  else printf("NO\n");
}

int main(void) {
  scanf("%d", &N);
  for (int i = 0; i<N; i++)
  {
    stack = 0; // 여러 개 출력하는 문제는 초기화 필요!
    scanf("%s", string);
    check_string(string);
  }
  return 0;
}

// 변수명을 짧게 해도 메모리 줄어들지 않음...
// tg314 님 방식 (for문 안에 조건 넣는 방식 참고)
// 함수를 숏코딩으로 변경해도 메모리 줄어들지 않음...
/*
#include <stdio.h>
int N;
char s[51];
int st;

int main(void) {
  scanf("%d", &N);
  for (int i = 0; i<N; i++)
  {
    scanf("%s", s);
    // 왜 int i = 0, st=0; 형태는 안 되지?
    for (int i = st = 0; s[i] && st >= 0; i++) s[i] == '(' ? (st++) : (st--);
    (st)? printf("NO\n"):printf("YES\n");
  }
  return 0;
}
*/