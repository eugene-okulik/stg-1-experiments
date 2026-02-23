def check_access(secret):
    def my_func(func):
        def wrapper(password):
            if password == secret:
                func()
            else:
                return
        return wrapper
    return my_func


@check_access(secret="1234")
def open_door():
    print("Дверь открыта")


open_door('1234')