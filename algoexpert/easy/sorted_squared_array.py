def sorted_squared_array(array):
    left, right = 0, len(array) - 1
    ans = [0] * len(array)
    ind = right
    while left <= right:
        if (abs(array[left]) >= abs(array[right])):
            ans[ind] = array[left] * array[left]
            left += 1
        else:
            ans[ind] = array[right] * array[right]
            right -= 1
        ind -= 1
    return ans    
            
def main():
    arr = [-7, -5, -2, 0, 2, 3, 6]
    ans = sorted_squared_array(arr)
    print(ans)

if __name__ == "__main__":
    main()                 