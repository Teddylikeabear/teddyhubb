import math

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y
    

def main():
    calculator = Calculator()

    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", calculator.add(num1, num2))
            elif choice == '2':
                print("Result:", calculator.subtract(num1, num2))
            elif choice == '3':
                print("Result:", calculator.multiply(num1, num2))
            elif choice == '4':
                print("Result:", calculator.divide(num1, num2))
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
