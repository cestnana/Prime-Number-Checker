# from itertools import count
import math

def is_composite(num):
  
  if num == 1 or num == 2:
    return False
  
  if num == 4:
    return True
  
  divided_count = 0
  num_square = math.sqrt(num)
  int_num_sqt = math.ceil(num_square)
  
  for element in range(2, int_num_sqt + 1, 1):
    is_divided = num % element
    if is_divided == 0:
      divided_count += 1
      
  if divided_count == 0:
    return False
  else:
    return True
  
def is_prime(num):
  if is_composite(num) == False and num != 1:
    return True
  else:
    return False

print(is_prime(73))
# except: True
print(is_prime(75))
# except: False
print(is_prime(1))
# except: False
print(is_prime(2))
# except: True
print(is_prime(4))
# except: False