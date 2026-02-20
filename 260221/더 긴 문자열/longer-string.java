import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String word1 = sc.next();
        String word2 = sc.next();

        if (word1.length() == word2.length()){
            System.out.println("same");
        } else if(word1.length() > word2.length()){
            System.out.println(word1 + " " + word1.length());
        } else{
            System.out.println(word2 + " " + word2.length());
        }
    }
}