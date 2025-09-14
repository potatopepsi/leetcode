# Used solution as reference for a more efficient solution

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        i = 1

        while(i < n):
            mid = (i + n) // 2
            if(isBadVersion(mid)):
                n = mid
            else:
                i = mid + 1
        return i
        
        # # Base Case
        # if(n == 1):
        #     return (1)

        # # Try to decrease n
        # while(isBadVersion(n)):
        #     n = n // 2
        # n = n * 2
        # # print(n)
        # i = 0
        # while(i<n+1):
        #     if(isBadVersion(i)):
        #         return i
        #     else:
        #         i = i + 1