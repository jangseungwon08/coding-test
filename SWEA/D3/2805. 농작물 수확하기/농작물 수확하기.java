import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int tc= 1; tc<=T; tc++){
            int n = Integer.parseInt(br.readLine());
            int[][] arr = new int[n][n];
            for(int i = 0; i< n; i++){
                String s = br.readLine();
                for(int j = 0; j< n; j++){
                    arr[i][j] = s.charAt(j) - '0';
                }
            }
            int count = 0;
//                    n/2 까지는 증가
//                    n/2 + 1부터는 감소
            int start = n/2;
            int end = n/2;
            for(int i = 0; i< n; i++){
                for(int j = start; j<= end; j++){
                    count += arr[i][j];

                }
                if(i < n/2){
                    start -=1;
                    end += 1;
                }
                if(i >= n/2){
                    start += 1;
                    end -= 1;
                }
            }
            System.out.println("#" + tc + " " + count);
        }
    }
}
