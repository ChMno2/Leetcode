class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pair = {}
        count = 0
        for domino in dominoes :
            key = tuple(sorted(domino))
            count += pair.setdefault(key,0)
            pair[key] += 1
        return count
