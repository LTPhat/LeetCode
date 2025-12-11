# You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

# A building is covered if there is at least one building in all four directions: left, right, above, and below.

# Return the number of covered buildings.

 

# Example 1:



# Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]

# Output: 1

# Explanation:

# Only building [2,2] is covered as it has at least one building:
# above ([1,2])
# below ([3,2])
# left ([2,1])
# right ([2,3])
# Thus, the count of covered buildings is 1.

from collections import defaultdict

class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        covered_count = 0
        group_by_x = defaultdict(list)
        group_by_y = defaultdict(list)

        # Group
        for x, y in buildings:
            group_by_x[x].append([x, y])
            group_by_y[y].append([x, y])

        # Filter & sort correctly
        for k in group_by_x:
            group_by_x[k].sort(key=lambda p: p[1])   # sort by y
        for k in group_by_y:
            group_by_y[k].sort(key=lambda p: p[0])   # sort by x

        for x, lst in group_by_x.items():
            if len(lst) <= 2:
                continue
            for i, (xx, yy) in enumerate(lst):
                if i == 0 or i == len(lst)-1:
                    continue  

                vert = group_by_y[yy]
                pos = vert.index([xx, yy])

                if pos != 0 and pos != len(vert)-1:
                    covered_count += 1

        return covered_count
    

    from collections import defaultdict

# class Solution(object):
    # def countCoveredBuildings(self, n, buildings):
    #     covered_count = 0
    #     group_by_x = defaultdict(list)
    #     group_by_y = defaultdict(list)

    #     # Group
    #     for x, y in buildings:
    #         group_by_x[x].append([x, y])
    #         group_by_y[y].append([x, y])

    #     # Filter & sort correctly
    #     for k in group_by_x:
    #         group_by_x[k].sort(key=lambda p: p[1])   # sort by y
    #     for k in group_by_y:
    #         group_by_y[k].sort(key=lambda p: p[0])   # sort by x

    #     for x, lst in group_by_x.items():
    #         if len(lst) <= 2:
    #             continue
    #         for i, (xx, yy) in enumerate(lst):
    #             if i == 0 or i == len(lst)-1:
    #                 continue  

    #             vert = group_by_y[yy]
    #             pos = vert.index([xx, yy])

    #             if pos != 0 and pos != len(vert)-1:
    #                 covered_count += 1

    #     return covered_count
class Solution(object):
        def countCoveredBuildings(self, n, buildings):
            rows_min = defaultdict(lambda: float('inf'))
            rows_max = defaultdict(lambda: -float('inf'))
            cols_min = defaultdict(lambda: float('inf'))
            cols_max = defaultdict(lambda: -float('inf'))

            # Compute min/max for each row and column
            for x, y in buildings:
                rows_min[y] = min(rows_min[y], x)
                rows_max[y] = max(rows_max[y], x)
                cols_min[x] = min(cols_min[x], y)
                cols_max[x] = max(cols_max[x], y)

            covered = 0

            # Check each building
            for x, y in buildings:
                if rows_min[y] < x < rows_max[y] and cols_min[x] < y < cols_max[x]:
                    covered += 1

            return covered
