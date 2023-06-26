# Example for class inheritance and composition
class Clothing:
    material = ""
    stock = {'name': [], 'material': [], 'amount': []}
    def __init__(self, name):
        self.name = name
    def add_item(self, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(material)
        Clothing.stock['amount'].append(amount)
    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in self.stock['material']:
            if item == material:
                count += self.stock['amount'][n]
                n += 1
        return count

class Shirt(Clothing):
    material = "Cotton"
class Pants(Clothing):
    material = "Cotton"

polo = Shirt("Polo")
sweatpants = Pants("Sweatpants")
jeans = Pants("Jeans")
jeans.material = "Cotton Fibres"
polo.add_item(polo.material, 4)
sweatpants.add_item(sweatpants.material, 6)
sweatpants.add_item("Cotton Fibres", 2)
jeans.add_item(jeans.material, 2)
print(sweatpants.Stock_by_Material("Cotton"))
print(sweatpants.Stock_by_Material("Cotton Fibres"))