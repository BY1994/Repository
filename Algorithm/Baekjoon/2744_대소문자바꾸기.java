/*
2744 대소문자 바꾸기

java string 연습

conv 배열을 char 로 선언했더니, for 문 돌면서 채우는 부분에서
int to char converting error 발생하여서 int 로 변경하였다.

string 의 길이를 확인하는 법: .length()
https://shanepark.tistory.com/327

string formatting방법
https://www.geeksforgeeks.org/java-string-format-method-with-examples/
*/
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int conv[] = new int[150];
        Scanner myObj = new Scanner(System.in);
        String word = myObj.nextLine();
        for (int i = 0; i < 26; i++) {
            conv['A' + i] = 'a' + i;
            conv['a' + i] = 'A' + i;
        }
        for (int i = 0; i < word.length(); i++) {
            System.out.print(String.format("%c", conv[word.charAt(i)]));
        }
        System.out.print("\n");
    }
}