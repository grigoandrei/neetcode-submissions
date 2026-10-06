class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1
        
        for letter in t:
            freq[letter] = freq.get(letter, 0) - 1

        print(freq)
        
        for n in freq:
            if freq[n] != 0:
                return False
        return True
        