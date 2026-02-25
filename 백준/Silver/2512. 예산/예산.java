
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;

public class Main {
    static int[] budget;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        budget = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int start = 0;
        int end = 0;
        for(int i = 0; i< n; i++){
            int num = Integer.parseInt(st.nextToken());
            budget[i] = num;
            if(num > end) end = num;
        }
        int limit = Integer.parseInt(br.readLine());
        int mid = 0;
        int res = 0;
//        이분탐색 실행
        while(start <= end){
            int total = 0;
            mid = (start + end) / 2;
            for(int i = 0; i<n; i++){
//                상한액이 예산보다 크면 i지방 예산 그냥 씀
                if(mid > budget[i]) total += budget[i];
                else total += mid;
                }
//            상한액 합이 예산보다 클 때 -> 상한액을 1 줄임
            if(total > limit){
                end = mid -1;
            }
//            합이 예상 상한액보다 작거나 같을 때
            else{
                res = mid;
                start = mid +1;
            }
        }
        System.out.println(res);
    }
}