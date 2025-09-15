print("Start Infinite Loop")
print("input '0' exit from the Loop\n")

while True :
    number = int(input("Enter the number : "))
    if (number == 0) :
        print("Exit")
        print("Bye Bye")
        break

    elif (number % 2 == 0) :
        print(number, "is even number")

    else :
        print(number, "is odd number")