import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        int N = Integer.parseInt(str[0]);
        int M = Integer.parseInt(str[1]);
        int[] arr = new int[N];
        for(int y =1; y <= N; y++) {
            arr[y - 1] = y;
        }
        for(int x = 0; x< M; x++){
            String[] str2 = br.readLine().split(" ");
            int i = Integer.parseInt(str2[0])-1;
            int j = Integer.parseInt(str2[1])-1;
            while(i < j){
                /*temp에 arr[i]번째 12345에서 1 4이면
                0번째 원소값을 temp에 저장하고, 1증가된 1번째 인덱스값에 arr[j]값을 i에 저장
                1 4이면 -> 0 3
                1. temp = 1  -> 42345 -> 42315 i 1   j 2
                2. temp = 2  -> 43315 -> 43215 i 2   j 1
                * */
                int temp = arr[i];
                arr[i++] = arr[j];
                arr[j--] = temp;
            }
        }
        for(int i = 0; i< arr.length;i++){
            System.out.print(arr[i]+ " ");
        }
    }
    }