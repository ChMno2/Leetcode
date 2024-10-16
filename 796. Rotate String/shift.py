#檢查A是否可經過shift成為B
#一直左移直到長成一樣
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        if len(s)!=len(goal):
            return False
        for _ in range(len(s)):
            if s == goal:
                return True
            else:
                s = s[1:] + s[0]
        return False
