class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(num)
        my_dict = {"0": "1", "1": "0"}
        answer = []
        for value in num[2:]:
            answer.append(my_dict[value])
        answer = "".join(answer)
        return int(answer, 2)

    class Solution:
        def findComplement(self, num):
            """
            :type num: int
            :rtype: int
            """
            num = bin(num)[2:]
            num_c = ''.join([str(abs(int(i) - 1)) for i in num])
            return int(num_c, 2)

        class Solution:
            def findComplement(self, num):
                """
                :type num: int
                :rtype: int
                """
                bits = math.floor(math.log(num) / math.log(2))
                mask = 1
                while bits:
                    mask = mask << 1 | 1
                    bits -= 1

                return (num ^ 0xffffffff) & mask