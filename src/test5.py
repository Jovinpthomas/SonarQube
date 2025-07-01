import os
import requests

# 🚨 Hardcoded secret (will be flagged as a vulnerability)
API_KEY = "sk_test_1234567890abcdef"

# 🚨 Unused variable (code smell)
unused_value = 42

# 🚨 Constant condition (will always be true)
if True:
    print("This will always run")

# 🚨 Nested if that could be merged (code smell)
user = "admin"
if user:
    if user == "admin":
        print("Admin access granted")

# 🚨 Insecure HTTP request (security hotspot)
def fetch_data():
    response = requests.get("http://example.com/data")  # insecure protocol
    return response.text

# 🚨 Using os.system (command injection risk if unvalidated input)
def run_command(cmd):
    os.system(cmd)

# 🚨 Potentially reading secrets from .env (include .env to detect)
db_password = os.getenv("DB_PASSWORD")
