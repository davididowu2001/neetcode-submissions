class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        slow = 0
        max_res = 0
        visited = set()
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[slow])
                slow +=1
            visited.add(s[i])
            max_res = max(max_res, i - slow +1)
        return max_res