'''
Question: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # solution 1: brute force
        # looping every element to check with other element
        # for the outer loop we can use n - 1 since we don't need to compare when i is the last element
        '''
       [1, 2, 3, 4] 
        i | j 
        0 | 1 => 1 == 2?
        0 | 2 => 1 == 3?
        0 | 3 => 1 == 4?
        
        ''' 
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    print(i, j)
                    return True

        return False

        # Time: O(nˆ2) Space: O(1)

        # Solution 2: by sorting array
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

        # Time Complexity: O(n log n) due to sorting which takes time
        # Space Complexity: O(n) (due to sorting)

        # Solution 3: by using HashSet
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False
        
        # Time Complexity: O(n) loop iterates only once through each element
        # Space Complexity: O(n) using set takes n elements to store