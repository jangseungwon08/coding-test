import java.util.*;
public class Main {
    public static void main(String[] args) {
     Scanner in = new Scanner(System.in);
     int A = in.nextInt();
     int B = in.nextInt();

     System.out.println(A+B);

     //최적화 관점에서 new로 동적으로 할당받았기 때문에 명시적으로 close해주는 것이 좋다.
        in.close();
      }
    }