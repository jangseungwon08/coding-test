import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] str = br.readLine().split(" ");
        int V = Integer.parseInt(br.readLine());
        int[] arr = new int[str.length];
        int count = 0;
        for (int i = 0; i< arr.length; i++){
            arr[i] = Integer.parseInt(str[i]);
        }
        for(int i =0; i < arr.length; i++){
            if(arr[i] == V){
                count ++;
            }
        }
        System.out.println(count);
    }
}