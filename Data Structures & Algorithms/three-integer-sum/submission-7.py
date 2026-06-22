class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, n in enumerate(nums):
            # skip duplicate fixed values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -n
            l, r = i + 1, len(nums) - 1

            while l < r:
                cur_sum = nums[l] + nums[r]

                if cur_sum < target:
                    l += 1
                elif cur_sum > target:
                    r -= 1
                else:
                    ans.append([n, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # skip duplicate left values after using one
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return ans