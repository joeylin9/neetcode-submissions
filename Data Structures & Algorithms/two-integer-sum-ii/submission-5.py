class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            want = target-n
            l, r = i+1, len(numbers)-1
            while l<=r:
                m = (l+r)//2
                if numbers[m] == want:
                    return [i+1, m+1]
                elif numbers[m] < want:
                    l = m+1
                else:
                    r = m-1
            