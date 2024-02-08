public class Main {
    public static void main(String[] args) {
        String userInput = "do GEEse See goD";
        palindrome(userInput);
    }//main
}//main

public static void palindrome(String s) {
    String userString = s.toLowerCase().replaceAll(" ", "");
    String reverseString = new StringBuilder(userString).reverse().toString();
    
    if (reverseString.equals(userString)) {
        System.out.println("This is a palindrome :)");
    } else {
        System.out.println("This is not a palindrome :(");
    }//if
}//palindrome
