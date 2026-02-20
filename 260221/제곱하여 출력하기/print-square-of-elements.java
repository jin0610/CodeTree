import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] int_list = new int[N];

        for (int i = 0; i < N; i++){
            int_list[i] = sc.nextInt();
        }

        for (int i = 0; i < N; i++){
            System.out.print(int_list[i]*int_list[i] + " ");
        }
    }
}