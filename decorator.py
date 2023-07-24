def check_login(f):
    # if user logged
    print('Checking')
    #if
    f()
    print('Done')

@check_login
def save():
    print('Saving')