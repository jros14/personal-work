

class Solution:
    def roman(self, letter):
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000

        if letter == "I":
            return I
        elif letter == "V":
            return V
        elif letter == "X":
            return X
        elif letter == "L":
            return L
        elif letter == "C":
            return C
        elif letter == "D":
            return D
        elif letter == "M":
            return M

    def romanToInt(self, s: str) -> int:
        s = s.upper()
        added_total = self.add_all_characters(s)
        return self.subtract_values(s, added_total)


    def add_all_characters(self, s):
        added_total = 0
        for char in range(len(s)):
            added_total += self.roman(s[char])
        return added_total

    def subtract_values(self, s, added_total):
        for char in range(len(s)-1):
            if s[char] == "I" and (s[char+1] == "V" or s[char+1] == "X"):
                added_total -= 2
            elif s[char] == "X" and (s[char+1] == "L" or s[char+1] == "C"):
                added_total -= 20
            elif s[char] == "C" and (s[char+1] == "D" or s[char+1] == "M"):
                added_total -= 200
        subtracted_total = added_total
        return subtracted_total



# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

# 1. add everything together
# 2. I, X and C can be used to subtract from the value
# CMXI = 911
# 100 + 1000 +10 + 1 = 1111 - 200 = 911

# total = 0
# for each letter in roman number
#   total += roman_value(letter)
#