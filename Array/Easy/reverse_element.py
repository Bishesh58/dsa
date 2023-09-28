'''
Question(344): Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''

# Approach:
# using two pointer methods to move left and right pointer to swap the indices of the array
# loop while left pointer is less than the right pointer so that they will meet the middle point in which case swap is completed
# another method can be slicing the string or array: for eg. string[start: end: step]


class Solution:
    def reverse_string(self, string):
        left = 0
        right = len(string) - 1
        # [ 1, 3, 5, 8, 9]
        #   l           r
        while left < right:
            # we need to get the left indices element before updating it's value so hold it on a variable
            temp = string[left]
            # swap the indices
            string[left] = string[right]
            string[right] = temp
            # this swap can be done using s[left], s[right] = s[right], s[left]
            # increase the left point and decrease the right pointer
            left += 1
            right -= 1
        return string


solution = Solution()
result = solution.reverse_string([1, 2, 3, 4, 5, 6])
# Output: [6, 5, 4, 3, 2, 1]


# Time O(n) : while loop runs for O(n/2) but ignoring the constant will give us O(n), each element is processed at least once
# Space O(1): didn't use any extra space (in-place)


# Another approach can be sliciing but the first one is better and more efficient as it doesn't need to copy each element
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

# Big O is same in both cases
