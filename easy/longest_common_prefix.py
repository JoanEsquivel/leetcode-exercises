"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.


"""

# Horizontal scanning approach. We can also solve it using Binary Search, but it will be more expensive.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for word in strs:
            while(word.find(prefix) != 0):
                prefix = prefix[0: len(prefix) -1]
                if(prefix==""):
                    return ""
        return prefix


s = Solution()
s.longestCommonPrefix(['flower', 'flow', 'flight'])


"""
# Complexity
# Time:  O(S), where S is the total number of characters across all strings.
#        Worst case: all n strings are identical; we compare S1 to S2..Sn,
#        doing a total of S character comparisons.
# Space: O(1) extra space (uses only constant additional memory).

"""

# Vertical scanning approach. (the best one)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == None or len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for j in range(1, len(strs)):
                print(strs[j])
                print(len(strs[j]))
                print(strs[j][i])
                if i == len(strs[j]) or strs[j][i] != letter:
                    return strs[0][0:i]
        return strs[0]


s = Solution()
s.longestCommonPrefix(['flower', 'flow', 'flight'])


"""
# Complexity
# Time:  O(S), where S = total number of characters across all strings.
#        Worst case: n strings of equal length m → S = m * n comparisons.
#        Best case: at most n * minLen comparisons,
#                   where minLen = length of the shortest string.
# Space: O(1) extra space (constant additional memory).

"""