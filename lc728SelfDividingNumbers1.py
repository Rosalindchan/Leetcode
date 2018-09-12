class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [i for i in range(left,right+1) if not any([m == '0' or i % int(m) != 0 for m in str(i)])]

    class Solution:
        def selfDividingNumbers(self, left, right):
            """
            :type left: int
            :type right: int
            :rtype: List[int]
            """

            return [x for x in range(left, right + 1) if all((i and (x % i == 0) for i in map(int, str(x))))]