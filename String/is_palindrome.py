'''
Question: Given an integer x, return true if x is a palindrome and false otherwise.

Input: x = 121
Output: true

'''

# Approach:

# 1. We can solve by converting the num into string and reversing to compare if equal
# 2. By using two pointer

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        reverse = num_str[::-1]
        if(num_str == reverse):
            return True
        else:
            return False
        
        # Big Time:O(N) Space:O(N)


'''
Question: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

'''

# Approach:
    # - first we convert to lowercase
    # - second remove any special character or only have alphanumeric value by using build in method or not

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert to lowercase string
        s = s.lower()
        #two pointers
        left, right = 0,len(s) - 1
        #loop until the pointer meet
        while(left < right):
            #if not alphanumeric increase left pointer
            if(not (s[left] >= 'a' and s[left] <= 'z')):
                left+=1
            elif(not (s[right] >= 'a' and s[right] <= 'z')):
                right-=1
            elif (s[left] == s[right]):
                left+=1
                right-=1
            else:
                return False
        return True


        
# Big Time:O(n) Space:O(1)

# Same Big using built in alpanumeric method

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the input string to lowercase
        s = s.lower()
        # Initialize two pointers
        left, right = 0, len(s) - 1

        while left < right:
            # Move the left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move the right pointer to the next alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Check if the characters are the same
            if s[left] != s[right]:
                return False

            # Move both pointers towards each other
            left += 1
            right -= 1

        return True

'''
Time Complexity: The while loop iterates through the string from both ends (using the two pointers) until they meet in the middle. In the worst case, the loop will iterate through half of the string's characters, which is O(n/2) or simply O(n) in terms of the input string length.

Space Complexity: The code uses a constant amount of additional space for the two pointers (left and right). It doesn't use any additional data structures that depend on the input size, so the space complexity is O(1).
'''