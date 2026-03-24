class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        n = len(s)

        for c in set(s):
            first = s.find(c)
            last = s.rfind(c)
            if first < last:
                # add all unique middle characters between first and last
                middle_chars = set(s[first+1:last])
                for m in middle_chars:
                    res.add(c + m + c)

        return len(res)