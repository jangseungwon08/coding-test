import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, m;
    static int[][] arr;
    static int count = 0;
    static int[] dr = {-1,0,1,0};
    static int[] dc = {0,1,0,-1};
    static boolean[][] isVisited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr= new int[n][m];
        isVisited = new boolean[n][m];
        for(int i = 0; i< n; i++){
            st=  new StringTokenizer(br.readLine());
            for(int j = 0; j< m; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for(int i = 0; i< n; i++){
            for(int j = 0; j< m; j++){
                if(arr[i][j] == 0 && !isVisited[i][j]) {
                    count++;
                    floodFill(new int[] {i,j});
                }
            }
        }
        System.out.println(count);
    }
    static void floodFill(int[] start){
        int r = start[0];
        int c = start[1];
        isVisited[r][c] = true;
        Queue<int[]> q = new ArrayDeque<>();
        q.offer( new int[] {r,c});
        while(!q.isEmpty()){
            int[] current = q.poll();
            for(int i = 0; i < 4; i++){
                int nr = current[0] + dr[i];
                int nc = current[1] + dc[i];
//                상 넘어가면
                if(nr < 0) nr = n-1;
//                우 넘어가면
                if(nc >= m) nc = 0;
//                하 넘어가면
                if(nr >= n) nr = 0;
//                좌 넘어가면
                if(nc < 0) nc = m-1;
//                이동한 좌표가 0이면
                if(arr[nr][nc] == 0 && !isVisited[nr][nc]){
                    isVisited[nr][nc] = true;
                    q.offer(new int[] {nr,nc});
                }
            }
        }
    }
}