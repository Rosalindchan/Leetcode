class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(map(lambda x:list(map(lambda y:y^1,x[::-1])),A))
    #line=line[::-1]就相当于line.reverse()

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for line in A:
            line = line[::-1]
            result.append(list(map(lambda a : int(a!=1),line)))
            result.append(list(map(lambda a: a ^1, line)))
            #int(a!=1)判断a是否为1，返回True或False，转成int就是1或0
        return result