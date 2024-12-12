class parrot :
    species = "Bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age 

blu = parrot("Blu" , 18)
woo = parrot("Woo", 15)

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print("Blu is {} years old".format(blu.age))
print("Woo is {} years old".format(woo.age))


