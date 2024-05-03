import os
import data
from sort import Sort
from tree import Tree

class App:
    def __init__(self):
        print('Hecho por: Leonardo Fabyan\n')
        try:
            os.mkdir(os.path.join('.//', data.DIRNAME))
        except FileExistsError:
            pass
        self.__startUpMenu__()

    def __inputUser__(self):
        user = list(input(' usuario: '))

        if len(user) == 0:
            print('\n! Usuario vácio\n')
            return True,
        if len(user) > 8:
            print('\n! Usuario NO puede ser mayor que 8 caracteres\n')
            return True,
        if user.count(' ') > 0:
            print('\n! Usuario no puede tener espacios\n')
            return True,
        
        nuser = [''] * 8
        nuser[:len(user)] = user
        return False, nuser

    def __inputPassw__(self):
        passw = list(input(' contraseña: '))
        
        if len(passw) != 8:
            print('\n! Contraseña debe ser 8 caracteres\n')
            return True,
        if passw.count(' ') > 0:
            print('\n! Contraseña no puede tener espacios\n')
            return True,
        return False, passw

    def __inputQuestions__(self):
        print('\n Preguntas de seguridad:')
        print(' 1) ¿Cómo se llama su primera escuela?')
        answerQuestion1 = input(' >> ')

        print('\n 2) ¿Cúal fue el nombre de su primer mascota?')
        answerQuestion2 = input(' >> ')

        print('\n  Eso es todo')
        return answerQuestion1, answerQuestion2

    def __input__(self):
        _input = self.__inputUser__()
        if _input[0]: return False,

        _input += self.__inputPassw__()
        if _input[2]: return False,
        
        user, passw = _input[1], _input[3]
        
        return True, user, passw

    def __startUpMenu__(self):
        while True:
            print('Hola\n\n'
                  '1) Login\n'
                  '2) SignUp\n'
                  '3) Ver matrices\n'
                  '4) Recuperar contraseña\n'
                  '5) Algoritmos de ordenamiento\n'
                  '6) Trees\n'
                  'e) Salir')

            opc = input('-> ')
            if opc == 'e': break
            elif opc == '1': self.__login__()
            elif opc == '2': self.__signUp__()
            elif opc == '3': self.__showMatrices__()
            elif opc == '4': self.__recoveryPass__()
            elif opc == '5': Sort.menu()
            elif opc == '6': Tree.menu()
            else: print('\n! Opcion invalida\n')

    def __login__(self):
        while True:
            print('\nLogin\n')
            _input = self.__input__()
            if _input[0]: break
            
        _id = data.validAccount(_input[1], _input[2])
        if _id == -1:
            print('\n! Usuario NO encontrado\n')
            return
        if _id == -2:
            print('\n! Contraseña incorrecta\n')
            return
        self.id = _id
        self.__menu__()

    def __signUp__(self):
        if len(data.getConta()) == 0:
            print('\n! Limite de Usuarios alcanzado\n')
            return
        
        while True:
            print('\nNuevo Usuario\n')
            _input = self.__input__()
            if _input[0]: break
        answerQuestions = self.__inputQuestions__()
        data.newAccount(_input[1], _input[2], answerQuestions)
        print('\n$ cuenta añadida\n')

    def __showMatrices__(self):
        print('\nUsuarios:')
        for i in data.getUsers(): print(i)

        print('\nContraseñas:')
        for i in data.getPassw(): print(i)

        print('\nDiccionario de Usuarios:')
        _dict_users = data.getDictUsers()
        for i in _dict_users: print('[{}: {}]'.format(i, _dict_users[i]))

        print('\nDiccionario de Contraseñas:')
        _dict_passws = data.getDictPassws()
        for i in _dict_passws: print('[{}: {}]'.format(i, _dict_passws[i]))

        print('\nConta:\n{}\n'.format(data.getConta()))

    def __menu__(self):
        while True:
            print('\nHola {}\n'.format(''.join(data.getOneUser(self.id))))
            print('1) Cambiar contraseña\n'
                  '2) Eliminar esta cuenta\n'
                  'e) Salir\n')

            opc = input('-> ')
            if opc == 'e': break
            elif opc == '1': self.__changePassw__()
            elif opc == '2':
                data.deleteThisAccount(self.id)
                print('\n$ Eliminado\n')
                break
            else: print('\n!Opcion invalida\n')

    def __changePassw__(self):
        print('\nNueva Contraseña\n')
        npassw = self.__input_passw__()
        if not npassw: return
        data.setOnePassw(self.id, npassw[1])
        print('\n$ Cambio realizado\n')

    def __recoveryPass__(self):
        print()
        user = self.__inputUser__()
        if user[0]:
            return

        questions = self.__inputQuestions__()
        
        query = data.recoveryPass(user[1], questions)
        if query == -1:
            print('\n! Usuario no encontrado\n')
            return
        if query == -2:
            print('\n! No coincide las contraseñas de seguridad\n')
            return

        print('\nSu contraseña es:')
        print(''.join(query))
        print()

if __name__ == '__main__':
    app = App()