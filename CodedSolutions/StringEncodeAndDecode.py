# Problem: String Encode and Decode

# Source: https://neetcode.io/problems/string-encode-and-decode 

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        joined = ""
        for currentString in strs:
            joined = joined + str(len(currentString)) + "$" + currentString
        return joined

    def decode(self, s: str) -> List[str]:
        stringList = []
        index = 0

        while index < len(s):
            currentString = ""
            sizeString = ""

            while s[index] != "$":
                sizeString += s[index]
                index += 1
            index += 1

            sizeStringInt = int(sizeString)
            while sizeStringInt > 0:
                currentString += s[index]
                sizeStringInt -= 1
                index += 1
            stringList.append(currentString)

        return stringList
