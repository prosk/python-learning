from typing import List

# Код на Java немного даже проще - так как в Java есть цикл do while, которого нет в Python 
# public void rotate(int[] nums, int k) {
#         k = k % nums.length;
#         int count = 0;
#         for (int start = 0; count < nums.length; start++) {
#             int current = start;
#             int prev = nums[start];
#             do {
#                 int next = (current + k) % nums.length;
#                 int temp = nums[next];
#                 nums[next] = prev;
#                 prev = temp;
#                 current = next;
#                 count++;
#             } while (start != current);
#         }
#     }

class Solution:
    def rotate_btfl(self, nums: List[int], k:int) -> None:
        n = len(nums)
        k %= n
        start_pos = replace_count = 0
        while replace_count < n:
            current_pos, prev_elem = start_pos, nums[start_pos]
            # здесь по сути while True + проверка в конце цикла с break имитирует цикл do..while 
            while True:  
                next_pos = (current_pos + k) % n
                nums[next_pos], prev_elem = prev_elem, nums[next_pos]
                current_pos = next_pos
                replace_count += 1

                if start_pos == current_pos:
                    break
            start_pos += 1

    def rotate_opt(self, nums: List[int], k:int) -> None:
        n = len(nums)
        k = k % n
        if k == 0:
            return
        replace_count = start_pos = 0
        while replace_count < n:
            cur_elem = nums[start_pos]
            next_pos = (start_pos + k) % n 
            while next_pos != start_pos:
                nums[next_pos], cur_elem = cur_elem, nums[next_pos]
                replace_count += 1
                next_pos = (next_pos + k) % n
            # next_pos == start_pos
            nums[next_pos] = cur_elem   
            replace_count += 1 
            start_pos += 1    


    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k == 0:
            return 
        # inv: 0 < k < n

        # Approach 1 (Let n=7 and k=3)
        # Original List                   : 1 2 3 4 5 6 7
        # After first reversing           : 4 3 2 1 5 6 7
        # After second reversing          : 4 3 2 1 7 6 5
        # After third reversing           : 5 6 7 1 2 3 4 --> Result
        self.reverse_sublist(nums, 0, n - k - 1)
        self.reverse_sublist(nums, n - k, n - 1)
        self.reverse_sublist(nums, 0, n - 1)

        # Approach 2 (Let n=7 and k=3)
        # Original List                   : 1 2 3 4 5 6 7
        # After reversing all numbers     : 7 6 5 4 3 2 1
        # After reversing first k numbers : 5 6 7 4 3 2 1
        # After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
        # self.reverse_sublist(nums, 0, n - 1)
        # self.reverse_sublist(nums, 0, k - 1)    
        # self.reverse_sublist(nums, k, n - 1)  
        
        
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