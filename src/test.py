class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"The {self.name} says {self.sound}")

    def __str__(self):
        return f"{self.name} makes a {self.sound} sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "woof")
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} barks: {self.sound}")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, "meow")
        self.age = age

    def speak(self):
        print(f"{self.name}, age {self.age}, meows: {self.sound}")


def print_animals(animals):
    for animal in animals:
        print(animal)
        animal.speak()


if __name__ == "__main__":
    animals = [
        Dog("Rex", "German Shepherd"),
        Cat("Whiskers", 3),
        Animal("Cow", "moo"),
    ]
    print_animals(animals)
