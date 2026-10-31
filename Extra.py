try :
    class pe_pr :
        def __init__(self,name,high,weight,colour,breed,age,catagory):
            self.name = name
            self.high = high
            self.weight = weight
            self.colour = colour
            self.breed = breed
            self.age = age
            self.catagory = catagory

    num = int(input("Enter number of customers : "))
    i = 0
    co_se = 0
    while i <= 999:
        na = input("Enter name of pet: ")
        ag = input(f"Enter age of {na}: ")
        hi = input(f"Enter height of {na} in feet: ")
        we = input(f"Enter weight of {na} in Kg: ")
        co = input(f"Enter colour of {na}: ")
        br = input(f"Enter breed of {na}: ")
        ca = input(f"Enter catagory of {na} (like cat or dog): ")
        p1 = pe_pr(na,hi,we,co,br,ag,ca)
        print("\n======== Profile Of {} =========".format(p1.name))
        print(f"Name of pet : {p1.name}")
        print(f"Age of {na} : {p1.age}")
        print(f"Height of {na} : {p1.high}")
        print(f"Weight of {na} : {p1.weight}")
        print(f"Colour of {na} : {p1.colour}")
        print(f"Breed of {na} : {p1.breed}")
        print(f"Catagory of {na} : {p1.catagory}")
        print("==================================")
        co_se = co_se + 1
        i = i + 1
    print("Number of profiles created = ",co_se)
except ValueError:
    print("Value should be in numbers!")
    