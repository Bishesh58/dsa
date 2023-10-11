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