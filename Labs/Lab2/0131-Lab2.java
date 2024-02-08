import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        String sentence = "secure";
        String tsentence = "rescue";
        if (isAnagram(tsentence, sentence)) {
            System.out.println("The two strings are anagrams");
        } else {
            System.out.println("Not anagrams");
        }//else
    }//main

    public static boolean isAnagram(String t, String s) {
        char[] tArray = t.toCharArray();
        char[] sArray = s.toCharArray();
        Arrays.sort(tArray);
        Arrays.sort(sArray);
        return Arrays.equals(tArray, sArray);
    }//isanagram
}//main
