class Human:
    def __init__(self, name = "noname"):
        self.name = name

class Pole:
    def __init__(self,pol):
        self.pol = pol
        self.footboler = []


    def add_footboler(self, *args):
        for  foot in args:
           self.footboler.append(foot)


    def print_footboler(self):
        if self.footboler != []:
            print(f"Склад команди{self.pol}:")
            for footboler in self.footboler:
                print(footboler.name)
        else:
                print(f"У {self.pol} немає футболістів")


fot1 = Human("==Ronaldo===Benzema===Bale==\n"
             "============================\n"
             "==Modrich============Kross==\n"
             "============================\n"
             "==========Casemiro==========\n"
             "============================\n"
             "==Marcelo=========Carvajal==\n"
             "=======Ramos====Pepe========\n"
             "============================\n"
             "============Navas==========="
             "")
fot2 = Human("===Pedro=====Eto=====Mesii==\n"
             "============================\n"
             "==Xavi===============Kelta==\n"
             "============================\n"
             "==========Busquets==========\n"
             "============================\n"
             "==Abidal=============Alves==\n"
             "=======Pique====Puyol=======\n"
             "============================\n"
             "============Valdes==========")
fot3 = Human("Яник")

pol1 = Pole(": Real Madrid ")
pol2 = Pole(": Barcelona")

pol1.add_footboler(fot1)
pol2.add_footboler(fot2)

pol1.print_footboler()
pol2.print_footboler()