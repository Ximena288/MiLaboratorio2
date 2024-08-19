class Perro:
    def __init__(self, nombre, raza, edad, peso, color, dueno, telefono):
        #atributos
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__color = color
        self.__dueno = dueno
        self.__telefono = telefono
        self.__estado = "NO ATENDIDO"
        self.__tamano = "Perro Grande" if peso >= 10 else "Perro Pequeno"
        self.__estado = "ATENDIDO"

        def ingresar_informacion(self):
            return {
            "Nombre": self.__nombre,
            "Raza": self.__raza,
            "Edad": self.__edad,
            "Peso": self.__peso,
            "Color": self.__color,
            "Dueno": self.__dueno,
            "Telefono": self.__telefono,
            "Estado": self.__estado,
            "Tamano": self.__tamano
        }

        # Funcion para registrar al perro
        def registrar_perro():
         nombre = input("Ingrese el nombre del perro: ")
    raza = input("Ingrese la raza del perro: ")
    edad = int(input("Ingrese la edad del perro (en años: "))
    peso = float(input("Ingrese el peso del perro (en kg): "))
    color = input("Ingrese el color del perro: ")
    dueno = input("Ingrese el nombre del dueno: ")
    telefono = input("Ingrese el telefono del dueno: ")

    #