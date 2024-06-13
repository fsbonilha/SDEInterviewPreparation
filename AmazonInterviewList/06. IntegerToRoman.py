# Source: https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=954v5ops

# Problem: Integer to Roman

# First Solution:
class Solution:
    def intToRoman(self, num: int) -> str:
        letters = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        subtractive_forms = {
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM"
        }
        num_str = str(num)
        length = len(num_str)
        roman = ""
        letter_values = list(letters.keys())
        letter_values.sort(reverse=True)
        for i, digit in enumerate(num_str): 
            val = int(digit) * (10 ** (length - i - 1))
            if digit in ["4","9"]:
                roman += subtractive_forms[val]
            else:
                while val > 0:
                    for letter_value in letter_values:
                        if val >= letter_value:
                                times = val//letter_value
                                roman += (letters[letter_value] * times)
                                val -= times * letter_value
        return roman

# Better Solution:

class Solution:
    def intToRoman(self, num: int) -> str:
        letters = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        num_str = str(num)
        length = len(num_str)
        roman = ""
        letter_values = list(letters.keys())
        for i, digit in enumerate(num_str): 
            val = int(digit) * (10 ** (length - i - 1))
            while val > 0:
                for letter_value in letter_values:
                    if val >= letter_value:
                            times = val//letter_value
                            roman += (letters[letter_value] * times)
                            val -= times * letter_value
        return roman
