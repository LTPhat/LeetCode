# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

# Wrong answer
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust: 
            return 1
        if n == 2:
            return trust[0][1]
        count = {}
        for i, j in trust:
            count[j] = count.get(j, 0) + 1
        if list(count.items())[0][1] == n-1:
            return list(count.items())[0][0]
        else:
            return -1


# Accept
from collections import defaultdict
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # being_trusted[a] = b means person a is being trusted by b people
        being_trusted = defaultdict(int)
        # to_trust[c] = d means person c trusts d people
        to_trust = defaultdict(int)
        for i, j in trust:
            to_trust[i] += 1
            being_trusted[j] += 1
        for i in range(1, n+1):
            if being_trusted[i] == n-1 and to_trust[i] == 0:
                return i
        return -1