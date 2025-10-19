# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        revertedNumber = 0
        input = x
        lengthX = len(str(x))
        if x > 0:
            while lengthX > 0:
                # This is going to retrieve the last digit from X and put it at the beggining of the variable
                revertedNumber = revertedNumber * 10 + x % 10

                # Delete the last digit of X
                x //= 10
                lengthX -= 1
            print(revertedNumber)
        return revertedNumber == input

s = Solution()
print(s.isPalindrome(121))