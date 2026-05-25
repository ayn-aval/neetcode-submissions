class Solution:
    def validPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        if newStr == newStr[::-1]:
            return True
        
        for i in range(len(newStr)):
            newStr_delete = newStr[:i] + newStr[i+1:]
            if newStr_delete == newStr_delete[::-1]:
                return True 
        return False  
        




        
        
            