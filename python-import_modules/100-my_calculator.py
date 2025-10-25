#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)

    if argv[2] not in "+-*/":
        print("{}".format("Unknown operator. Available operators: +, -, * and /"))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    valid_operator = ['+', '-', '*', '/']
    operations = [add, sub, mul, div]

    operation_index = valid_operator.index(operator)
    ans = operations[operation_index](a, b)

    print("{} {} {} = {}".format(a, operator, b, ans))
    exit(0)
