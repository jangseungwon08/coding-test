import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int target = Integer.parseInt(st.nextToken());
		int[] arr = new int[n];
		int s = 0, e = 0, res = 0, len = Integer.MAX_VALUE;
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i< n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		while(true) {
			if(res >= target) { // res가 target이상
				if(len > e - s) len = e - s;
				res -= arr[s++];
			} else if(e == n) {
				break;
			}else {
				res += arr[e++];
			}
		}
		if(len == Integer.MAX_VALUE) {
			System.out.println("0");
		}
		else {
			System.out.println(len);
		}
	}

}
