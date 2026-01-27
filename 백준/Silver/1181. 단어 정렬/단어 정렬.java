import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.function.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Set<String> hashSet = new HashSet<>();
        for(int i = 0; i< n; i++){
            hashSet.add(br.readLine());
        }
        List<String> arr = new ArrayList<>(hashSet);
        Collections.sort(arr,
                (w1,w2) -> {
            int lengthCompare = Integer.compare(w1.length(), w2.length());
        if(lengthCompare != 0){
            return lengthCompare;
        }
        return w1.compareTo(w2);
        });
        for (String s : arr) {
            System.out.println(s);
        }
    }
}
