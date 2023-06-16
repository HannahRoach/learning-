scores = [56, 99, 68, 45, 9, 61, 8, 77, 58, 20]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)