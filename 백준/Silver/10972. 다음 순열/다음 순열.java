
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int pivot = n-1;
//        뒤에서부터 탐색
        while(pivot > 0 && arr[pivot-1] >= arr[pivot]){
            pivot--;
        }
//        pivot이 0이면 내림차순 수열이라서 -1 출력
        if (pivot == 0) {
            System.out.println("-1");
            return;
        }
        int changeIdx = n-1;
        while(arr[pivot-1] >= arr[changeIdx]){
            changeIdx--;
        }
        int temp = arr[pivot-1];
        arr[pivot-1] = arr[changeIdx];
        arr[changeIdx] = temp;
        int k = n - 1;
        while (pivot < k) {
            temp = arr[pivot];
            arr[pivot] = arr[k];
            arr[k] = temp;
            pivot++;
            k--;
        }
        StringBuilder sb = new StringBuilder();
        for (int num : arr) {
            sb.append(num).append(" ");
        }
        System.out.println(sb.toString());
    }
}