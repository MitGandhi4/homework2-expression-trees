from stack import Stack


def evaluate_postfix(expression):
    """
    Evaluate a postfix expression (space-separated string)
    and return the numeric result.
    """

    if not expression or expression.strip() == "":
        raise ValueError("Empty postfix expression")

    stack = Stack()
    tokens = expression.split()

    for token in tokens:

        try:
            number = int(token)
            stack.push(number)

        except ValueError:

            if token in ["+", "-", "*", "/"]:

                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "*":
                    result = operand1 * operand2
                elif token == "/":
                    if operand2 == 0:
                        raise ZeroDivisionError("Division by zero")
                    result = operand1 / operand2

                stack.push(result)

            else:
                raise ValueError(f"Invalid token: {token}")

    if stack.size() != 1:
        raise ValueError("Malformed postfix expression")

    return stack.pop()