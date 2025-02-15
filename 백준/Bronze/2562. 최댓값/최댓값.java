import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i = 0 ; i < 9; i++){
            arr.add(Integer.parseInt(br.readLine()));
        }
        int max = Collections.max(arr);
        int max_idx = arr.indexOf(max);
        System.out.println(max);
        System.out.println(max_idx+1);
    }
}