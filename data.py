import os

__LIMIT__ = 8
DIRNAME = 'securityQuestions'

users = [[''] * __LIMIT__] * __LIMIT__
passws = [[''] * __LIMIT__] * __LIMIT__
conta = set(range(__LIMIT__))

dict_users = {i: [''] * 8 for i in range(__LIMIT__)}
dict_passws = {i: [''] * 8 for i in range(__LIMIT__)}

def getUsers(): return users[:][:]

def getPassw(): return passws[:][:]

def getConta(): return conta

def getDictUsers(): return dict_users

def getDictPassws(): return dict_passws

def newAccount(user : list, passw : list, questions : tuple):
    global conta
    min_id = min(conta)
    
    users[min_id] = user
    passws[min_id] = passw

    dict_users.update({min_id: user})
    dict_passws.update({min_id: passw})

    for i in range(len(questions)):
        f = open('./' + DIRNAME + '/question' + str(min_id) + '_' + str(i) + '.txt', 'w')
        f.write(questions[i])
        f.close()

    '''
    f = open('./' + DIRNAME + '/user_' + str(''.join(user)) + '.txt', 'w')
    f.write(str(min_id))
    f.close()
    '''
    
    conta.remove(min_id)

def validAccount(user : list, passw : list):
    _id = -1
    for i in range(__LIMIT__):
        if users[i] == user:
            _id = i
            break

    if _id == -1: return -1
    if passws[_id] == passw: return _id
    return -2

def getOneUser(_id : int): return users[_id][:]

def setOnePassw(_id : int, npassw : list):
    passws[_id] = npassw

def deleteThisAccount(_id : int):
    users[_id] = [''] * 8
    passws[_id] = [''] * 8
    
    global conta
    conta.add(_id)

    dict_users.update({_id: [''] * 8})
    dict_passws.update({_id: [''] * 8})

    for i in range(2):
        #deberia checar si existen
        os.remove('./' + DIRNAME + '/question' + str(_id) + '_' + str(i) + '.txt')

def recoveryPass(user : list, questions : tuple):
    _id = -1
    
    for i in range(__LIMIT__):
        if users[i] == user:
            _id = i
            break
    if _id == -1: return -1
    
    '''
    if os.path.exists('./' + DIRNAME + '/user_' + str(''.join(user)) + '.txt'):
        file = open('./' + DIRNAME + '/user_' + str(''.join(user)) + '.txt', 'r')
        _id = int(file.read())
        file.close()
        print('_id: ', _id)
    else:
        return -1
    '''

    for i in range(len(questions)):
        file = open('./' + DIRNAME + '/question' + str(_id) + '_' + str(i) + '.txt', 'r')
        file_ans = file.read()

        if file_ans != questions[i]:
            return -2
        file.close()

    return passws[_id]
