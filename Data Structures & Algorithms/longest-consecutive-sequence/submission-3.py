class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        current_streak = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i + 1]:
                current_streak += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                current_streak = 1
            
            count = max(count, current_streak)

        return count