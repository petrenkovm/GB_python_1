
s = 0

while s<6 or s%2 != 0 :
    s = int(input("Enter an even number of cranes: "))

K = int(s/2)
PS = int(K//2)

print("Sergeq and Peter made {} cranes each. Kate made {} cranes".format(PS, K))
