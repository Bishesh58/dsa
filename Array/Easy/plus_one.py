'''
Question:You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Approach: This function simulates the process of adding one to a number represented by an array of digits.
        # We start from the last digit (rightmost) and keep adding from right to left.
        # If the current digit is less than 9, we simply add 1 and return the updated array.
        # If the current digit is 9, we set it to 0 and continue with the next digit.
        # If we reach the leftmost digit and it is also 9, we add a new most significant digit '1' at the beginning.

        # Loop through the array from the last element (most significant digit) to the first element (least significant digit)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # If the current digit is less than 9, we can safely add 1 and return the updated array
                digits[i] += 1
                return digits
            else:
                # If the current digit is 9, set it to 0 and continue to the next most significant digit
                digits[i] = 0
        
        # If we reach this point, it means all digits were 9, so we add a new most significant digit '1'
        return [1] + digits


# Time: O(n) Space: O(1)