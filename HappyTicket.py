
n = ""
sum1 = sum2 = 0

while len(n) != 6 :
	n = input("Enter a ticket number:")

for i in range(3):
	sum1 += int(n[i])
	sum2 += int(n[-(i+1)])

if sum1==sum2:
	print('this ticket is lucky!')
else:
	print("this ticket isn't lucky!")

print('sum1 = ', sum1)
print('sum2 = ', sum2)