import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[][] graph;
    static int count;
    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};
    static int n, m;
    static List<int[]> virusList = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        count = 0;
        for(int i = 0; i< n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                graph[i][j] = Integer.parseInt(st.nextToken());
//                메모리 최적화
                if(graph[i][j] == 2){
                    virusList.add(new int[] {i,j});
                }
            }
        }
        dfs(0);
        System.out.println(count);
    }
    static void dfs(int cnt){
        if(cnt == 3){
//            bfs로직 시작?
            bfs();
            return;
        }
        for(int i = 0; i< n; i++){
            for(int j = 0; j< m; j++){
                if(graph[i][j] == 0){
                    graph[i][j] = 1;
                    dfs(cnt+1);
                    graph[i][j] = 0;
                }
            }
        }
    }
    static void bfs(){
        int cnt = 0;
        int[][] copyArr = new int[n][m];
        for (int i = 0; i < n; i++) {
            for(int j = 0; j< m; j++){
                copyArr[i][j] = graph[i][j];
            }
        }
        Queue<int[]> q = new ArrayDeque<>();
        for(int[] virus : virusList) {
            q.offer(new int[]{virus[0], virus[1]});
        }
            while(!q.isEmpty()) {
                int[] current = q.poll();
                int r = current[0];
                int c = current[1];
                for (int k = 0; k < 4; k++) {
                    int nr = r + dr[k];
                    int nc = c + dc[k];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                        if (copyArr[nr][nc] == 0) {
                            copyArr[nr][nc] = 2;
                            q.offer(new int[]{nr, nc});
                        }
                    }
                }
            }
        for(int i = 0; i< n; i++){
            for(int j = 0; j< m; j++){
                if(copyArr[i][j] == 0){
                    cnt++;
                }
            }
        }
        count = Math.max(cnt , count);
    }
}