# youre a sysadmin for a big tech company, and you have to estimate the amount of servers you need to handle some long running jobs
# one server can handle only one job at once, one job can only be executed by one server at once. once a server has finished executing its current job, it can be reassigned to a new job.

# given an array of time intervals:
# intervals where intervals[i] = [starti, endi]
# representing the start and end time for a particular job that needs to be executed return the minimum number OverflowErrorservers required to run all
from typing import List
import heapq


def minMeetingRooms(intervals: List[List[int]]) -> int:
    # one server can handle only one job at once
    # one job can only be executed by one server at once
    # once a server has finished executing its current job, it can be reassigned

    intervals.sort()
    servers = 0 # number of servers initialized
    ends = [] # empty list to keep track of end times

    for start, end in intervals:
            # Check if any server is freed up (end time <= current start time)
            while ends and ends[0] <= start:
                heapq.heappop(ends) # popping the earliest end time
            heapq.heappush(ends, end) # push the end time of current job
            servers = max(servers, len(ends))   # update the number of servers
    return servers

testcase1 = [[0,30], [5,10], [15,20]]
print(minMeetingRooms(testcase1))
testcase2 = [[0,1],[1,2],[2,3]]
print(minMeetingRooms(testcase2))