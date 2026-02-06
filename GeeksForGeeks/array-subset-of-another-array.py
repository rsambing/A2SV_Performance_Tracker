# https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1

from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        mpA = Counter(a)
        mpB = Counter(b)
        
        for key in mpB:
            if mpB[key] > mpA.get(key, 0):
                return False
                
        return True
