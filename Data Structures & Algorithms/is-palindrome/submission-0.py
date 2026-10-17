class Solution:
    def isPalindrome(self, s: str) -> bool:
        tempstr = ""

        for c in s:
            if c.isalnum():
                tempstr += c.lower()
        
        return tempstr == tempstr[::-1]