import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        int sum = 0;
        int temp = 0;
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i< N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        for(int i = 0; i< N-2;i++){
            for(int j = i+1; j < N-1; j++){
                for(int k = j+1; k < N; k++){
                    //temp에 3개 카드 값 저장
                    temp = arr[i] + arr[j] + arr[k];
                    //temp값이 M보다 작거나  같고 sum보다 크면
                    if(temp <= M && temp > sum){
                        //sum에 temp를 저장한다.
                        sum = temp;
                    }
                }
            }
        }
        System.out.print(sum);
    }
}
