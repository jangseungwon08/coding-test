import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        char[][] arr = new char[n][m];
        int[][] count = new int[n][m];
        boolean[][] isVisited = new boolean[n][m];
        int[] dr = {-1,0,1,0};
        int[] dc = {0,1,0,-1};
        st = new StringTokenizer(br.readLine());
        int r1 = Integer.parseInt(st.nextToken()) - 1;
        int c1 = Integer.parseInt(st.nextToken()) - 1;
        int r2 = Integer.parseInt(st.nextToken()) - 1;
        int c2 = Integer.parseInt(st.nextToken()) - 1;
        for(int i = 0; i< n; i++) {
            String s = br.readLine();
            for(int j = 0; j< m; j++) {
                arr[i][j] = s.charAt(j);
            }
        }
        Deque<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[] {r1,c1});
        isVisited[r1][c1] = true;
        while(!dq.isEmpty()) {
            int[] current = dq.pollFirst();
            int r = current[0];
            int c = current[1];
//            뽑은 r과 c가 도착지점이라면
            if (r == r2 && c == c2) {
                System.out.println(count[r][c]);
                break;
            }
            for(int i = 0; i< 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                if(nr >=0 && nr < n && nc >=0 && nc < m) {
                    if(!isVisited[nr][nc]){
                        isVisited[nr][nc] = true;
                        if(arr[nr][nc] == '0'){
                            dq.offerFirst(new int[] {nr,nc});
//                           1을 안만나면 1을 만날 때 까지 count값 유지
                            count[nr][nc] = count[r][c];
                        }
                        else{
//                            1이나 #을 만나면 파동이 멈추기 때문에 한번 더 뛰어야되기 때문에 1 증가
                            dq.offerLast(new int[] {nr,nc});
                            count[nr][nc] = count[r][c] + 1;
                        }
                    }
                }
            }
        }
    }
}