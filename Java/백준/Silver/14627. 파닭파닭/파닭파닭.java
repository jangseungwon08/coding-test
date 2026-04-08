import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static long[] pa;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        pa = new long[n];
        long start = 1;
        long end = Integer.MIN_VALUE;
        for(int i = 0 ; i < n ; i++){
            pa[i] = Long.parseLong(br.readLine());
            if(pa[i] > end) end = pa[i];
        }
        long ans = 0;
//        이분탐색이나 파라메트릭 서치는 왜 start <= end?
//        투포인터같은것들은 start < end이던데
        while(start <= end){
            long mid = (start + end) / 2;
            long count = 0;
            for(int i = 0; i< n; i++){
                count += pa[i] / mid;
            }
//            만들 수 있는 개수보다 작으면
            if(c > count){
                end = mid-1;
            }
//            만들 수 있는 개수보다 크면
            else{
                ans = mid;
                start = mid + 1;
            }
        }
        long res = 0;
        for(int i = 0; i< n; i++){
            res += pa[i];
        }
        res = res - (ans *(long)c);
        System.out.println(res);
    }
}