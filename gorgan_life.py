class Critter(object):
    """ZooKeeper"""
    total = 0
    
    def __init__(self, name, boredom = 2, hunger = 0 ):
        self.name = name
        self.boredom = boredom
        self.hunger = hunger
        print(self.name)
        Critter.total += 1
                
    def __str__(self):
        rep = "Name of gorgan is ...  "
        rep += self.name + "\n"
        return rep
    
    @staticmethod
    def status():
        print(Critter.total)
       
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
        
    def talk(self):
        print("Hi. My name is ", self.name, ". I feel ", self.mood)
        self.__pass_time()
        
    @property
    def mood(self):
        unhappines = self.boredom + self.hunger
        if unhappines < 5:
            m1 = "preety"
        elif 5<= unhappines < 10:
            m1 = "good"
        elif 10<= unhappines < 20:
            m1 = "normal" 
        elif 20<= unhappines <= 30:
            m1 = "some bad"
        elif unhappines > 30:
            m1 = "i hate you !"
        return m1
    
    def eat(self):
        food = int(input("how mutch meel ? "))
        print("Nam-Nam")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        happy = int(input(" how mutch hours  ? "))
        print(" GO Bitch ")
        self.boredom -= happy
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    name = input("Enter name of 1 gorgan  ")

    crit = Critter(name)

    Critter.status()
    choice = None
    while choice != "0":
        print(
            """
    My monster
    0 - Escape
    1 - How are you
    2 - EAT !
    3 - PlaY!
    4 - secret (inside)
    """)
        choice = input("Your choice: ")
        
        
        if choice == "0":
            print("Goodbuy.")

        elif choice == "1":
            crit.talk()

        elif choice == "2":
            crit.eat()

        elif choice == "3":
            crit.play()

        elif choice == "4":
            print(crit.name, crit.hunger,  crit.boredom)
        else:
            print( "sorry but... ", choice)
main()
input(" ")
    
