'''
Question(27): Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''


# Approach:
# have pointer starts with 0 & can use to update the nums's index item
# loop through the items
# if item is not value then
# upate the nums's index with the item
# increase the pointer
# return the pointer value

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pointer = 0
        for i, item in enumerate(nums):
            if item != val:
                nums[pointer] = item
                pointer += 1
        return pointer

solution = Solution()
result = solution.removeElement([3, 2, 2, 3], 3)
print(result) 

# Output: 2

# Time O(n) : at worst case we have to loop through every element of the array
# Space O(1): didn't use any extra space
