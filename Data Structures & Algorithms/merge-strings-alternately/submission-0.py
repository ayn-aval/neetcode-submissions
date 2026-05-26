class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)

        new_string = ""

        for i in range(max(m,n)):
             if i < m :
                new_string += word1[i]
             if i < n :
                new_string += word2[i]
        return new_string
            
            
            



        
        