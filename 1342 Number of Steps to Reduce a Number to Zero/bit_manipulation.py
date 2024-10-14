
class Solution:
    def numberOfSteps(self, num: int) -> int:
        binary = bin(num)[2:]
        return len(binary)+binary.count('1')-1

#bit manipulation
#num =14          1110

#len() = 4        1111
#binary.count     1110
#最前面是1所以減掉  -1
#-----------------------
#                   6
