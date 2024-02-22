import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> triplet(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) { continue ;}
            int left = i + 1;
            int right = nums.length - 1;
            while (i + 1 < nums.length - 1) {
                if ((nums[i] + nums[left] + nums[right]) == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left+1]) left++;
                    while (left < right && nums[right] == nums[right-1]) right++;
                    left++;
                    right--;
                } else if ((nums[i] + nums[left] + nums[right]) < 0) {
                    left++;
                } else right --;

            } //while
        } //for
    } //triplet

    public static void main(String[] args) {
        ThreeSum threesum = new ThreeSum();

        int[] testcase1 = {0, 1, 1};
        System.out.println(threesum.triplet(testcase1));

        int[] testcase2 = {-5, 0, 5, 10, -10, 0};
        System.out.println(threesum.triplet(testcase2));

    } //main
} //threesum