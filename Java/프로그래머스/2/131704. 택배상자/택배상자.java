import java.util.*;
class Solution {
    public int solution(int[] order) {
        int answer = 0;
        int idx = 0;
        Stack<Integer> stack = new Stack<>();
        for(int i = 1; i<= order.length; i++){
            stack.push(i);
//             스택이 비어있지 않고 스택의 top이 order랑 같으면 즉 보조 벨트 맨 위가 지금 실어야 된다믄
            while(!stack.isEmpty() && stack.peek() == order[idx]){
                stack.pop();
                idx++;
            }
        }
        return idx;
    }
}