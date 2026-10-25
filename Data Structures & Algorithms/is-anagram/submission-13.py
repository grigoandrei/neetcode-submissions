class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1

        for letter in t:
            freq[letter] = freq.get(letter, 0) - 1

        for letter in freq.values():
            if letter != 0:
                return False

        return True