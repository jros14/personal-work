

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
        self.add_all_characters(s)

    def add_all_characters(self, s):
        total = 0
        for char in range(len(s)):
            total += self.roman(s[char])
        return total

    def subtract_values(self, s):
        pass

# 1. add everything together
# 2. I, X and C can be used to subtract from the value
# CMXI = 911
# 100 + 1000 +10 + 1 = 1111 - 200 = 911

# total = 0
# for each letter in roman number
#   total += roman_value(letter)
#