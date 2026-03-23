class Solution:
    def minFlips(self, s: str) -> int:
        s = [c for c in s]
        r = 0
        s = deque(s)
        overall = float('inf')
        odd_ones = 0
        even_ones = 0
        odd_zeros = 0
        even_zeros = 0
        while r < len(s):
            if r == 0:
                for i in range(len(s)):
                    if i % 2 == 1:
                        if s[i] == "1":
                            odd_ones += 1
                        else:
                            odd_zeros += 1
                    else:
                        if s[i] == "1":
                            even_ones += 1
                        else:
                            even_zeros += 1
            else:
                # s[-1] is the element rotated to the back last iteration
                # (it was at position 0, which is always even)
                if s[-1] == "1":       # ← was s[0]
                    even_ones -= 1
                else:
                    even_zeros -= 1

                odd_ones,even_ones=even_ones,odd_ones
                odd_zeros,even_zeros=even_zeros,odd_zeros

                if (len(s) - 1) % 2 == 1:
                    if s[-1] == "1":   # ← was s[0]
                        odd_ones += 1
                    else:
                        odd_zeros += 1
                else:
                    if s[-1] == "1":   # ← was s[0]
                        even_ones += 1
                    else:
                        even_zeros += 1

            mini = min(odd_ones + even_zeros, even_ones + odd_zeros)
            overall = min(mini, overall)
            if overall==0:
                return 0 
            s.append(s.popleft())
            r += 1
        return overall