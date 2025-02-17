import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] str = br.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);
        int[] arr = new int[n];
        for(int y = 0; y < n; y++){
            arr[y] = y+1;
        }
        for(int x = 0; x< m; x++) {
            String[] str2 = br.readLine().split(" ");
            int i = Integer.parseInt(str2[0])-1;
            int j = Integer.parseInt(str2[1])-1;
            int i1 = arr[i];
            int j1 = arr[j];
            arr[i] = j1;
            arr[j] = i1;
        }
        for(int a=0; a < arr.length; a++){
            bw.write(arr[a] + " ");
        }
        br.close();
        bw.flush();
        bw.close();
    }
}