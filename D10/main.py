import art


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def div(a, b):
    if b == 0:
        print("Do not divide by 0.")
        return "Error"
    return a / b


def power(a, b):
    return a ** b


def calculate(given_symbol, a, b):
    calc_function = operations[given_symbol]
    return calc_function(a, b)


def calculator():
    print(art.logo)

    first_num = float(input("What is your first number? "))
    for key in operations:
        print(key)
    keep_going = True

    while keep_going:
        # user inputs
        symbol = input("Pick an operation: ")
        second_num = float(input("What is your next number? "))

        # calculate and print
        result = calculate(symbol, first_num, second_num)
        print(f"Solution: {first_num} {symbol} {second_num} = {result}")

        next_calculation = input(f"Type 'y' to continue calculating with {result} or type 'n' to start new calculation: ").lower()
        if next_calculation == 'y':
            first_num = result
        elif next_calculation == 'n':
            keep_going = False
            calculator()


operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": div,
    "^": power,
}

calculator()
