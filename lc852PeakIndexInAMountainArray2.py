class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lo, hi = 0, len(A) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] > A[mid - 1]:
                lo = mid
            else:
                hi = mid
