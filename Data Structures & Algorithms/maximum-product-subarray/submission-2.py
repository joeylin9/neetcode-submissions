class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # if zeros, find greatest between
        # if even negatives, take all
        # if odd, split between and find greatest between
        if len(nums) == 1:
            return nums[0]

        segments = [] # list of tuples of (l,r, bool if even number of negs)
        l = 0
        negs = 0
        for i, n in enumerate(nums):
            if n == 0:
                if l!=i:
                    segments.append((l,i-1, negs%2==0))
                l = i+1
                negs = 0
            if n < 0:
                negs += 1

        if nums[-1]!=0:
            segments.append((l,len(nums)-1, negs%2==0))
        
        prefix = []
        suffix = []

        pre_prod, suf_prod = 1, 1
        for i in range(len(nums)):
            if nums[i] == 0:
                pre_prod = 1
                prefix.append(0)
            else:
                pre_prod *= nums[i]
                prefix.append(pre_prod)
            if nums[-i-1] == 0:
                suf_prod = 1
                suffix.append(0)
            else:
                suf_prod *= nums[-i-1]
                suffix.append(suf_prod)
        suffix.reverse()
        suffix.append(-math.inf)
        prefix.insert(0, -math.inf)

        ans = -math.inf
        for s,e,b in segments:
            if b:
                ans = max(ans, prefix[e+1])
            else: #odd number of negs
                for i in range(s, e+1):
                    if nums[i] < 0:
                        ans = max(ans, prefix[i], suffix[i+1])
        print(prefix)
        print(segments)
        return ans
        
