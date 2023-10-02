'''
Question: Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

Input: arr = [3, 5, 4, 1, 9]
Output: Minimum element is: 1
        Maximum element is: 9

Input: arr1 = [22, 14, 8, 17, 35, 3]
Output:  Minimum element is: 3
         Maximum element is: 35
'''

# Approach: 

# 1. linear method using single pointer to compare

class Solution:
    def find_min_max(self, nums: list[int]) -> list:
        min_val = nums[0]
        max_val = nums[0]
        
        # assuming the first item is the min and max value, we start comparing from the second element so the loop will start from second elemen
        for item in nums[1:]:
            if item < min_val:
                min_val = item
            elif item > max_val:
                max_val = item

        return [min_val, max_val]

solution = Solution()
result = solution.find_min_max([3, 2, 8, 1])
print(result)
# Output: [1, 8]

# Time O(n - 1): 
# Space O(1): didn't use any extra space (in-place)



# 2. divide and conquer (optimize solution)