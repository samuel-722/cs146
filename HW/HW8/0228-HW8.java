import java.util.HashMap;

public class Main {
    public static int longestPalindrome(String s) {
        HashMap<Character, Integer> hm = new HashMap<>();
        int length = 0;
        boolean isOdd = false;

        // Initialize hashmap
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            hm.put(currentChar, hm.getOrDefault(currentChar, 0) + 1);
        } //for

        // Count pairs and handle odd counts
        for (int count : hm.values()) {
            length += count / 2 * 2;
            if (count % 2 != 0) {
                isOdd = true;
            } //if
        } //for
        if (isOdd) length++;

        return length;
    } //longest palindrome

    public static void main(String[] args) {
        String testcase1 = "abcccdd";
        System.out.println(longestPalindrome(testcase1));

        String testcase2 = "speediskey";
        System.out.println(longestPalindrome(testcase2));
    } //main
} //main
