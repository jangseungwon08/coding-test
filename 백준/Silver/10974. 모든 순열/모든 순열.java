
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static boolean[] isVisited;
    static List<Integer> arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        isVisited = new boolean[n+1];
        arr = new ArrayList<>();
        backTrack(0);
    }
    static void backTrack(int depth){
        if (depth == n) {
            for (int val : arr) {
                System.out.print(val + " ");
            }
            System.out.println();
            return; // 여기서는 arr 조작 없이 깔끔하게 return만!
        }
        for(int i = 1; i<= n; i++){
            if(!isVisited[i]){
                arr.add(i);
                isVisited[i] = true;
                backTrack(depth+1);

                arr.remove(arr.size()-1);
                isVisited[i] = false;
            }
        }
    }
}