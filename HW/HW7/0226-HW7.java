package HW.HW7;
import java.util.Arrays;
import java.util.PriorityQueue;

public class MeetingRooms {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<Integer> ends = new PriorityQueue<>();
        int roomsNeeded = 0;
        for (int[] interval : intervals) {
            int start = interval[0];
            int end = interval[1];
            while (!ends.isEmpty() && ends.peek() <= start) {
                ends.poll();
            }
            ends.offer(end);
            roomsNeeded = Math.max(roomsNeeded, ends.size());
        }
        return roomsNeeded;
    }//minmeetingrooms
    public static void main(String[] args) {
        MeetingRooms meetingRooms = new MeetingRooms();
        
        int[][] testcase1 = {{0, 30}, {5, 10}, {15, 20}};
        System.out.println(meetingRooms.minMeetingRooms(testcase1));

        int[][] testcase2 = {{0, 1}, {1, 2}, {2, 3}};
        System.out.println(meetingRooms.minMeetingRooms(testcase2));
    }//main
}
