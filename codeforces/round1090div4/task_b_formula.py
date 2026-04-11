for t in range(int(input())):
	a = list(map(int, input().split()))
	print(max(a) * 2 - sum(a))