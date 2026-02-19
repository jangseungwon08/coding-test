
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
//    상하좌우
    static int[] dr  = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int[][] arr;
    static int m, n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < t; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
//        가로
            m = Integer.parseInt(st.nextToken());
//        세로
            n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            arr = new int[n][m];
            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                int col = Integer.parseInt(st.nextToken());
                int row = Integer.parseInt(st.nextToken());
                arr[row][col] = 1;
            }
            int bugCount = 0;
            Queue<int[]> q = new ArrayDeque<>();
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (arr[i][j] == 1) {
                        q.offer(new int[]{i, j});
                        arr[i][j] = 0;
                        bugCount++;
                    }
                    bfs(q);
                }
            }
            System.out.println(bugCount);
        }
    }
    static void bfs(Queue<int[]> q){
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int r = current[0];
            int c = current[1];
            for (int l = 0; l < 4; l++) {
                int nr = r + dr[l];
                int nc = c + dc[l];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                    if (arr[nr][nc] == 1) {
                        q.offer(new int[]{nr, nc});
                        arr[nr][nc] = 0;
                    }
                }
            }
        }
    }
}