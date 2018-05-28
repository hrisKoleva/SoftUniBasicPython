side = int(input())

for row in range(1, side+1):
    if row == 1 or row == side:
        print(side*"*")
    else:
        print("*"+(side-2)*" " + "*")

