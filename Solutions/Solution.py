# Goal is to check if the input numbers are a palindrome

#Example 1:
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse = 0
        xCopy = x

        while x > 0:
             reverse = (reverse * 10) + (x % 10)
             x //= 10
            
        return reverse == xCopy
