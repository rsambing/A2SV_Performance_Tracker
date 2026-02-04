# https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1

class Solution:    
    def findUnion(self, a, b):
        ans = set(a + b)
        return ans