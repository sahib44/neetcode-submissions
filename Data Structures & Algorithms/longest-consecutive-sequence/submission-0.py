class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        size = {}
        parents = {}

        def find(n):
            while n != parents[n]:
                n = parents[n]
            return n


        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if size[p1] >= size[p2]:
                parents[p2] = p1
                size[p1] += size[p2]
            else:
                parents[p1] = p2
                size[p2] += size[p1]
        
        for n in nums:
                if n in parents:
                    continue
                parents[n] = n
                size[n] = 1
                
                if (n-1) in parents:
                    union(n,n-1)
                if (n+1) in parents:
                    union(n,n+1)

        return max(size.values()) if size else 0

    
