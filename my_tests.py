def get_first_and_last_elem(arr):
    print(f"id(arr) = {id(arr)}")
    if len(arr) == 0:
        return None, None
    return arr[0], arr[-1]

def set_empty(arr):
    print(f"Inside set_empty id(arr) = {id(arr)}")
    arr = []
    print(f"Inside set_empty after setting id(arr) = {id(arr)}")
    print(f"arr = {arr}")

def main():
    my_list = [[(1, 2), (4, 5, 6)], "asdf", 3.456, 56, 89]
    print(f"id(my_list) = {id(my_list)}")
    # my_list = []
    first_elem, last_elem = get_first_and_last_elem(my_list)
    print(f"The first elem of {my_list} is {first_elem}, last elem is {last_elem}")

    print(f"Before my_list = {my_list}")
    set_empty(my_list)
    print(f"After my_list = {my_list}")

    a = 456
    print(f"The type of a is {type(a)}")
    a = "My string"
    print(f"Now the type of a is {type(a)}")
    a = my_list
    print(f"And now the type of a is {type(a)}")


if __name__ == "__main__":
    main()
