class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[2x4x6, 4x6, 6, 1]
        #[1, 1, 1x2, 1x2x4] --> reverse
        prefix_1, prefix_2 = [1], [1]

        for i in range(len(nums)-1):
            prefix_2.append(prefix_2[i]*nums[i])
            prefix_1.append(prefix_1[i]*nums[-i-1])
        
        ans = [prefix_1[-i-1]*prefix_2[i] for i in range(len(nums))]
        return ans
