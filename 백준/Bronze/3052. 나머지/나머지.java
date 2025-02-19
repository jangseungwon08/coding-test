import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Integer> set = new HashSet<Integer>();
        for(int i = 0; i<10; i++){
            int x = Integer.parseInt(br.readLine()) % 42;
            set.add(x);
        }
        System.out.println(set.size());
    }
    }