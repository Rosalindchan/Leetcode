class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3=[]
        for a in nums1:
            index=nums2.index(a)
            if index+1>=len(nums2):
                nums3.append(-1)
            elif nums2[index+1]>a:
                nums3.append(nums2[index+1])
            else:
                i=index+1
                while i<len(nums2):
                    if nums2[i]>a:
                        nums3.append(nums2[i])
                        break
                    else:
                        i+=1
                        if i==len(nums2):
                            nums3.append(-1)
        return nums3