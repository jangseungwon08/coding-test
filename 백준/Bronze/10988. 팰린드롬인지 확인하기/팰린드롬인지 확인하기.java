import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringBuffer sb = new StringBuffer(str);
        String reverse = sb.reverse().toString();
        if(str.equals(reverse)){
            System.out.println(1);
        }
        else{
            System.out.println(0);
        }
    }
    }