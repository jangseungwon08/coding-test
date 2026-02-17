
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int[][] arr = new int[100][100];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 0;
        for(int i = 0; i< n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            for(int j = r; j < r+ 10; j++){
                for(int k = c; k < c + 10; k++){
                    arr[j][k] = 1;
                }
            }
        }
        for(int i = 0; i< 100; i++){
            for(int j = 0; j< 100; j++){
                count += arr[i][j];
            }
        }
        System.out.println(count);
    }
}