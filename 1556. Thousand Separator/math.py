class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ''
        while n > 0:
            if len(ans) % 4 ==3:
                ans = '.' + ans
            ans= str(n%10) + ans
            n//=10
        return ans if ans else '0'
