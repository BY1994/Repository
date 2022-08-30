/*
16019 Are we there yet?

구간합 문제인데 input 및 output 크기가 고정이라 단순하게 풀이하였다.
java 연습

2차원 배열
https://www.acmicpc.net/source/47560190
string 출력
https://www.acmicpc.net/source/47659865
*/
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner myObj = new Scanner(System.in);
        int array[][] = new int[5][5];
        
        int a = myObj.nextInt();
        int b = myObj.nextInt();
        int c = myObj.nextInt();
        int d = myObj.nextInt();
        
        System.out.println(String.format("0 %d %d %d %d", (a),(a+b),(a+b+c),(a+b+c+d)));
        System.out.println(String.format("%d 0 %d %d %d", (a),(b),(b+c),(b+c+d)));
        System.out.println(String.format("%d %d 0 %d %d", (a+b),(b),(c),(c+d)));
        System.out.println(String.format("%d %d %d 0 %d", (a+b+c),(b+c),(c),(d)));
        System.out.println(String.format("%d %d %d %d 0", (a+b+c+d),(b+c+d),(c+d),(d)));
    }
}