class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        parity = bits.pop()
        while bits and bits.pop(): #判断bits（）.pop==1
            parity ^= 1
        return parity == 0 #判断parity是否为0，是返回True，否返回False
#先取出最后一位字符0保存到parity中，然后由倒数第二位开始从右向左遍历，直到遇到倒数第二个0(bits.pop==0) while结束，通过parity ^= 1检查最后一个0和倒数第二个0之间1的个数： 有偶数个1，则parity最后值是0，返回True; 有奇数个1，则parity最后值是1，返回False;


class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
    #使用i作为增量指针，记录当前遍历到的位置。如果bits[i]=0，则i增加1(btis数组中前进一位)， 如果bits[i]=1，则i增加2(btis数组中前进两位)，最后保留bits数组最后一个字符(len(bits)-1)，判断bits数组剩余长度与i的大小(前进了多少位)是否相同，如果相同，说明最后一个比特字符0是一个一比特字符，返回True。否则返回False