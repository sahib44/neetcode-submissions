class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        suff = [0] * len(height)
        bigl = 0
        pref = [0] * len(height)
        bigr = 0

        for i in range(len(height)):
            if height[i] > bigl:
                bigl = height[i]
            suff[i] = bigl
            if height[len(height)-i-1] > bigr:
                bigr = height[len(height)-i-1]
            pref[len(height)-i-1] = bigr

        for i in range(1, len(height)):
            res += min(pref[i],suff[i]) - height[i]
        
        return res