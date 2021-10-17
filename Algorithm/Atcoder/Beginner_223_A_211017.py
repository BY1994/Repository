"""
A task
"""

n = int(input())

print("No" if n % 100 or n < 100 else "Yes")
