weight_kg = [80.34, 97.67, 98.31, 80.59, 91.51, 88.54]

import numpy as np

np_weight_kg = np.array(weight_kg)

np_weight_lbs = np_weight_kg * 2.2

print(np_weight_lbs)