import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        
        System.out.println(minCoins(n));
    }

    public static int minCoins(int n) {
        int count = 0;
        
        while (n >= 0) {
            if (n % 5 == 0) {
                return count + (n / 5);
            }
            n -= 2;
            count++;
        }
        
        return -1;
    }
}