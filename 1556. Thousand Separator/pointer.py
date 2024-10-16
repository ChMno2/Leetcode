#pointer
class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ''
        p = 0
        sn = str(n)
        for i in range(len(sn)):
            if i>0 and (len(sn)-i) % 3 ==0:
                ans +='.'   
            ans +=sn[i]
        return ans
