'''
Question(37): Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

'''

# Approach: binary search by dividing to find the middle index
# define two pointer for start and end indexes
# loop while the left is smaller and equal to right pointer
# if target is smaller then the midder then go towards right from the mid
# else if target is higher than the middle then come towards left from the mid
# else we retur found the target index, so return the mid


class Solution:
    def find_index(self, nums, target):
        left = 0
        right = len(nums) - 1
        # loop while left is smaller or equal to right
        while left <= right:
            # find the middle index
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return left


solution = Solution()
result = solution.find_index([1, 3,  7], 5)
print(result)
