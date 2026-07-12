import java.util.*;

class Solution {
    static Map<String, Integer> index = new HashMap<>();
    public List<Integer> solution(String msg) {
     List<Integer> answer = new ArrayList<>();
        int answerSize = 0;
        for(int i = 1; i<= 26; i++){
            index.put(String.valueOf((char) (i + 64)), i);
        }
        int lastIndex = 26;
        int i = 0;
        // while문을 사용해 탐색 시작 위치(i)를 자유롭게 제어합니다.
        while (i < msg.length()) {
            String w = "";
            int nextI = i;
            while(nextI < msg.length() && index.containsKey(w + msg.charAt(nextI))){
                w += msg.charAt(nextI++);
            }
            answer.add(index.get(w));
            // 입력에서 처리되지 않은 글자가 남아있다면 (w + 다음글자)를 사전에 등록
            if (nextI < msg.length()) {
                String c = String.valueOf(msg.charAt(nextI));
                index.put(w + c, ++lastIndex);
            }
            i = nextI;
        }
        return answer;
    }
}