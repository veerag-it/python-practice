class Solution(object):
    def isPalindrome(self, x):
        num=x
        rev=0
        while(x>0):
            rem=x%10
            rev=(rev*10)+rem
            x=x//10
        return num==rev
    
x=121
s=Solution()
print(s.isPalindrome(x))