import json

def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)

salaries = '{"Alex" : 2000, "Jill" : 5000 }'
new_salaries = add_employee(salaries, "Me", 9000)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alex"])
print(decoded_salaries["Jill"])
print(decoded_salaries["Me"])