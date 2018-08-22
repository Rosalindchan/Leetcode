class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in A:
            length = len(i)
            if (length % 2) != 0:
                for j in range(0,length//2+1,1):
                    if i[j] == i[-(j+1)]:
                        i[j] = 1 -i[j]
                        if j != length//2:
                            i[-(j+1)] = 1 - i[-(j+1)]
            else:
                for j in range(0,length//2,1):
                    if i[j] == i[-(j+1)]:
                        i[j] = 1 -i[j]
                        i[-(j+1)] = 1 - i[-(j+1)]
        return A