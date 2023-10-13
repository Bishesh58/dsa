''''
Question:Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
'''

# Brute Force: Time => O(n), Space => O(n)
def find_pivot(nums):

    for i in range(len(nums)):
        left_sum = sum(nums[: i])
        right_sum = sum(nums[i + 1:])
        if left_sum == right_sum:
            return i
    return -1


result = find_pivot([1, 7, 3, 6, 5, 6])
print(result)


# Optimize: Time => O(n), Space => O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)

        for i, item in enumerate(nums):
            if left_sum == total_sum - nums[i] - left_sum:
                return i
            left_sum += nums[i]
            
        return -1