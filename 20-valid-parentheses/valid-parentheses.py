class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their matching opening brackets
        close_to_open = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for char in s:
            if char in close_to_open.values():
                stack.append(char)
            elif char in close_to_open:
                if not stack or stack.pop() != close_to_open[char]:
                    return False
        return len(stack) == 0

                