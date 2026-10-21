class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1

        for letter in t:
            freq[letter] = freq.get(letter, 0) - 1

        for n in freq.values():
            if n != 0:
                return False
        return True
        