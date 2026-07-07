class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -1 * nums[i]
            l = i+1
            r = len(nums) - 1
            while l<r:
                x = nums[l] + nums[r]
                if x == target:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                if x > target:
                    r-=1
                elif x < target:
                    l+=1
            
            
        return output