# brute force
# time: O(n*n) | space O(1)
def two_number_brute_force(array, targetSum):
    for i in range(len(array) - 1):
        first_num = array[i]
        for j in range(i + 1, len(array)):
            second_num = array[j]
            if first_num + second_num == targetSum:
                return [first_num, second_num]
    return []   

# hash map: 
# time: O(N) | space O(N)
def two_number_hash_map(array, targetSum):
    seen = set()
    for num in array:
        to_sum = targetSum - num
        if to_sum in seen:
            return [to_sum, num]
        seen.add(num)    
    return []   

# two pointers
# time O(N*log(N)) : space O(1)
def two_number_two_pointers(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while(left < right):
        curr_sum = array[left] + array[right]
        if curr_sum == targetSum:
            return [array[left], array[right]]
        elif curr_sum < targetSum:
            left += 1
        else:
            right -= 1
    return []      

def main():
    arr = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 11

    print(two_number_brute_force(arr, target_sum))

    print(two_number_hash_map(arr, target_sum))

    print(two_number_two_pointers(arr, target_sum))

if __name__ == "__main__":
    main()