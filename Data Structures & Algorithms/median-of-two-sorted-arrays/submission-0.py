class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newList = []
        pointNums1, pointNums2 = 0, 0

        while pointNums1 < len(nums1) and pointNums2 < len(nums2):
            if nums1[pointNums1] < nums2[pointNums2]:
                newList.append(nums1[pointNums1])
                pointNums1 += 1
            else:
                newList.append(nums2[pointNums2])
                pointNums2 += 1
        
        newList.extend(nums1[pointNums1:])
        newList.extend(nums2[pointNums2:])
        
        total = len(newList)

        if len(newList) % 2 == 0:
            return (newList[total // 2 - 1] + newList[total // 2]) / 2
        else:
            return newList[total // 2]
