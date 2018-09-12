class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=int(a,2)
        b=int(b,2)
        c=a+b
        return bin(c)[2:]
        #return bin(int(a,2)+int(b,2))[2:]