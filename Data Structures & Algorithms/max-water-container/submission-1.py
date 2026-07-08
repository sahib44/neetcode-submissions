class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            dist = r-l
            area = dist * min(heights[l], heights[r])
            if area > res:
                res = area
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return res