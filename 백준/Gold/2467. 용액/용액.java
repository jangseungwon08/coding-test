import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr= new int[n];
        for(int i = 0; i< n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
//      count하나 잡고 arr[start] + arr[end] 가 count보다 크면
        int start = 0;
        int end = n-1;
        int count = Integer.MAX_VALUE;
        int startIdx = 0;
        int endIdx = 0;
        while(start < end){
            int num1 = arr[start];
            int num2 = arr[end];
//            음수 일때 처리 로직이랑 양수일 때 처리 로직
            if(num1 + num2 == 0) {
                startIdx = start;
                endIdx = end;
                break;
            }
//            갱신
            if( Math.abs((num1+num2)) < count){
                count = Math.abs((num1+num2));
                startIdx = start;
                endIdx = end;
            }
//            포인터 옮기기
            if(num1+num2 < 0){
                start++;
            }
            if(num1 + num2 > 0){
                end--;
            }
        }
        System.out.println(arr[startIdx] + " " + arr[endIdx]);
    }
}
