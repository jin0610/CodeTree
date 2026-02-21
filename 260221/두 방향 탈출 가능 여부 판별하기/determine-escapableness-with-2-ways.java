import java.util.Scanner;
public class Main {
    public static final int MAX_NUM = 100;
    public static final int DIR_NUM = 2;
    
    public static int n, m;
    public static int[][] grid = new int[n][m];
    public static int[][] visited = new int[MAX_NUM][MAX_NUM];
    
    public static boolean inrange(int x, int y){
        return x >= 0 && x < n && y >=0 && y < m;
    }

    public static boolean canGO(int x, int y){
        if (!inrange(x, y)){
            return false;
        }
        if(visited[x][y] == 1 || grid[x][y] == 0){
            return false;
        }
        return true;
    }
     
    public static void dfs(int x, int y){
        int[] dx = new int[]{1, 0};
        int[] dy = new int[]{0, 1};

        for(int i = 0; i < DIR_NUM; i ++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (canGO(nx, ny)){
                visited[nx][ny] = 1;
                dfs(nx, ny);
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        grid = new int[n][m];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                grid[i][j] = sc.nextInt();

        visited[0][0] = 1;
        dfs(0, 0);

        System.out.println(visited[n - 1][m - 1]);
        // Please write your code here.
    }
}