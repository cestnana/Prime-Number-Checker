import math

def is_positive_integer(num):
  # Check if the input is a positive integer
  return isinstance(num, int) and num > 0

def is_composite(num):
  # Handle small numbers directly
  if num in (1, 2):
    return False
  if num == 4:
    return True

  # Check if the number has any divisors other than 1 and itself
  limit = math.isqrt(num)  # More efficient than math.ceil(math.sqrt(num))
  
  for divisor in range(2, limit + 1):
    if num % divisor == 0:
      return True  # Found a divisor, it's composite
  
  return False  # No divisors found, it's not composite

def is_prime(num):
  # Validate input and check for prime status
  if not is_positive_integer(num):
    print("Please input a positive integer number.")
    return "Error: not a positive integer number"
  
  # Prime if not composite and not 1
  return not is_composite(num) and num != 1

# Test Cases
print(is_prime(73))  # Expected: True
print(is_prime(75))  # Expected: False
print(is_prime(1))   # Expected: False
print(is_prime(2))   # Expected: True
print(is_prime(4))   # Expected: False
print(is_prime(-1))  # Expected: "Error: not a positive integer number"

# Test is_positive_integer()
print(is_positive_integer(-1))  # Expected: False