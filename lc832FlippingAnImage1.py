class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        l=len(A)
        for i in range(l):
            A[i].reverse()
            for j in range(l):
                #A[i][j]=1^A[i][j]
                A[i][j]=1-A[i][j]#经过测试，这条更快
        return A