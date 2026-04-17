def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()


while True:
    print("\n1. Factorial")
    print("2. Fibonacci")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        num = int(input("Enter number: "))
        print("Factorial =", factorial(num))
    
    elif choice == "2":
        num = int(input("Enter number of terms: "))
        fibonacci(num)
    
    elif choice == "3":
        break
    
    else:
        print("Invalid choice")
