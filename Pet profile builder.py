class pe_pr :
    def __init__(self,name,high,weight,colour,breed,age):
        self.name = name
        self.high = high
        self.weight = weight
        self.colour = colour
        self.breed = breed
        self.age = age
p1 = pe_pr("Tommy","2.3 Feet","34 Kg","Black,White","Dalmatine,DOG",14)
p2 = pe_pr("Garfield","3 Feet","45 Kg","Orange,Brown","Ginger,CAT",23)
p3 = pe_pr("King Kong","6.9 Feet","50 Kg","Black,Grey","Gorilla",24)
print("\n======== Profile Of {} =========".format(p1.name))
print("Name of pet : {}".format(p1.name))
print("Age of pet : {}".format(p1.age))
print("Height of pet : {}".format(p1.high))
print("Weight of pet : {}".format(p1.weight))
print("Colour of pet : {}".format(p1.colour))
print("Breed of pet : {}".format(p1.breed))
print("==================================")
print("\n======== Profile Of {} =========".format(p2.name))
print("Name of pet : {}".format(p2.name))
print("Age of pet : {}".format(p2.age))
print("Height of pet : {}".format(p2.high))
print("Weight of pet : {}".format(p2.weight))
print("Colour of pet : {}".format(p2.colour))
print("Breed of pet : {}".format(p2.breed))
print("==================================")
print("\n======== Profile Of {} =========".format(p3.name))
print("Name of pet : {}".format(p3.name))
print("Age of pet : {}".format(p3.age))
print("Height of pet : {}".format(p3.high))
print("Weight of pet : {}".format(p3.weight))
print("Colour of pet : {}".format(p3.colour))
print("Breed of pet : {}".format(p3.breed))
print("==================================\n")
