class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        visited = set()
        res = 0

        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[slow])
                slow += 1
            visited.add(s[i])
            res = max(res, i - slow + 1)
        return res
        