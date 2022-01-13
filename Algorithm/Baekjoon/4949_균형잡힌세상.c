// _%c로는 안 될 것 같다. .을 마지막에 처리해야해서...
#include <stdio.h>
int N;
char s[101];
int stack;
char temp;
int ans = 1;
int sentence = 0;

int main(void) {
  // 여기 처리 잘못됨... 인풋이 한 번으로 끝나는게 아님...
    for (;;)
    {
      scanf(" %c", &temp);
      if (temp == '.') break;

      if (ans == 0) continue;

      if (temp > ']' || temp < '(') continue;
      else if ('[' > temp && temp > ')') continue;
      else
      {
        if (temp == '(' || temp == '[') {s[stack++] = temp;}
        else 
        {
          stack--;
          if (stack < 0) ans = 0; // break;
        int diff = temp - s[stack]; 
        if (diff == 1 || diff == 2) continue;
        else {ans = 0;} //stack++; }
        }
      }
    }

    if (ans && stack == 0) printf("yes\n");
    else printf("no\n");

  return 0;
}

/*
각 input들이 .으로 종료되고, 마지막으로 전체 데이터 입력에 대한 최종 종료도 .으로 종료된다는 점이 현재 번역본에는 반영되어있지 않은 것 같습니다. 


원문

The input consists of one or more lines, each of which being a dataset. A dataset is a string that consists of English alphabets, space characters, and two kinds of brackets, round (“( )”) and square (“[ ]”), terminated by a period. You can assume that every line has 100 characters or less. The line formed by a single period indicates the end of the input, which is not a dataset.



현재 번역﻿
하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.

입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.
*/