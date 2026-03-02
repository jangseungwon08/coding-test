import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n,s;
    static int[] arr;
    static boolean[] isVisited;
    static int count;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());
        count = 0;
        arr = new int[n];
        isVisited = new boolean[n];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i< n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        powerSet(0, 0);
//        공집합 제거
        if(s == 0) System.out.println(count-1);
        else System.out.println(count);
    }
    static void powerSet(int depth, int sum){
        if(depth == n){
            if(sum == s) count++;
            return;
        }
        isVisited[depth] = true;
        powerSet(depth+1, sum + arr[depth]);
        isVisited[depth] = false;
        powerSet(depth+1, sum);
        }
    }
