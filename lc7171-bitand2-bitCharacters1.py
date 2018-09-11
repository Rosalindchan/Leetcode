class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        l=len(bits)
        if l==1:
            return True
        else:
            for i in range(1,l):
                if bits[-i-1]==0:
                    if i%2==1:
                        return True
                        break
                    else:
                        return False
                        break
                elif i==l-1:
                    if (l-1)%2==0:
                        return True
                    else:
                        return False