import java.io.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        String[] str = br.readLine().split(" ");
        Integer[] arr = new Integer[N];
        for(int i = 0; i< str.length; i++){
            arr[i] = Integer.parseInt(str[i]);
        }
        Arrays.sort(arr);
        System.out.print(arr[N-k]);
    }
}
