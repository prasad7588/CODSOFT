while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Choose operation:\n1] ADD\n2] SUB\n3] MULtiply\n4] DIVIDE\n"))

    if c == 1:
        print(a + b)
    elif c == 2:
        print(a - b)
    elif c == 3:
        print(a * b)
    elif c == 4:
        if b != 0:
            print(a / b)
        else:
            print("Cannot divide by zero!")
    else:
        print("Enter a valid input.")

    d = input("Do you want to continue? (yes/no): ")
    if d.lower() != "yes":
        break
