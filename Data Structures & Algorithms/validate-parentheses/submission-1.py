class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # map of brackets
        bracks = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracks:
                top = stack.pop() if stack else '#'

                if bracks[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack

            