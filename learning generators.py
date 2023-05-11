import random

def lottery():
       for i in range(9):
              yield random.randint(1, 90)

       yield random.randint(1, 20)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))