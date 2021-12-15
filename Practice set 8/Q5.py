# Display the following pattern using python function.

# ***
# **
# *

def print_pattern(n):
    for i in range(n):
        print("*" * (n-i))

print_pattern(3)
