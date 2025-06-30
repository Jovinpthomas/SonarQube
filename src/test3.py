# bad_code.py

import os
import sys

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, password):
        self.users.append((name, password))  # ⚠️ Storing passwords in plain text!

    def delete_user(self, name):
        for i in range(len(self.users)):
            if self.users[i][0] == name:
                del self.users[i]
                break

    def print_all(self):
        for u in self.users:
            print("User:", u[0], "Password:", u[1])  # ⚠️ Printing passwords

# Unused function
def unused():
    return True

# Poor structure
def bad():
    if True:
        if True:
            if True:
                print("Too deep!")  # ⚠️ Deep nesting
