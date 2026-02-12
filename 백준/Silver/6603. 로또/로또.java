
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static List<Integer> arr;
    static int k ;
    static List<Integer> res;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true){
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr = new ArrayList<>();
            res = new ArrayList<>();
            k  = Integer.parseInt(st.nextToken());
            if(k == 0) return;
            while(st.hasMoreTokens()){
                arr.add(Integer.parseInt(st.nextToken()));
            }
            backTrack(0, 0);
            System.out.println();
        }
    }

    static void backTrack(int depth, int start){
        if(depth == 6){
            res.stream().forEach(e -> System.out.print(e + " "));
            System.out.println();
            return;
        }

        for(int i = start; i< k; i++){
            res.add(arr.get(i));
            backTrack(depth+1, i+1);
            res.remove(res.size()-1);
        }
    }
}
