
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
//    상하좌우
    static int[] dr  = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int[][] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new int[n][n];
        for(int i = 0; i< n; i++){
            String s = br.readLine();
            for(int j = 0; j< s.length(); j++){
                arr[i][j] = s.charAt(j) - '0';
            }
        }
        Queue<int[]> q = new ArrayDeque<>();
        int buildingCount = 0;
        int buildingNum = 1;
        List<Integer> buildings = new ArrayList<>();
        for(int i = 0; i< n; i++){
            for(int j = 0; j< n; j++){
                int count = 0;
                if(arr[i][j] == 1){
                    q.offer(new int [] {i, j});
                    buildingNum++;
                    buildingCount++;
                    arr[i][j] = buildingNum;
                }
                while(!q.isEmpty()){
                    int[] current = q.poll();
                    int r = current[0];
                    int c = current[1];
                    count++;
                    for(int k = 0; k< 4; k++){
                        int nr = r + dr[k];
                        int nc = c + dc[k];
                        if(nr >= 0 && nr < n && nc >=0 && nc < n) {
                            if (arr[nr][nc] == 1) {
                                q.offer(new int[] {nr, nc});
                                arr[nr][nc] = buildingNum;
                            }
                        }
                    }
                }
                if(count > 0) buildings.add(count);
            }
        }
        System.out.println(buildingCount);
        Collections.sort(buildings);
        for(int i = 0; i< buildings.size(); i++){
            System.out.println(buildings.get(i));
        }
    }
}