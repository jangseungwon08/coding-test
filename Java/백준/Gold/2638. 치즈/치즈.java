import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int time = 0;
    static int[][] arr;
    static int[] dr = {-1,0,1,0};
    static int[] dc = {0,1,0,-1};
    static int n,m;
    static boolean[][] isVisited;
    static Queue<int[]> q = new ArrayDeque<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        isVisited = new boolean[n][m];
        int[] current = new int[2];
        for(int i = 0; i< n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j< m; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
                if(arr[i][j] == 0 && q.isEmpty()){
                   current[0] = i;
                   current[1] = j;
                }
            }
        }
        boolean flag = false;
        while(!flag) {
            bfs(current);
            flag = check();
            time++;
        }
        System.out.println(time);
    }
    static void bfs(int[] curr){
        q.offer(new int[] {curr[0], curr[1]});
        boolean[][] temp = new boolean[n][m];
        int[][] countArr = new int[n][m];
        temp[curr[0]][curr[1]] = true;
        while(!q.isEmpty()){
            int[] current = q.poll();
            int r = current[0];
            int c = current[1];
            for(int i = 0; i< 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                if(nr < 0 || nr >= n || nc < 0 || nc >=m) continue;
//
                if (arr[nr][nc] == 0 && !temp[nr][nc]) {
                    temp[nr][nc] = true;
                    q.offer(new int[]{nr, nc});
                }
                else if (arr[nr][nc] == 1){
                    countArr[nr][nc]++;
                }
            }
        }
        for(int i = 0; i< n; i++){
            for(int j = 0; j< m; j++){
                if(countArr[i][j] >= 2){
                    arr[i][j] = 0;
                }
            }
        }
    }
//     모든 치즈가 녹았는지 확인하는 메서드 -> 1이 있으면 false리턴
    static boolean check(){
        for(int i = 0; i< n; i++){
            for(int j = 0; j< m; j++){
                if(arr[i][j] > 0){
                    return false;
                }
            }
        }
        return true;
    }
}