import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static int[] arr;
    static int[] calculator;
    static int n;
    static int maxVal, minVal;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int tc = 1; tc <= t; tc++){
            n = Integer.parseInt(br.readLine());
            arr = new int[n];
            calculator = new int[4];
            maxVal = Integer.MIN_VALUE;
            minVal = Integer.MAX_VALUE;
            StringTokenizer st= new StringTokenizer(br.readLine());
            for(int i = 0; i< 4; i++){
                calculator[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i< n; i++){
                arr[i] = Integer.parseInt(st.nextToken());
            }
            backTrack(0, arr[0]);
            System.out.println("#" + tc + " " + (maxVal - minVal));
        }
    }
//    순열 백트래킹
//    4개중에 순서가 중요 -> for문 돌리면서
    static void backTrack(int depth, int val){
//        max,min업데이트 조건
        if(depth == n-1){
            if(val > maxVal) maxVal = val;
            if (val < minVal) minVal = val;
            return;
        }

        for(int i = 0; i< 4; i++){
//            0번 이상인 calculator를 뽑는 경우
            if(calculator[i] > 0){
                calculator[i] -= 1;
                if(i == 0 ) backTrack(depth+1, val + arr[depth+1]);
                else if(i==1) backTrack(depth+1, val - arr[depth+1]);
                else if(i==2) backTrack(depth+1, val * arr[depth+1]);
                else if(i==3) backTrack(depth+1, val / arr[depth+1]);
                calculator[i] += 1;
            }
        }
    }
}
