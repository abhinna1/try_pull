class Vehicle:
    def __init__(self, brand, color, age):
        self.__brand = brand
        self.__color = color
        self.__age = age

    def set_brand(brand):
        self.__brand=brand
    
    def get_brand(brand):
        return self.__brand
    
    def set_color(color):
        self.__color=color
    def get_color():
        return self.__color
    
    def set_age(age):
        self.__age = age
    def get_age():
        return self.__age


class Car(Vehicle):
    def __init__(self, brand, color, age):
        pass


car1 = Vehicle("Suzuki", "Grey", 5)
print(car1.get_age)