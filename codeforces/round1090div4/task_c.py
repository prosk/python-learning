for _ in range(int(input())):
    n = int(input())
    perm = []
    left, right = 1, 3*n 
    for _ in range(n):
        perm.append(left)
        perm.append(right-1)
        perm.append(right)
        left += 1
        right -= 2
    print(" ".join(map(str, perm)))    