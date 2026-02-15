
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int maxPrice = 0;
    static int[][] arr;
    static int n;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int [n][2];
        for(int i = 0; i< n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int day = Integer.parseInt(st.nextToken());
            int price = Integer.parseInt(st.nextToken());
            arr[i] = new int[]{day, price};
        }
        backTrack(0,0);
        System.out.println(maxPrice);
    }
    static void backTrack(int start, int sum){
//        현재까지 번 돈이 최대값인지 확인(매 순간 최적해 가능) 아래 for문에서 가지치기를 수행
        maxPrice = Math.max(sum, maxPrice);
//        탈출조건 -> 현재 시점이 퇴사일 이후면 종료
        if(start >= n){
            return;
        }
        for(int i = start; i< n; i++) {
//           가지치기 
            if (i + arr[i][0] <= n) {
//                재귀호출
                backTrack(i + arr[i][0], sum + arr[i][1]);
            }
        }
    }
}