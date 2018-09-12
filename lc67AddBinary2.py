class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # return bin(int(a,2)+int(b,2))[2:]
        if '' in (a, b):
            return a or b
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary('1', self.addBinary(a[:-1], b[:-1])) + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        return self.addBinary(a[:-1], b[:-1]) + '1'