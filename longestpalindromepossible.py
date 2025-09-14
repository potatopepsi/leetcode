# Needed to reference a solution to learn how to tackle this kind of problem
# Abhinash Singh

class Solution:
    def longestPalindrome(self, s: str) -> int:

        occurence = {}
        oddCounter = 0

        for char in s:
            if char in occurence:
                occurence[char] += 1
            else:
                occurence[char] = 1

            if occurence[char] % 2 == 1:
                oddCounter += 1
            else:
                oddCounter -= 1
        if oddCounter > 1:
            return len(s) - oddCounter + 1
        return len(s)
        