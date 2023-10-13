'''
Question: Given an input string s, reverse the order of the words.

Input: s = "the sky is blue"
Output: "blue is sky the"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        rev = arr[::-1]
        st = ' '.join(rev)
        return st
    

'''
Question: Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
       s[:] = s[::-1]



#Two pointers
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while(left < right):
           s[left], s[right] = s[right], s[left]
           left+=1
           right-=1

        return s