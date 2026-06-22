class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        two_sum = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                two_sum[nums[i]+nums[j]].append((i,j))
        
        triplet_seen = set()
        ans = []
        for i,n in enumerate(nums):
            if -n in two_sum:
                for x,y in two_sum[-n]:
                    triplet = frozenset((nums[x], nums[y], nums[i]))
                    if i != x and i != y and triplet not in triplet_seen:
                        ans.append([nums[x],nums[y],nums[i]])
                        triplet_seen.add(triplet)
        return ans