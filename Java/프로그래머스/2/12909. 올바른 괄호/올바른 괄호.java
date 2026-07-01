import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int count = 0;
        
        for(char word: s.toCharArray()){
            if(word == '(') count++;
            else{
                count --;
                if(count < 0 ){
                    return false;
                }
            }
        }
        if(count == 0) return true;
        else return false;
    }
}