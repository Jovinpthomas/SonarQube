# This script has intentional issues for SonarQube testing

import os
import sys


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.result = None  # Unused variable

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def divide(self):
        return self.x / self.y  # ⚠️ Division by zero not handled

    def unused_method(self):  # ⚠️ Dead code
        print("This method is never used")


def main():
    calc = Calculator(10, 0)

    print("Addition:", calc.add())
    print("Subtraction:", calc.subtract())
    print("Division:", calc.divide())  # ⚠️ Will crash with ZeroDivisionError

    password = input("Enter your password: ")  # ⚠️ Security hotspot (use getpass instead)
    print("You entered:", password)  # ⚠️ Bad practice: Echoing passwords


main()  # ⚠️ No if __name__ == "__main__"

