import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i< n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int m = Integer.parseInt(br.readLine());
        int[] target = new int[m];
        st= new StringTokenizer(br.readLine());
        for(int i = 0; i< m; i++){
            target[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i< m; i++){
            int num = target[i];
//            시작점을 0으로 끝 점을 배열 마지막 n-1로
            int start = 0;
            int end = n-1;
            boolean flag = false;
            while(start <= end){
//                mid값 업데이트 
                int mid = (start + end) / 2;
                if(arr[mid] == num){
//                    찾았으면 break
                    sb.append("1").append("\n");
                    flag = true;
                    break;
                }
//                mid값이 num보다 크면 왼쪽으로 이동
                else if(arr[mid] > num){
                    end = mid-1;
                }
                else{
                    start = mid+1;
                }
            }
            if(!flag){
                sb.append("0").append("\n");
            }
        }
        System.out.println(sb);
    }
}
