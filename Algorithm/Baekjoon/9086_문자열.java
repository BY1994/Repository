/*
9086 문자열

Java String 연습
String 길이를 알고 싶을 때 .size() 를 생각했는데, .length()였다.
https://mine-it-record.tistory.com/126

int 입력 후 string 입력 안 되는 현상
nextLine();을 한 번 해주고 string을 입력 받는다. (개행 문자가 안 받아지고 남아있어서)
https://velog.io/@eodnjs467/javaTip1666
*/

import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        int T = myObj.nextInt();
        myObj.nextLine();
        for (int tc = 0; tc < T; tc++) {
            String word = myObj.nextLine();
            System.out.print(word.charAt(0));
            System.out.println(word.charAt(word.length()-1));
        }
    }
}