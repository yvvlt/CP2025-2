number = int(input("Enter the number : "))
print("Your number is ", number)

for i in range(1, number):
    if(i % 2 == 0):
        continue
    elif (i % 3 == 0):
        continue

    else:
        print("number = ", i)