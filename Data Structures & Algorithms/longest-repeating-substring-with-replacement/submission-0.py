class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        slow = 0
        max_freq = 0
        max_len = 0

        for fast in range(len(s)):
            count[s[fast]] = count.get(s[fast], 0) + 1
            max_freq = max(max_freq, count[s[fast]])

            win_len = fast - slow + 1

            if win_len - max_freq > k:
                count[s[slow]] -= 1
                slow +=1
            max_len = max(max_len, fast - slow + 1)

        return max_len