
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static int[][] arr;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr= new int[n][n];
        for(int i = 0; i< n; i++){
            String s = br.readLine();
            for(int j = 0; j< n; j++){
                arr[i][j] = s.charAt(j) - '0';
            }
        }
        divideAndConquer(n, 0, 0);
        System.out.println(sb);
    }
    static void divideAndConquer(int n, int r, int c){
        if(isPossible(n,r,c)) {
            sb.append(arr[r][c]);
            return;
        }
            int halfN = n / 2;
            sb.append("(");
            divideAndConquer(halfN, r, c);
            divideAndConquer(halfN, r, c + halfN);
            divideAndConquer(halfN, r + halfN, c);
            divideAndConquer(halfN, r + halfN, c + halfN);
            sb.append(")");
    }
    static boolean isPossible(int n, int r, int c){
        for(int i = r; i< r +n; i++){
            for(int j = c; j< c + n; j++){
                if(arr[r][c] != arr[i][j]) return false;
            }
        }
        return true;
    }
}