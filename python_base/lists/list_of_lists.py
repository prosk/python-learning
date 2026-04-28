def main():
    lists = [[]] * 3
    print(f"lists after creation: {lists}")
    lists[0].append(3)
    lists[2].append("some value")
    print(f"lists after appending: {lists}")

    # right approach
    print("Right approach: ")
    lists = [[] for _ in range(3)]
    print(f"lists after creation: {lists}")
    lists[0].append(3)
    lists[2].append("some value")
    print(f"lists after appending: {lists}")


main()    