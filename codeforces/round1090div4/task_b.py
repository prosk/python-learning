def main():
    t = int(input())
    for _ in range(t):
        solve()


def solve():
    arr = list(map(int, input().split()))
    arr.sort()
    sum = 0
    for i, val in enumerate(arr):
        sum += -val if i < len(arr) - 1 else val 
    print(sum)

main()        
