import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static int N, K;
    public static ArrayList<Integer> selectedNums = new ArrayList<>();

    public static void printAnswer(){
        for(int i = 0; i < selectedNums.size(); i++){
            System.out.print(selectedNums.get(i) + " ");
        }
        System.out.println();
    }

    public static void findPermutations(int curridx){
        // 종료 조건 : n개를 모두 뽑은 경우 답을 춫력
        if (curridx == N){
            printAnswer();
            return;
        }

        // 1~k까지의 숫자가 뽑혔을 때의 경우
        for(int i = 1; i <= K; i ++){
            selectedNums.add(i);
            findPermutations(curridx + 1);
            selectedNums.remove(selectedNums.size() - 1);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        K = sc.nextInt();
        N = sc.nextInt();
        // Please write your code here.

        findPermutations(0);
        
    }
}