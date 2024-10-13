class Solution:
    def maxPower(self, s: str) -> int:
        prev_char = None
        count = 0
        power = 0
        for char in s:
            if char ==prev_char:
                count+=1
            else:
                prev_char = char
                count = 1
            power = max(power,count)
        return power
