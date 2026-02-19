import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class Main {
    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        char[][] arr = new char[n][n];
        char[][] mangArr = new char[n][n];
        int rgbCount = 0;
        int rbCount = 0;
        for(int i = 0; i< n; i++){
            String s = br.readLine();
            for(int j = 0; j< n; j++){
                char word = s.charAt(j);
                arr[i][j] = word;
                if(word == 'G'){
                    mangArr[i][j] = 'R';
                }
                else{
                    mangArr[i][j] = word;
                }
            }
        }
        rgbCount = bfs(arr);
        rbCount = bfs(mangArr);
        StringBuilder sb = new StringBuilder();
        sb.append(rgbCount).append(" ").append(rbCount);
        System.out.println(sb.toString());
    }
    static int bfs(char[][] map){
        Queue<int[]> q= new ArrayDeque<>();
        boolean[][] isVisited = new boolean[n][n];
        int count = 0;
        for(int i = 0; i< n; i++){
            for(int j = 0; j< n; j++){
                if(!isVisited[i][j]){
                    q.offer(new int[] {i,j});
                    isVisited[i][j] = true;
//                    for(int li = 0 ; li < n; li++){
//                        System.out.println(Arrays.toString(isVisited[i]));
//                    }
//                    System.out.println();
                    count++;
                    while(!q.isEmpty()){
                        int[] current = q.poll();
                        int r = current[0];
                        int c = current[1];
                        for(int k = 0; k< 4; k++){
                            int nr = r + dr[k];
                            int nc = c + dc[k];
                            if(nr >= 0 && nr < n && nc >= 0 && nc <n){
                                if(map[r][c] == map[nr][nc] && !isVisited[nr][nc]){
                                    q.offer(new int[] {nr,nc});
                                    isVisited[nr][nc] = true;
                                }
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
}