import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[][] arr;
    static int[][] distance;
    static int[] dr = {-1,0,1,0};
    static int[] dc = {0,1,0,-1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int idx = 0;
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) return;
            arr = new int[n][n];
            distance = new int[n][n];
            for (int i = 0; i < n; i++) {
                Arrays.fill(distance[i], Integer.MAX_VALUE);
            }
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(distance[o1[0]][o1[1]], distance[o2[0]][o2[1]]));
            pq.offer(new int[]{0, 0});
            distance[0][0] = arr[0][0];
            while (!pq.isEmpty()) {
                int[] current = pq.poll();
                int r = current[0];
                int c = current[1];
                for (int i = 0; i < 4; i++) {
                    int nr = r + dr[i];
                    int nc = c + dc[i];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
//                    현재 최단거리가 업데이트
                        if (distance[nr][nc] > arr[nr][nc] + distance[r][c]) {
                            pq.offer(new int[]{nr, nc});
                            distance[nr][nc] = arr[nr][nc] + distance[r][c];
                        }
                    }
                }
            }
        System.out.println("Problem" + " " + ++idx + ": "+ distance[n-1][n-1]);
        }
    }
}
