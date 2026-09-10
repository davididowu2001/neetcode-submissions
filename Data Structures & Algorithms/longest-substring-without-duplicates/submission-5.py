class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        slow = 0
        res = 0

        for fast in range(len(s)):
            while s[fast] in visited:
                visited.remove(s[slow])
                slow +=1
            visited.add(s[fast])
            res = max(res, fast - slow + 1)
        return res