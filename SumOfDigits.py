# Option #1
"""
n = ""
sum = 0

while len(n) != 3 :
	n = input("Entered a tree-digit number:")
	
for i in n :
	sum += int(i)

print("sum of digits = ", sum)"""

# Option #2
n_str = ''
sum = 0

while len(n_str) !=3:
	n_str =input("Entered a tree-digit number:")

n_int = int(n_str) 

for i in range(3):
	
	fract1 = n_int % 10
	n_int //= 10

	sum += fract1

print("sum of digits = ", sum)
