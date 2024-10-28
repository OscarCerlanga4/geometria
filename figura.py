#! C:\Users\alumno24\AppData\Local\Microsoft\WindowsApps\python.exe



class figura:
    
    __dimensiones = []
    
    
    def __init__(self, dimensions=[1,1]) -> None:
        self.__dimensiones = dimensions

    def getDimesiones(self):
        return self.__dimensiones
    
    def perimetro(self):
        return "P"
    
    def area(self):
        return "A"
    
    def __str__(self) -> str:
        answ = f"figura: area: "
        answ += f"area: {self.area()} " 
        answ += f"perim: {self.perimetro()} "
        return answ
    

if __name__ == "__main__":
    
    f0 = figura()
    #print (f0.getDimesiones())
    print(f0)
    
    f1 = figura ([2])
    #print(f1.getDimesiones())
    print(f1)
    
    f2 = figura ([2,3])
    #print(f2.getDimesiones())
    print(f2)