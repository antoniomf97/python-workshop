"""
Python Classes Example
"""


# class Mammal:
#     def __init__(self, order, family, genus, species) -> None:
#         self.order = order
#         self.family = family
#         self.genus = genus
#         self.species = species

#     def __str__(self) -> str:
#         return "{} |> {} |> {} |> {}".format(
#             self.order, self.family, self.genus, self.species
#         )


# class Dog(Mammal):
#     def __init__(self, name) -> None:
#         super().__init__("carnivora", "canidae", "canis", "c. familiaris")
#         self.dogname = name

#     def sound(self):
#         print(self.dogname + ": woof")


# class Cat(Mammal):
#     def __init__(self, name) -> None:
#         super().__init__("carnivora", "felidae", "felis", "f. catus")
#         self.catname = name

#     def sound(self):
#         print(self.catname + ": miau")


# print()
# dog = Dog(name="Doge")
# print(dog)
# dog.sound()
# print()

# cat = Cat(name="Garfield")
# print(cat)
# cat.sound()


# def get_animal_species(animal: Mammal):
#     print(animal.species)


# print()
# get_animal_species(dog)
# get_animal_species(cat)
# print()
