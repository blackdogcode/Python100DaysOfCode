import art


def add(a, b): return a + b


def subtract(a, b): return a - b


def multiply(a, b): return a * b


def divide(a, b): return a / b


calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)
print("Welcome to the Calculator!")

num_1 = float(input("What's the first number: "))
while True:
    for operator_symbol in calculator:
        print(operator_symbol)

    operator = input("Pick and operation: ")
    num_2 = float(input("What's the next number?: "))
    answer = calculator[operator](num_1, num_2)

    print(f"{num_1} {operator} {num_2} = {answer}")
    num_1 = answer

    
    if input("Type 'y' to continue calculating, or type 'n' to start a new calculation: ").lower() == "n":
        num_1 = float(input("What's the first number: "))
