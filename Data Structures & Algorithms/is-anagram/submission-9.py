class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t):
            return False

        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1

        for letter in t:
            freq[letter] = freq.get(letter, 0) - 1

        for n in freq:
            if freq[n] != 0:
                return False
        return True
        