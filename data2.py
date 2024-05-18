import os
import ast

DIRNAME = 'data'
PATH = os.path.join(os.getcwd(), DIRNAME)
QUESTION_1_PATH = os.path.join(PATH, 'Question1.txt')
QUESTION_2_PATH = os.path.join(PATH, 'Question2.txt')
USERS_PATH = os.path.join(PATH, 'Users.txt')

def init():
    """Si no existe la carpeta ./data, entonces crea dicha carpeta e inicializa
    por primera vez los archivos Users.txt, Question1.txt y Question2.txt en el formato
    requerido cómo un diccionario de Python para su uso."""
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
    """Lee el archivo Users.txt y lo combierte a un objeto diccionario de Python.
    
    Returns:
    -------
    dict
        contains all users key, names, passwords 
    """
    with open(USERS_PATH, 'r') as file:
        lines = file.read()
    lines.replace(']],\n', ']],')
    return ast.literal_eval(lines)

def setUsers(users : dict):
    """Escribe en el archivo Users.txt un diccionario de nombre y constraseñas de
    Usuarios.
    
    Parameters
    -------
    users : dict
    """
    lines = str(users).replace(']],', ']],\n')
    with open(USERS_PATH, 'w') as file:
        file.write(lines)

def getAnswers() -> tuple:
    """Lee los archivos Question1.txt y Question2.txt convertirlo a dos
    diccionarios.
    
    Returns:
    -------
    tuple
        contains two dictionaries.
    """
    with open(QUESTION_1_PATH, 'r') as file:
        ans1 = file.read()
    ans1 = ast.literal_eval(ans1.replace(',\n', ','))

    with open(QUESTION_2_PATH, 'r') as file:
        ans2 = file.read()
    ans2 = ast.literal_eval(ans2.replace(',\n', ','))

    return ans1, ans2

def setAnswers(ans1 : str, ans2 : str):
    """Escribe en los archivos Question1.txt y Question2.txt las respuestas
    a cada pregunta en sus archivos respectivos.
    
    Parameters
    -------
    ans1 : str
    ans2 : str
    """
    lines1 = str(ans1).replace(',', ',\n')
    lines2 = str(ans2).replace(',', ',\n')
    with open(QUESTION_1_PATH, 'w') as file:
        file.write(lines1)
    with open(QUESTION_2_PATH, 'w') as file:
        file.write(lines2)

def getTotalUsers() -> int:
    """Regresa el número de usuarios registrados
    
    Returns:
    -------
    int
    """
    users = getUsers()
    max_key = 8
    for i in users:
        if users[i] == [['']*8, ['']*8]:
            max_key -= 1
    return max_key

def newAccount(name, passw, answers):
    """Guarda en los archivos .txt nombre, contraseña y respuesta a cada pregunta
    en sus respectivos archivos.
    
    Parameters
    -------
    name : list
    passw : list
    answers : lsit
    """
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

def validAccount(name, passw) -> int:
    """Valida si el nombre de usuario y contraseña coinciden con algun
    usuario previamente guardado.

    Parameters
    -------
    name : list
    passw : list
    
    Returns:
    -------
    int
        user id
    """
    users = getUsers()

    id_ = -1
    for i in users:
        if users[i] == [name, passw]:
            id_ = i 
            break
    return id_

def getOneUser(id_ : int) -> list:
    """Regresa el nombre de usuario guardado en Users.txt.

    Parameters
    -------
    id : int
    
    Returns:
    -------
    list
        contains user name
    """
    users = getUsers()
    return users[id_][0]

def setOnePassw(id_, passw):
    """Establece una nueva contraseña se un usuario previamente registrado.
    
    Parameters
    -------
    id_ : int
    passw : list
    """
    users = getUsers()
    users[id_][-1] = passw
    setUsers(users)

def deleteThisAccount(id_):
    """Elimina un usario de los archivos .txt según por su id_/key:
    
    Parameters
    -------
    id_ : int
    """
    users = getUsers()
    users[id_] = [['']*8, ['']*8]
    setUsers(users)

    ans = getAnswers()
    ans[0].update({id_: 'empy'})
    ans[1].update({id_: 'empy'})
    setAnswers(ans[0], ans[1])

def recoveryPass(name, answers):
    """Recupera la constraseña de un usuario a partir de su nombre y
    las respuestas a las dos preguntas.
    
    Parameters
    -------
    name : list
    answers : list

    Returns
    -------
    int
        user id
    """
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
    """Imprime el contenido en Users.txt, Question1.txt y Question2.txt."""
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