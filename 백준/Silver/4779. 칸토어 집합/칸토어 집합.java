import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static String cantoir(int depth){
        String s;
        if (depth == 1){
            s = "-";
            return s;
        }
        String stack = cantoir(depth / 3);
        return stack + " ".repeat(depth/3) + stack;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;
        while ((input = br.readLine()) !=null) {
            if (input.isEmpty()) {
                break;
            }
            try {
                int num = Integer.parseInt(input);
                int depth = (int) Math.pow(3, num);
                String res = cantoir(depth);
                System.out.println(res);
            }
        catch (NumberFormatException e) {
                // 숫자가 아닌 입력이 들어왔을 때 종료하거나 무시
                break;
            }
        }
    }
    }
