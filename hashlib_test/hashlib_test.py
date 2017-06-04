import hashlib
# md5=hashlib.md5()
# md5.update('huu'.encode('utf-8'))
# print(md5.hexdigest())

def calc_md5(user,password):
    md5=hashlib.md5()
    md5.update(user.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    md5.update('HUU'.encode('utf-8'))
    #print(md5.hexdigest())
    return md5.hexdigest()


db = {}


def login(user,password):
    if not user in db:
        print('user is not exist')
        return
    if  calc_md5(user,password)==db[user]:
        print('password is True,login successed!')
    else:
        print('password is False,login failed!')

def register(user,password):
    db[user]= calc_md5(user,password)

def logreg():
    cmd=input('input "register" or "login":')
    user=input('username:')
    password=input('password:')   
    if cmd =='register':
        register(user,password)
        logreg()
    elif cmd =='login':
        login(user,password)
    else :
        print('please input right cmd')

if __name__ == '__main__':
    logreg()