import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static int[] dr = {-1,0,1,0};
    static int[] dc = {0,1,0,-1};
    static int[][] distance, arr;
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int tc = 1; tc <= T; tc++){
            n = Integer.parseInt(br.readLine());
            arr= new int[n][n];
            distance = new int[n][n];
            for(int i = 0; i< n; i++){
                String s = br.readLine();
                for(int j = 0; j< n; j++){
                    arr[i][j] = s.charAt(j) - '0';
                }
            }
            for(int i = 0; i< n; i++){
                Arrays.fill(distance[i], Integer.MAX_VALUE);
            }
            bfs();
            System.out.println("#" + tc + " " + distance[n-1][n-1]);
        }
    }
    static void bfs(){
        Queue<int[]> q= new ArrayDeque<>();
        q.offer(new int[] {0,0});
        distance[0][0] = 0;
        while(!q.isEmpty()){
            int[] current = q.poll();
            int r = current[0];
            int c = current[1];
            for(int i = 0; i< 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                if(nr >=0 && nr < n && nc >=0 && nc <n) {
//                    현재까지의 최소경로가
                    if (distance[nr][nc] > arr[nr][nc] + distance[r][c]) {
                        distance[nr][nc] = arr[nr][nc] + distance[r][c];
                        q.offer(new int[]{nr, nc, arr[nr][nc]});
                    }
                }
                }
            }
        }
    }
