class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        left = 1
        right = 1

        for i in range(len(nums)):
            k = len(nums) - i -1
            output[i] *= left
            left *= nums[i]
            output[k] *= right
            right *= nums[k]
        
        return output