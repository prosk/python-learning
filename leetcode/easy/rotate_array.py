from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k == 0:
            return 
        # inv: 0 < k < n
        self.reverse_sublist(nums, 0, n - k - 1)
        self.reverse_sublist(nums, n - k, n - 1)
        self.reverse_sublist(nums, 0, n - 1)
        
        
    def reverse_sublist(self, nums: List[int], start: int, end: int) -> None:
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        
def main():
    s = Solution()
    nums = [1, 3, 4, 4, 4, 6, 21, 56, 77, 77]
    s.rotate(nums, 3)
    print(nums)

main()