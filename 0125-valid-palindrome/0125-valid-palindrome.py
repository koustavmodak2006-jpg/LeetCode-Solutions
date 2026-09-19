class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalpha() or i.isalnum():
                res+=i.lower()
        rev = res[::-1]
        
        if res == rev:
            return True
        return False