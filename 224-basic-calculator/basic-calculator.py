class Solution:
    def calculate(self, s: str) -> int:
        curr_sum = 0
        curr_num = 0
        sign = 1
        stack = []
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char in "+-":
                curr_sum += sign * curr_num
                curr_num = 0
                sign = 1 if char == "+" else -1
            elif char is "(":
                stack.append(curr_sum)
                stack.append(sign)
                curr_sum = 0
                sign = 1
            elif char is ")":
                curr_sum += sign * curr_num
                curr_num = 0
                prev_sign = stack.pop()
                prev_sum = stack.pop()
                curr_sum = prev_sum + (prev_sign * curr_sum)
            i+=1
        return curr_sum + (sign * curr_num)


