
m = int(input("Enter m:"))
n = int(input("Enter n:"))
k = int(input("Enter k:"))

if k < m*n and (k % m == 0 or k % n == 0):
	print("yes")
else:
	print("no")