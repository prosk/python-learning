from typing import List

def get_concatenation(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * 2 * n 
    for i, val in enumerate(nums):
        ans[i] = ans[n + i] = val
    return ans


def main():
    ans = get_concatenation([1, 2, 3, 4])
    print(ans)


if __name__ == "__main__":
    main()




