class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result=0
        AA={J[i] for i in range(len(J))}
        for i in range(len(S)):
            if S[i] in AA:
                result=result+1
        return result