/*
2754 학점 계산

java 문자열 처리 연습

string array 받는 방법: .nextLine()
https://www.codegrepper.com/code-examples/java/take+string+array+input+in+java

문자열에서 문자 가져오는 방법: charAt()
https://www.delftstack.com/ko/howto/java/java-string-indexing/
https://devpouch.tistory.com/12
*/
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner myObject = new Scanner(System.in);
        String score = myObject.nextLine();
        double value = 0.0;
        char first = score.charAt(0);
        if (first == 'F') value = 0.0;
        else {
            char second = score.charAt(1);
            if (first == 'A') value = 4.0;
            else if (first == 'B') value = 3.0;
            else if (first == 'C') value = 2.0;
            else if (first == 'D') value = 1.0;

            if (second == '+') value += 0.3;
            else if (second == '-') value -= 0.3;
        }

        System.out.println(value);
    }
}