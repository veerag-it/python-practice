class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
    
x=121
s=Solution()
print(s.isPalindrome(x))