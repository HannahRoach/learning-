actor = {"name": "Joey Snow", "rank": "one"}

def get_last_name():
    return actor["name"].split()[1]

get_last_name()
print("All exceptions met! Great job!")
print("The actor's last name is %s" % get_last_name())