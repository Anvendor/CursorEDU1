#parent class
class Animals:
    def eat(self):
        print("The animal is eating.")

    def sleep(self):
        print("The animal is sleeping.")

#subclass 1
class Dog(Animals):
    def bark(self):
        print("The dog is barking.")

    def fetch(self):
        print("The dog is fetching.")

#subclass 2
class Cat(Animals):
    def purr(self):
        print("The cat is purring.")

    def scratch(self):
        print("The cat is scratching.")

#subclass 3
class Bird(Animals):
    def chirp(self):
        print("The bird is chirping.")

    def fly(self):
        print("The bird is flying.")

#subclass 4
class Fish(Animals):
    def swimm(self):
        print("The fish is swimming.")

    def breathe_underwater(self):
        print("The fish is breathing underwater.")
#calling different function
dog = Dog()
dog.bark()
dog.eat()

cat = Cat()
cat.scratch()
cat.sleep()

bird = Bird()
bird.chirp()
bird.eat()

fish = Fish()
fish.swimm()
fish.sleep()


#direct instance check
if isinstance(dog,Animals) == True:
    print("Dog is an animal.")
if isinstance(cat,Animals) == True:
    print("Cat is an animal.")
if isinstance(bird, Animals) == True:
    print("Bird is an animal.")
if isinstance(fish, Animals) == True:
    print("Fish is an animal.")

#try to check instance by loop
Animals_list = [dog, cat, bird, fish ]

for i in Animals_list:

    if isinstance(i,Animals) == True:
        print(f"{Animals_list.index(i)+1}){i} is an animal.")
    else:
        print(f"Seems like {i} is NOT an animal")




#1.a

#second parent class
class Human:
    def eat(self):
        print("Eating...")
    def sleep(self):
        print("Sleeping...")
    def study(self):
        print("Studing...")
    def work(self):
        print("Working...")
#subclass
class Centaur(Human,Animals):
    def trotting(self):
        print("Trotting...")
    def walk(self):
        print("Walking...")

cent = Centaur()
cent.work()
cent.eat()
cent.sleep()
cent.trotting()