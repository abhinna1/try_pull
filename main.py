class Master:
    def __init__(self):
        self.__name = ""
    def set_name(self, name):
        self.__name= name
    def get_name(self):
        return self.__name

m1 = Master()
m1.set_name("Abhinna")
print(m1.get_name)