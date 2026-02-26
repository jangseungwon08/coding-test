
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        List<Integer> memo = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long s = Long.parseLong(br.readLine());
        long num = 1;
        long idx = 0;
        while(s >= 0){
            s -= num;
            if(s < 0){
                break;
            }
            num++;
            idx++;
        }
        System.out.println(idx);
    }
}