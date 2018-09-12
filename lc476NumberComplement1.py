class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_b=bin(num)
        a=""
        for i in range(2,len(num_b)):
            a+=str(1-int(num_b[i]))
        return int(a,2)