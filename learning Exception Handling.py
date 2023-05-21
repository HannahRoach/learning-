def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (3, 4, 6, 7, 9)

    for i in range(10):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError:
            do_stuff_with_number(10)
catch_this()