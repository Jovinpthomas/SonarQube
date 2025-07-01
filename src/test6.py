import subprocess
import hashlib
import os

# 🚨 Hardcoded password (secret detection)
db_password = "My$ecret123"

# 🚨 Insecure subprocess call (command injection risk)
def delete_user(username):
    subprocess.call(f"rm -rf /home/{username}", shell=True)

# 🚨 Insecure hash algorithm (weak cryptographic function)
def get_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

# 🚨 Unreachable code (bug)
def example():
    return
    print("This will never execute")

# 🚨 Redundant expression (always false)
def is_valid(x):
    if x and False:
        print("This will never print")

# 🚨 Empty except block (bad practice)
try:
    risky_operation()
except:
    pass

def risky_operation():
    raise ValueError("Just testing...")
