import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static int n,b;
    static int count;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int tc= 1; tc<=T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
             n = Integer.parseInt(st.nextToken());
             b = Integer.parseInt(st.nextToken());
             count = Integer.MAX_VALUE;
             arr= new int[n];
             st = new StringTokenizer(br.readLine());
             for(int i = 0; i< n; i++){
                 arr[i] = Integer.parseInt(st.nextToken());
             }
             combinations(0,0);
            System.out.println("#" + tc + " " + (count - b));
        }
    }
    static void combinations(int depth, int val){
//        뽑았으면
        if(depth == n){
//            b보다 크거나 같고 val이 count보다 작으면
            if(val >= b && val < count) {
                count = val;
            }
            return;
        }

        combinations(depth+1, val+ arr[depth]);
        combinations(depth+1, val);
    }
}
