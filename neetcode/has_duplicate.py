from typing import List

def has_duplicate(nums: List[int]) -> bool:
    seen = set()
    for val in nums:
        if val in seen:
            return True
        seen.add(val)
    return False  


def main():
    ans = has_duplicate([1, 2, 3, 4])
    print(ans)
    ans = has_duplicate([3, 1, 2, 3, 4])
    print(ans)


if __name__ == "__main__":
    main()