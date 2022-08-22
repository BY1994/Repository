import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        long A = myObj.nextLong();
        long B = myObj.nextLong();
        System.out.println((A+B)*(A-B));
    }
}