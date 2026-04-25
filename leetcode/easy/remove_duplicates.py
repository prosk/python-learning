from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_pos = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[write_pos] = nums[i]
                write_pos += 1
        return write_pos         
    
def main():
    s = Solution()
    nums = [1, 3, 4, 4, 4, 6, 21, 56, 77, 77]
    s.removeDuplicates(nums)
    print(nums)

main()
    