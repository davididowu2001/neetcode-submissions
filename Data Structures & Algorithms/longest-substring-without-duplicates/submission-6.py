class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        maxString = 0
        visited = set()

        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[slow])
                slow += 1
            visited.add(s[i])
            maxString = max(maxString, len(visited))
        return maxString