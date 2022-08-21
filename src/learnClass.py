class Dog :

    def __init__(self,dogbreed, dogcolor, dogheight):
        self.breed = dogbreed
        self.color = dogcolor
        self.height = dogheight

tommy = Dog("Pomerian", "Black", "5")
print("Tommy is a", tommy.breed, "and its color is ", tommy.color ,"its height is", tommy.height)

if __name__ == '__main__':
    print("\n\nI start here.\n\n")

