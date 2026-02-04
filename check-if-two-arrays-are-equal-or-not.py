# https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1
from collections import Counter

class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
            
        return Counter(a) == Counter(b)