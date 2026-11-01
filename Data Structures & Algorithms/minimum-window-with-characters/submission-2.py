class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        count_s = {}
        l = 0

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        need = len(count_t)
        have = 0
        
        best_window = []
        length = float('inf')
        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r], 0) + 1
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have += 1
                while have == need:
                    if r - l + 1 < length:
                        best_window = [l, r]
                        length = r - l + 1
                    count_s[s[l]] -= 1
                    if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                        have -= 1
                    l += 1
        
        if length == float('inf'):
            return ""
        

        l,r = best_window
        return s[l:r + 1]

        