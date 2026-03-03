import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static int[] arr;
    static int n, b;
    static boolean[] isVisited;
    static int maxSum;
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int tc = 1; tc <= t; tc++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            arr = new int[n];
            isVisited = new boolean[n];
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i< n; i++){
                arr[i] = Integer.parseInt(st.nextToken());
            }
            maxSum = Integer.MAX_VALUE;
            powerSet(0,0);
            System.out.println("#" + tc + " " + (maxSum - b));
        }
    }
    static void powerSet(int depth, int sum){
        if(depth == n) {
//            b보다 크고 maxSum보다 작으면
            if (sum >= b && maxSum > sum) {
                maxSum = sum;
            }
            return;
        }
//        뽑는 경우
        isVisited[depth] = true;
        powerSet(depth+1, sum + arr[depth]);
//        안뽑는 경우
        isVisited[depth] = false;
        powerSet(depth+1, sum);
        }
}
