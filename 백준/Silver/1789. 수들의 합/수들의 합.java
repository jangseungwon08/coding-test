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
        int idx = 0;
        memo.add(1);
        int num = 1;
        s -= num;
        while(s >= 0){
//            memo.get(idx)에서 num을 더한 값에 s를 뺌
            int temp = num + memo.get(idx);
            s -= temp;
            if(s < 0 ) break;
            memo.add(memo.get(idx++) + num);
        }
        System.out.println(memo.get(memo.size()-1));
    }
}