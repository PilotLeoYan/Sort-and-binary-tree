import os
import ast

DIRNAME = 'data'
PATH = os.path.join(os.getcwd(), DIRNAME)
QUESTION_1_PATH = os.path.join(PATH, 'Question1.txt')
QUESTION_2_PATH = os.path.join(PATH, 'Question2.txt')
USERS_PATH = os.path.join(PATH, 'Users.txt')

def init():
    if not os.path.exists(PATH):
        os.makedirs(PATH)

        questions_init = str(dict(map(lambda i: (i, 'empy'), range(8)))).replace(',', ',\n')

        with open(QUESTION_1_PATH, 'x') as file:
            file.writelines(questions_init)

        with open(QUESTION_2_PATH, 'x') as file:
            file.writelines(questions_init)

        users_init = str(dict(map(lambda i: (i, [['']*8, ['']*8]), range(8)))).replace(']],', ']],\n')
        with open(USERS_PATH, 'w') as file:
            file.writelines(users_init)

def getUsers() -> dict:
    with open(USERS_PATH, 'r') as file:
        lines = file.read()
    lines.replace(']],\n', ']],')
    return ast.literal_eval(lines)

def setUsers(users : dict):
    lines = str(users).replace(']],', ']],\n')
    with open(USERS_PATH, 'w') as file:
        file.write(lines)

def getAnswers() -> tuple:
    with open(QUESTION_1_PATH, 'r') as file:
        ans1 = file.read()
    ans1 = ast.literal_eval(ans1.replace(',\n', ','))

    with open(QUESTION_2_PATH, 'r') as file:
        ans2 = file.read()
    ans2 = ast.literal_eval(ans2.replace(',\n', ','))

    return ans1, ans2

def setAnswers(ans1 :dict, ans2 :dict):
    lines1 = str(ans1).replace(',', ',\n')
    lines2 = str(ans2).replace(',', ',\n')
    with open(QUESTION_1_PATH, 'w') as file:
        file.write(lines1)
    with open(QUESTION_2_PATH, 'w') as file:
        file.write(lines2)

def getTotalUsers() -> int:
    users = getUsers()
    max_key = 8
    for i in users:
        if users[i] == [['']*8, ['']*8]:
            max_key -= 1
    return max_key

def newAccount(name, passw, answers):
    users = getUsers()

    id_ = -1
    for i in users:
        if users[i] == [['']*8, ['']*8]:
            id_ = i 
            break      
    if id_ == -1: print('ocurrio un error')
    
    users.update({id_: [name, passw]})
    setUsers(users)

    ans = getAnswers()
    ans[0].update({id_: answers[0]})
    ans[1].update({id_: answers[1]})
    setAnswers(ans[0], ans[1])

def validAccount(name, passw):
    users = getUsers()

    id_ = -1
    for i in users:
        if users[i] == [name, passw]:
            id_ = i 
            break
    return id_

def getOneUser(id_ : int):
    users = getUsers()
    return users[id_][0]

def setOnePassw(id_, passw):
    users = getUsers()
    users[id_][-1] = passw
    setUsers(users)

def deleteThisAccount(id_):
    users = getUsers()
    users[id_] = [['']*8, ['']*8]
    setUsers(users)

    ans = getAnswers()
    ans[0].update({id_: 'empy'})
    ans[1].update({id_: 'empy'})
    setAnswers(ans[0], ans[1])

def recoveryPass(name, answers):
    users = getUsers()

    id_ = -1
    for i in users:
        if users[i][0] == name:
            id_ = i
            break
    if id_ == -1: return -1

    ans = getAnswers()
    if ans[0][id_] == answers[0]:
        if ans[1][id_] == answers[1]:
            return users[id_][1]
    return -2

def toString():
    users = getUsers()
    ans = getAnswers()

    print('\nUsuarios:')
    for i in users: print(users[i][0])

    print('\nContraseñas')
    for i in users: print(users[i][1])

    print('\nDiccionario:')
    print('{')
    for i in users: print(f"{i}: {users[i]}")
    print('}')

    print('\nPregunta 1:')
    for i in ans[0]: print(f"{i}: {ans[0][i]}")

    print('\nPregunta 2:')
    for i in ans[1]: print(f"{i}: {ans[1][i]}")