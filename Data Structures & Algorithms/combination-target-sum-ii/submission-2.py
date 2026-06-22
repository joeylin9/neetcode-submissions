class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        cur = []
        cur_sum = 0

        def helper(i):
            nonlocal ans, cur, cur_sum

            if cur_sum == target:
                ans.append(cur.copy())
                return

            if i >= len(candidates) or cur_sum + candidates[i] > target:
                return

            # take
            cur_sum += candidates[i]
            cur.append(candidates[i])
            helper(i + 1)

            cur_sum -= candidates[i]
            cur.pop()

            # don't take: skip duplicates of candidates[i]
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            helper(j)

        helper(0)
        return ans