class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        res = []
        for num in range(left, right + 1):
            num_temp = num
            while num_temp > 0:
                rem = num_temp % 10
                if rem == 0 or num % rem != 0:
                    break
                else:
                    num_temp = num_temp // 10
            if num_temp == 0:
                res.append(num)
        return res

    class Solution:
        def selfDividingNumbers(self, left, right):
            """
            :type left: int
            :type right: int
            :rtype: List[int]
            """
            res = []
            for i in range(left, right + 1):
                x_index = True
                for j in map(int, str(i)):
                    if j == 0 or i % j != 0:
                        x_index = False
                        break
                if x_index:
                    res.append(i)
            return res


