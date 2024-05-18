import data2
from sort import Sort
from tree import Tree

class App:
    """Class App

    Esta clase de interfaz para el usuario, además de ser la base para los
    distintos modulos y package para este proyecto.

    Módulos:
    - data2.py

    Package:
    - sort
    . tree
    """
    def __init__(self):
        """Incio del programa y configuración inicial"""
        print('Hecho por: Leonardo Fabyan\n')
        data2.init()
        self.__startUpMenu__()

    def __inputUser__(self):
        """Permite al usuario ingresar un string para convertirlo a una
        lista de 8 elementos que contenga cada caracter ingresado.
        Usado para ingresar el nombre del Usuario.
        
        Returns:
        -------
        list
            list of 8 characters 
        """
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
        """Permite al usuario ingresar un string para convertirlo a una
        lista de 8 elementos que contenga cada caracter ingresado.
        Usado para ingresar la contraseña del Usuario.

        Returns:
        -------
        list
            8 character list 
        """
        passw = list(input(' contraseña: '))
        
        if len(passw) != 8:
            print('\n! Contraseña debe ser 8 caracteres\n')
            return True,
        if passw.count(' ') > 0:
            print('\n! Contraseña no puede tener espacios\n')
            return True,
        return False, passw

    def __inputQuestions__(self):
        """Regresa las respuestas para cada pregunta de seguridad usado para
        data2.py. 
        Usado para establecer y validar preguntas de seguridad.

        Returns:
        -------
        tuple
            contains two strings, one per question
        """
        print('\n Preguntas de seguridad:')
        print(' 1) ¿Cómo se llama su primera escuela?')
        answerQuestion1 = input(' >> ')

        print('\n 2) ¿Cúal fue el nombre de su primer mascota?')
        answerQuestion2 = input(' >> ')

        print('\n  Eso es todo\n')
        return answerQuestion1, answerQuestion2

    def __input__(self):
        """Obtiene y valida que el nombre y contraseña de Usuario sea
        de formato lista y de 8 caracteres.

        Returns:
        -------
        tuple
            contains format validated, user name, user password
        """
        _input = self.__inputUser__()
        if _input[0]: return False,

        _input += self.__inputPassw__()
        if _input[2]: return False,
        
        user, passw = _input[1], _input[3]
        
        return True, user, passw

    def __startUpMenu__(self):
        """Inicia un bucle con las distintas opciones del programa para
        acceder a dichas opciones"""
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
        """Obtiene y usa data2.py para validar que los datos sean correctos.
        Usado para acceder al submenu __menu__()
        """
        while True:
            print('\nLogin\n')
            _input = self.__input__()
            if _input[0]: break
            
        _id = data2.validAccount(_input[1], _input[2])
        if _id == -1:
            print('\n! datos erróneos\n')
            return
        self.id = _id
        self.__menu__()

    def __signUp__(self):
        """Obtiene los datos del usuario y usa data2.py para crear un nuevo 
        usuario si es disponible. Unicamente se puede tener hasta 8 usuarios
        guardados simultaneamente."""
        if data2.getTotalUsers() >= 7:
            print('\n! Limite de Usuarios alcanzado\n')
            return
        
        while True:
            print('\nNuevo Usuario\n')
            _input = self.__input__()
            if _input[0]: break

        answer_questions = self.__inputQuestions__()
        data2.newAccount(_input[1], _input[2], answer_questions)
        print('$ cuenta añadida\n')

    def __showMatrices__(self):
        """Se usa para mostrar todos los datos almecenados en ./data cómo:
        - Users.txt
        - Question1.txt
        - Question2.txt"""
        data2.toString()
        print()

    def __menu__(self):
        """Un menu en bucle para mostrar todos las opciones para un usuario ya ingresado."""
        while True:
            print('\nHola {}\n'.format(''.join(data2.getOneUser(self.id))))
            print('1) Cambiar contraseña\n'
                  '2) Eliminar esta cuenta\n'
                  'e) Salir\n')

            opc = input('-> ')
            if opc == 'e': break
            elif opc == '1': self.__changePassw__()
            elif opc == '2':
                data2.deleteThisAccount(self.id)
                print('\n$ Eliminado\n')
                break
            else: print('\n!Opcion invalida\n')

    def __changePassw__(self):
        """Función para cambiar la contraseña de un usuario ya ingresado."""
        print('\nNueva Contraseña\n')
        npassw = self.__inputPassw__()
        if not npassw: return

        data2.setOnePassw(self.id, npassw[1])
        print('\n$ Cambio realizado')

    def __recoveryPass__(self):
        """Función para poder recuperar la contraseña de un usuario a partir
        de su nombre de usuario y las respuestas de ambas preguntas de seguridad."""
        print()
        user = self.__inputUser__()
        if user[0]: return

        questions = self.__inputQuestions__()
        
        query = data2.recoveryPass(user[1], questions)
        if query == -1:
            print('\n! Usuario no encontrado\n')
            return
        if query == -2:
            print('\n! No coincide las contraseñas de seguridad\n')
            return

        print('Su contraseña es:', ''.join(query))
        print()

if __name__ == '__main__':
    """Inicial el proyecto una sola vez por ejecución."""
    app = App()
