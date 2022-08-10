/*
10807 개수 세기

java 배열 선언 new 이용
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=heartflow89&logNo=220950491600

배열을 0으로 초기화할 필요가 없다. 생성하면 무조건 0임
https://www.delftstack.com/ko/howto/java/java-initialize-array-elements-to-zero/
*/

import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        int n, v;
        int array[] = new int[202];
        
        Scanner myObj = new Scanner(System.in);
        n = myObj.nextInt();
        
        for (int i = 0; i < n; i++) {
            array[myObj.nextInt() + 100] += 1;
        }
        
        v = myObj.nextInt();
        
        System.out.println(array[v+100]);
    }
}