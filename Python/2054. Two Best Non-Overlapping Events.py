# You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

# Return this maximum sum.

# Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

 

# Example 1:


# Input: events = [[1,3,2],[4,5,2],[2,4,3]]
# Output: 4
# Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
# Example 2:

# Example 1 Diagram
# Input: events = [[1,3,2],[4,5,2],[1,5,5]]
# Output: 5
# Explanation: Choose event 2 for a sum of 5.
# Example 3:


# Input: events = [[1,5,3],[1,5,1],[6,6,5]]
# Output: 8
# Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.

# LINE_SWEEP ALGO FOR INTERVAL OVERLAP PROCESSING

class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        
        # Create a time_sweep without overlaping
        line_sweep = []
        for start, end, val in events:
            line_sweep.append([start, 1, val])
            line_sweep.append([end + 1, -1, val])

        line_sweep.sort(reverse = False)
        max_val = 0     # Maximum value obtained
        max_seen = 0    # Maximum value of the seen events

        for start, status, value in line_sweep:
            if status == 1:
                max_val = max(max_val, value + max_seen)
            elif status == -1:
                max_seen = max(max_seen, value)

        return max_val

# Test case
# events = [[1,5,3],[1,5,1],[6,6,5]]
# sweep_line = [[1, 1, 1], [1, 1, 3], [6, -1, 1], [6, -1, 3], [6, 1, 5], [7, -1, 5]]