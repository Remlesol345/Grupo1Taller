from DataBase.Connection import Connection
import os

class EliminarPersona:
    def __init__(self):
        self.coneccion = Connection()

    def eliminapersona(self):
            nombre = input('Ingrese el nombre del que quiere eliminar: ')
            sql = "delete from persona where nombre = '%s'" %nombre
            self.coneccion.cursor.execute(sql)
            self.coneccion.connection.commit()
            print("Elemento eliminado \n")
            os.system('pause')
            os.system('cls')