import re
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["jen@gmail.com", "coding-list@python.org", "rin.backer@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")

pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)