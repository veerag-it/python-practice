class Solution(object):
    def isValid(self, s):
        bracket_pair={")":"(","}":"{","]":"["}
        stack=[]
        for ob in s:
            if ob in "({[":
                stack.append(ob)

            elif ob in ")}]":
                if not stack or stack.pop()!=bracket_pair[ob]:
                    return False
        return not stack

s=Solution()
print(s.isValid("{([])}"))  # True