def main():
    stack = []
    print("Appending values to the stack")
    for i in range(5):
        stack.append(i)
    print("The current state of the stack is: ", stack)
    print(f"len(stack) = {len(stack)}")    

    print(f"The value on the top is {stack[-1]}")
    last = stack.pop()
    prev = stack.pop()
    print(f"The last = {last} and the prev = {prev}")
    print("The current state of the stack is: ", stack)
    print(f"len(stack) = {len(stack)}")
    

if __name__ == "__main__":
    main()    