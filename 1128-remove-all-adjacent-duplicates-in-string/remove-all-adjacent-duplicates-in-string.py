class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            char = s[i]
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
            i+=1
        return "".join(stack)
            
