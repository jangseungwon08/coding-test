import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);
        int[] arr = new int[n];
        for(int a = 0; a < m; a++){
            String[] str2 = br.readLine().split(" ");
            int i = Integer.parseInt(str2[0]);
            int j = Integer.parseInt(str2[1]);
            int k = Integer.parseInt(str2[2]);
            for(int x = i-1; x < j; x++){
                arr[x] = k;
            }
        }
        for(int x = 0; x < arr.length; x++){
            System.out.print(arr[x] + " ");
        }
    }
}