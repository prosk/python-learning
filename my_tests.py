def get_first_and_last_elem(arr):
    if len(arr) == 0:
        return None, None
    return arr[0], arr[-1]


def main():
    my_list = [[(1, 2), (4, 5, 6)], "asdf", 3.456, 56, 89]
    # my_list = []
    first_elem, last_elem = get_first_and_last_elem(my_list)
    print(f"The first elem of {my_list} is {first_elem}, last elem is {last_elem}")
    a = 456
    print(f"The type of a is {type(a)}")
    a = "My string"
    print(f"Now the type of a is {type(a)}")
    a = my_list
    print(f"And now the type of a is {type(a)}")


if __name__ == "__main__":
    main()
