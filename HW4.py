def calculator():
    try:
        # ввод первого числа
        num1 = float(input("Enter the first number: "))

        # Ввод операции
        operation = input("Enter action (+, -, *, /): ")

        # Ввод второго числа
        num2 = float(input("Enter the second number: "))

        # Выполнение операции
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:# проверка деления на 0
                print("Error: dividing by 0 is impossible!")
                return
            result = num1 / num2
        else:
            print("Error: Invalid action! Choose from (+, -, *, /).")#ывод ошибки при некорректном вводе данных
            return

        # Вывод результата
        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter correct numbers!")# вывод ошибки при некорректном вводе данных(букв, либо символов)








# способ match
num1 = input("Enter the first number: ") # входящие данные
operation = input("Enter action (+, -, *, /): ")
num2 = input("Enter the second number: ")
# Преобразование целого числа в дробное
try:
    num1 = float(num1)
    num2 = float(num2)

    match operation:
        case '+':
            print(f"Result: {num1 + num2}")
        case '-':
            print(f"Result: {num1 - num2}")
        case '*':
            print(f"Result: {num1 * num2}")
        case '/':
            if num2 == 0:
                print("Error: division by 0 is impossible!")
            else:
                print(f"Result: {num1 / num2}")
        case _:  # Аналог else
            print("Invalid operation. Please try again.")
except ValueError:
    print("Error: Please enter correct numbers!")



