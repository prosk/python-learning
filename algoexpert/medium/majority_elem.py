# Smart voting alg: time O(n) | space O(1)
def majority_elem_voting_alg(array):
    count = 0
    curr = array[0]
    for elem in array:
        if count == 0:
            curr = elem
        if (elem == curr):
            count += 1
        else:
            count -= 1 
    return curr 

# Bit manipulation alg: time O(n) | space O(1)
def majority_elem_by_bits_alg(array):
    half = len(array) // 2
    ans = 0
    for curr_bit in range(32):
        curr_bit_val = 1 << curr_bit
        ones_cnt = 0
        for elem in array:
            if (elem & curr_bit_val) != 0:
                ones_cnt += 1
            if ones_cnt > half:
                ans += curr_bit_val
                break
    return ans  

def main():
    arr = [1, 20, 3, 20, 20, 4, 20, 20, 5, 20, 1]

    ans1 = majority_elem_voting_alg(arr)
    print(f"Voting alg ans = {ans1}")

    ans2 = majority_elem_by_bits_alg(arr)
    print(f"Bit manipulation alg ans = {ans2}")


if __name__ == "__main__":
    main()