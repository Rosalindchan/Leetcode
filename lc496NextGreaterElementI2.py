class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = dict()
        stack = []
        for num in nums2:
            if not stack or num < stack[-1]:
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    next_greater[stack.pop()] = num
                stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1
        return [next_greater[x] for x in nums1]

    # 通过栈维护一个升序或者降序序列的case，思路首先找出所有的res的map，然后再得出结果
    class Solution:
        def nextGreaterElement(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
            stack = []
            dict_res = {}
            for num in nums2:
                while len(stack) and stack[-1] < num:
                    dict_res[stack.pop()] = num
                stack.append(num)
            return [dict_res[num] if num in dict_res else -1 for num in nums1]

        class Solution:
            def nextGreaterElement(self, nums1, nums2):
                """
                :type nums1: List[int]
                :type nums2: List[int]
                :rtype: List[int]
                """
                numsmap = {}
                for i, num in enumerate(nums2):
                #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
                    for nextnum in nums2[i:]:
                        if nextnum > num:
                            numsmap[num] = nextnum
                            break
                return [numsmap.get(num, -1) for num in nums1]