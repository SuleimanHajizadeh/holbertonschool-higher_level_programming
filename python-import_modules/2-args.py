#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Skriptin adını çıxmaq üçün [1:]
    n = len(args)
    
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))
    
    for i, arg in enumerate(args, 1):  # 1-dən başlamaq üçün
        print("{}: {}".format(i, arg))
