def perform_operation(num1, num2, operation):

#Perform basic arithmetic operations.

    if operation =="add":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division be zero is not allowed"
        return num1 / num2
    else:
        return "Error:Invalid operation"