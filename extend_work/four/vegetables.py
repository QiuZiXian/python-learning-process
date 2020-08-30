class Vegetable:
    ID : str
    Calories : float
    Protein : float
    Carbohydrate : float
    Fat : float
    VitaminA : float
    VitaminB1 : float
    VitaminB2 : float
    VitaminC : float

    def __init__(self, ID, Calories,Protein, Carbohydrate ,Fat,VitaminA,VitaminB1,VitaminB2, VitaminC):
        self.ID = ID
        self.Calories = Calories
        self.Protein = Protein
        self.Carbohydrate = Carbohydrate
        self.Fat = Fat
        self.VitaminA = VitaminA
        self.VitaminB1 = VitaminB1
        self.VitaminB2 = VitaminB2
        self.VitaminC = VitaminC

    def __add__(self, other):
        return Vegetable(self.ID,
                self.Calories + other.Calories,
                self.Protein + other.Protein,
                self.Carbohydrate + other.Carbohydrate,
                self.Fat + other.Fat,
                self.VitaminA + other.VitaminA,
                self.VitaminB1 + other.VitaminB1,
                self.VitaminB2 + other.VitaminB2,
                self.VitaminC + other.VitaminC)

    def __str__(self):
        return "\nVegetable ID: " + self.ID + \
               "\n  Calories:" + '{:f}'.format(self.Calories) + " kcal" \
               "\n  Protein:" + '{:f}'.format(self.Protein) + " g" \
               "\n  Carbohydrate:" + '{:f}'.format(self.Carbohydrate) + " g" \
               "\n  Fat:" + '{:f}'.format(self.Fat) + " g"\
               "\n  VitaminA:" + '{:f}'.format(self.VitaminA) + " ug"\
               "\n  VitaminB1:" + '{:f}'.format(self.VitaminB1) + " mg"\
               "\n  VitaminB2:" + '{:f}'.format(self.VitaminB2) + " mg"\
               "\n  VitaminC:" + '{:f}'.format(self.VitaminC)+" mg"

class Root_Vegetable(Vegetable):
    color: str
    mass: float

    def __init__(self, ID, Calories, Protein, Carbohydrate, Fat, VitaminA, VitaminB1, VitaminB2, VitaminC, color,mass):
            super().__init__(ID, Calories, Protein, Carbohydrate, Fat, VitaminA, VitaminB1, VitaminB2, VitaminC)
            self.color = color
            self.mass = mass

class Stalk_Vegetable(Vegetable):
    color: str
    mass: float

    def __init__(self, ID, Calories, Protein, Carbohydrate, Fat, VitaminA, VitaminB1, VitaminB2, VitaminC, color,mass):
        super().__init__(ID, Calories, Protein, Carbohydrate, Fat, VitaminA, VitaminB1, VitaminB2, VitaminC)
        self.color = color
        self.mass = mass

class Leafy_Vegetable(Vegetable):
    color: str
    mass: float

    def __init__(self, ID, Calories, Protein, Carbohydrate, Fat, VitaminA, VitaminB1, VitaminB2, VitaminC, color,mass):
        super().__init__(ID, Calories, Protein, Carbohydrate, Fat, VitaminA, VitaminB1, VitaminB2, VitaminC)
        self.color = color
        self.mass = mass

class Flower_Vegetable(Vegetable):
    color: str
    mass: float

    def __init__(self, ID, Calories, Protein, Carbohydrate, Fat, VitaminA, VitaminB1, VitaminB2, VitaminC, color,mass):
        super().__init__(ID, Calories, Protein, Carbohydrate, Fat, VitaminA, VitaminB1, VitaminB2, VitaminC)
        self.color = color
        self.mass = mass

class Fruit_Vegetable(Vegetable):
    color: str
    mass: float

    def __init__(self, ID, Calories, Protein, Carbohydrate, Fat, VitaminA, VitaminB1, VitaminB2, VitaminC, color,mass):
        super().__init__(ID, Calories, Protein, Carbohydrate, Fat, VitaminA, VitaminB1, VitaminB2, VitaminC)
        self.color = color
        self.mass = mass

if __name__ == "__main__":
  Vegetables = []
  Vegetables.append(Root_Vegetable("Radish", 21, 0.9, 5, 0.1, 3, 0.02, 0.03, 21, "white", 100))
  Vegetables.append(Stalk_Vegetable("Potato", 76, 2, 17.2, 0.2, 5, 0.08, 0.04, 27, "yellow", 100))
  Vegetables.append(Leafy_Vegetable("Spinach", 24, 0.6, 4.5, 0.3, 487, 0.04, 0.11, 32, "green", 100))
  Vegetables.append(Flower_Vegetable("Hemerocallis citrina", 38, 2.5, 6.8, 0.9, 357, 0, 0, 62, "green", 100))
  Vegetables.append(Fruit_Vegetable("Eggplant", 23, 1.1, 4.9, 0.2, 8, 0.02, 0.04, 5, "purple", 100))
  Total = Vegetable("Total", 0, 0, 0, 0, 0, 0, 0, 0)
  for E in Vegetables:
    assert isinstance(Total, object)
    Total += E
    print(str(E))

  print("\n" + Total.ID, ': ', Total.Calories, " kcal")
  print(Total)