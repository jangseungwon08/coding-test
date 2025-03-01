import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] chess = {1, 1, 2, 2, 2, 8};
        int[] ans = new int[6];
        String[] str = br.readLine().split(" ");
        for(int i = 0; i< str.length;i++){
            int n = Integer.parseInt(str[i]);
            ans[i] = chess[i] - n;
        }
        for(int i = 0; i< ans.length;i++){
            System.out.print(ans[i] + " ");
        }
    }
    }