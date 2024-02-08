public class Main {
    public static void main(String[] args) {
        int[] inputArray = {1, 2, 2, 0, 4, 5, 0, 6, 7, 8, 9};
        System.out.println("This is the first bad index: " + firstBad(inputArray));
    }

    public static boolean isBadVersion(int i) {
        return i == 0;
    } //isbadversion

    public static int firstBad(int[] inputArray) {
        for (int i = 0; i < inputArray.length; i++) {
            if (isBadVersion(inputArray[i])) {
                return i;
            }//if
        }//for
    }//firstbad
}//main
