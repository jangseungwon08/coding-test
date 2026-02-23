
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] threeWay = new int[3];
        Queue<Integer> q = new ArrayDeque<>();
        int[] dayList = new int[100_001];
        q.offer(n);
        while(!q.isEmpty()){
            int now = q.poll();
            if(now == k) break;
            threeWay[0] = now - 1;
            threeWay[1] = now + 1;
            threeWay[2] = now * 2;
            for(int i = 0; i< 3; i++){
//                뽑은 값이 0이상 10만 이하 그리고 탐색하지 않은 day일 때
                if(threeWay[i] >= 0 && threeWay[i] <= 100_000 && dayList[threeWay[i]] == 0){
//                    dayList현재 날짜에서 1 더함
                    dayList[threeWay[i]] = dayList[now] + 1;
                    q.offer(threeWay[i]);
                }
            }
        }
        System.out.println(dayList[k]);
    }
}