class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l +=1
            visited.add(s[r])
            res = max(res, r-l + 1)
        return res



"zxyzxyz"

'''
Algorithm
fast and slow pointer

while element isnt in the set, add element and increment fast. then calculate max window each time

then move slow pointer, till set[element] isnt in the set, then increment by 1

slow


'''