import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i = 1; i <= 30 ; i++){
            arr.add(i);
        }
        for(int i = 0; i< 28; i++){
            int x = Integer.parseInt(br.readLine());
            arr.remove(Integer.valueOf(x));
        }
        Collections.sort(arr);
        for(int i = 0; i < arr.size(); i++){
            System.out.println(arr.get(i));
        }
    }
    }