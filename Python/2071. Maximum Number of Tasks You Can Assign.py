# You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

# Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

# Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.

 

# Example 1:

# Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
# Output: 3
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 2 (0 + 1 >= 1)
# - Assign worker 1 to task 1 (3 >= 2)
# - Assign worker 2 to task 0 (3 >= 3)
# Example 2:

# Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
# Output: 1
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 0 (0 + 5 >= 5)
# Example 3:

# Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
# Output: 2
# Explanation:
# We can assign the magical pills and tasks as follows:
# - Give the magical pill to worker 0 and worker 1.
# - Assign worker 0 to task 0 (0 + 10 >= 10)
# - Assign worker 1 to task 1 (10 + 10 >= 15)
# The last pill is not given because it will not make any worker strong enough for the last task.


class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        tasks.sort()  # sort tasks by difficulty (ascending)
        workers.sort()  # sort workers by strength (ascending)
        def canAssign(k):
            """
            Check if we can complete k tasks
            """
            selected_tasks = tasks[:k]  # Take k easiest tasks
            available_workers = workers[-k:]  # Take k strongest workers
            remaining_pills = pills
            
            # Process from hardest to easiest in the k tasks
            for task in reversed(selected_tasks):
                # If strongest worker can't do task even with pill, return False
                if available_workers[-1] < task and \
                (available_workers[-1] + strength < task or remaining_pills == 0):
                    return False
                
                # If strongest worker can do it without pill, assign them
                if available_workers[-1] >= task:
                    available_workers.pop()  # Use strongest worker
                else:
                    # Find the weakest worker who can do this task with a pill
                    # Binary search to find the right worker
                    left, right = 0, len(available_workers) - 1
                    while left < right:
                        mid = (left + right) // 2
                        if available_workers[mid] + strength >= task:
                            right = mid
                        else:
                            left = mid + 1
                    
                    # Remove this worker and use a pill
                    available_workers.pop(left)
                    remaining_pills -= 1
            
            return True
        
        # Binary search to find maximum k
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (left + right + 1) // 2
            if canAssign(mid):
                left = mid
            else:
                right = mid - 1
                
        return left