import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());
        int day_climb = A - B;
        int dest = V - B;
        //딱 나누어 떨어지면 남은 일 수가 없다는 뜻이다.
        if(dest % day_climb == 0){
            System.out.print((dest/day_climb));
        }
        //딱 나누어 떨어지지 않는다면 하루가 더 걸린다는 뜻
        else{
            System.out.print((dest/day_climb) +1);
        }
    }
}
