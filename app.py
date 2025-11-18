import hashlib
import os

# Hardcoded secret → Security Hotspot
SECRET_KEY = "my-super-secret-key"

# SQL Injection vulnerability
def insecure_sql_query(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "';"
    print("Executing:", query)
    return query

# Duplicate code (intentionally repeated)
def duplicate_logic(x):
    if x > 10:
        return "High"
    elif x <= 10:
        return "Low"
    else:
        return "Unknown"

def duplicate_logic_v2(x):  # duplicate
    if x > 10:
        return "High"
    elif x <= 10:
        return "Low"
    else:
        return "Unknown"

# Long and complex method → Code smell + complexity
def process_data(items):
    total = 0
    for item in items:
        if item > 5:
            total += item
        else:
            if item == 5:
                total += 5
            elif item == 4:
                total += 4
            elif item == 3:
                total += 3
            elif item == 2:
                total += 2
            elif item == 1:
                total += 1
            else:
                total += 0

    # Dead code
    unused_var = 12345

    return total

# Weak hashing → Vulnerability
def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

# Unused function → code smell
def unused_function():
    print("I am never called.")

# Main execution
if __name__ == "__main__":
    print("Starting bad Python program...")

    # Vulnerable SQL
    insecure_sql_query("admin' OR '1'='1")

    # Code duplication tests
    print(duplicate_logic(8))
    print(duplicate_logic_v2(15))

    # Complexity
    items = [1, 5, 10, 20, 3]
    print("Processed total:", process_data(items))

    # Weak hash
    print("Password hash:", weak_hash("password123"))
