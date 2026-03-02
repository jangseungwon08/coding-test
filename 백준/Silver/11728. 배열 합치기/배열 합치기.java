import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int aN = Integer.parseInt(st.nextToken());
        int bN = Integer.parseInt(st.nextToken());
        int[] arr = new int[aN + bN];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i< aN; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for(int i = aN; i< bN+aN; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i< arr.length; i++){
            sb.append(arr[i]).append(" ");
        }
        System.out.println(sb.toString());
    }
}
