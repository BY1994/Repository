/*
2738 행렬 덧셈

java 연습

2차원 배열 생성
https://keichee.tistory.com/423

줄바꿈 없는 print
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=reeeh&logNo=220347297635
(+ ' ') 하니 값이 더해져버린 듯 해서 (+ " ")로 수정하였다.
*/

import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner myObject = new Scanner(System.in);
        int myarray[][] = new int[100][100];
        int N = myObject.nextInt();
        int M = myObject.nextInt();
        for (int n = 0; n < 2; n++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    int temp = myObject.nextInt();
                    myarray[i][j] += temp;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(myarray[i][j] + " ");
            }
            System.out.print("\n");
        }
    }
}