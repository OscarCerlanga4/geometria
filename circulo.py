#! C:\Users\alumno24\AppData\Local\Microsoft\WindowsApps\python.exe


from figura import figura



class circulo(figura):
    
    __color = None
    
    # TODO elevar color a la superclase
    def __init__(self, dimensions=..., color=None) -> None:
        super().__init__(dimensions)
        self.__color == color


if __name__ == "__main__":
    
    f0 = figura()
    print(f0.getDimesiones())
    print(f0)
    
    c0 = circulo()
    print(c0.getDimesiones())
    print(c0)