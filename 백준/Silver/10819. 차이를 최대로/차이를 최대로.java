
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;

public class Main {
    static boolean[] isVisited;
    static int n;
    static int maxSum;
    static int[] arr;
    static List<Integer> selected;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new int[n];
        isVisited = new boolean[n];
        selected  = new ArrayList<>();
        maxSum = 0;
        for(int i = 0; i< n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
//        모든 조합 8!
        backTrack(0, 0);
        System.out.println(maxSum);
    }
    static void backTrack(int depth, int sum){
        if(depth == n){
//            selected.forEach(e -> System.out.print(e + " "));
//            System.out.println();
            for(int i = 0; i< n-1; i++){
                sum += Math.abs(selected.get(i) - selected.get(i+1));
            }
            maxSum = Math.max(sum, maxSum);
            return;
        }
        for(int i = 0; i< n; i++){
            if(!isVisited[i]){
                isVisited[i] = true;
                selected.add(arr[i]);
                backTrack(depth + 1, sum);
                isVisited[i] = false;
                selected.remove(selected.size()-1);
            }
        }
    }

}