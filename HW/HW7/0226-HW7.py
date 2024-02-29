# youre a sysadmin for a big tech company, and you have to estimate the amount of servers you need to handle some long running jobs
# one server can handle only one job at once, one job can only be executed by one server at once. once a server has finished executing its current job, it can be reassigned to a new job.

# given an array of time intervals:
# intervals where intervals[i] = [starti, endi]
# representing the start and end time for a particular job that needs to be executed return the minimum number OverflowErrorservers required to run all

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    # one server can handle only one job at once
    # one job can only be executed by one server at once
    # once a server has finished executing its current job, it can be reassigned



testcase1 = [[0,30], [5,10], [15.20]]