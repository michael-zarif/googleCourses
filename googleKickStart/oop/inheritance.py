class Furniture:
    _typeOfWood = "Teakwood"    # Protected
    # def __init__(self):
    #     self._typeOfWood = "Teakwood"

class Chair(Furniture):
    __numberOfLegs = 4  # Private
    # def __init__(self):
    #     # super is used to call base class methods.
    #     # Here we are calling the init of our base class to initialise the type of wood as Teakwood
    #     super().__init__()
    #     self.__numberOfLegs = 4

    def setWoodType(self, type_of_wood):
        self._typeOfWood = type_of_wood

    def displayChairSpecification(self):
        print("This chair is made of {} and has {} legs".format(self._typeOfWood, self.__numberOfLegs))

chair = Chair()
userChoice = input("Would you like to change the type of wood from Teakwood? Y/N: ")
if userChoice == 'Y':
    typeOfWood = input("Enter the type of wood you would like your chair to be made of: ")
    chair.setWoodType(typeOfWood)
chair.displayChairSpecification()