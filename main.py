# from itertools import count
import math

def is_composite(num):
  # num_square = math.sqrt(num)
  # int_num_sqt = math.ceil(num_square)
  # for element in range(1, int_num_sqt):
  #   divided_count = 0
  divided_count = 0
  while divided_count < 4:
    num_square = math.sqrt(num)
    print(num_square)
    int_num_sqt = math.ceil(num_square)
    for element in range(1, int_num_sqt, 1):
      # divided_count = 0
      
      is_divided = num % element
      if is_divided == 0:
        divided_count += 1
        
      element += 1
      print(f"divided count: {divided_count}, current element is: {element}, int num sqt: {int_num_sqt}.")
  return True

def is_prime(num):
  if num != 1 or is_composite(num) == False:
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