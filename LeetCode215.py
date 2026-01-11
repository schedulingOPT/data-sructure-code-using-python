class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        return nums[n-k]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
