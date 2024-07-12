# Definición de la clase base Animal
class Animal:
    def __init__(self, name, species):
        self._name = name  # Atributo protegido
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        return f"{self._name} is a {self.species}"

    # Método adicional para demostrar encapsulación
    def get_name(self):
        return self._name


# Definición de la clase derivada Dog que hereda de Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Llamada al constructor de la clase base
        self.breed = breed

    # Sobrescritura del método make_sound para implementar polimorfismo
    def make_sound(self):
        return "Woof!"


# Definición de la clase derivada Cat que hereda de Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")  # Llamada al constructor de la clase base
        self.color = color

    # Sobrescritura del método make_sound para implementar polimorfismo
    def make_sound(self):
        return "Meow!"


# Creación de instancias de las clases derivadas
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")

# Demostración de polimorfismo al llamar al método make_sound
animals = [dog, cat]
for animal in animals:
    print(f"{animal} says {animal.make_sound()}")

# Uso del método get_name para demostrar encapsulación
print(f"The dog's name is {dog.get_name()}")
print(f"The cat's name is {cat.get_name()}")