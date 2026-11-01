class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        count_s2 = {}
        l = 0

        for c in s1:
            count_s1[c] = count_s1.get(c, 0) + 1
        
        for r in range(len(s2)):
            count_s2[s2[r]] = count_s2.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                count_s2[s2[l]] -= 1
                if count_s2[s2[l]] == 0:
                    del count_s2[s2[l]]
                l += 1
            
            if count_s2 == count_s1:
                return True
        
        return False
        