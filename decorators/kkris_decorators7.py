#Task7

def check_pwd(pwd): 
    def decor(func):

        def wrapper():
            correct_pwd = '1111'
            if pwd == correct_pwd:
                func()
            else:
                pass
        return wrapper
    return decor


@check_pwd('1111')
def mainfunc():
    print('Correct password')


mainfunc()