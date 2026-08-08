class Solution:
    def isValid(self, s: str) -> bool:
        Parentheses={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char in Parentheses:
                if stack and Parentheses[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
            