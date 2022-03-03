class Roles:
    def __init__(self):
        
        
        self.warrior_class=["Solider","Knight","Hunter","Thief","Monk","Dragnor","Beserker","Gunner","Hero"]
        self.solider={"descrpt":"basic Warrior type you start off as"}
        self.knight={"descrpt":"a Solider great offence and defence"}
        self.warriorClasses={"solider":self.solider,
                             "knight":self.knight}
        self.magi={"descrpt":"can use basic to high class elemental magics"}
        self.sage={"descrpt":"can use all forms of magic as well as the infinate magic as an extention"}
        self.mage_class=["Magicain","Sorcorer","Paladen","Psion","Sage"]
        self.mageClasses={"magi":self.magi,
                          "sage":self.sage}
        
        self.support_class=["Tamer","Priest","Shaman","Smith","Alchemist","Bard","Analyist"]
        self.tamer={"descrpt":"can form bonds with animals and use powers related to thems"}
        self.bard={"descrpt":"effect the effectiveness of partys and enermies in battle through music"}
        self.supportClasses={"tamer":self.tamer,
                             "bard":self.bard}
        
        #print(self.warriorClasses["knight"]["descrpt"])
    def Select(self):
        print("Which one of these roles is suible for you?")
        role_classes=["Warrior","Mage","Supporter"]
        print(role_classes)
        role_class=input("type role type here:  ")
        if role_class[0]=="w" or role_class[0]=="W":
            print("You picked Warrior class")
            print("Which job would you like?")
            print(self.warrior_class)
            Roles().warrior_roles()
            
        elif role_class[0]=="m" or role_class[0]=="M":
            print("You picked Mage class")
            print("Which job would you like?")
            print(self.mage_class)
            Roles().mage_roles()
            
        elif role_class[0]=="s" or role_class[0]=="S":
            print("You picked Supporter class")
            print("Which job would you like?")
            print(self.support_class)
            Roles().support_roles()

    def warrior_roles(self):
        self.wSelect=input("Select Warrior type:     ")
        #self.warriorClasses={"solider":self.solider,"knight":self.knight}
        
        #self.solider={"descrpt":"basic Warrior type you start off as"}
        #self.knight={"descrpt":"a Solider great offence and defence"}
        print(self.warriorClasses[self.wSelect]["descrpt"])
    
    def mage_roles(self):
        self.wSelect=input("Select Mage type:         ")
        #self.warriorClasses={"solider":self.solider,"knight":self.knight}
        
        #self.solider={"descrpt":"basic Warrior type you start off as"}
        #self.knight={"descrpt":"a Solider great offence and defence"}
        print(self.mageClasses[self.wSelect]["descrpt"])
    
    def support_roles(self):
        self.wSelect=input("Select Support type:     ")
        #self.warriorClasses={"solider":self.solider,"knight":self.knight}
        
        #self.solider={"descrpt":"basic Warrior type you start off as"}
        #self.knight={"descrpt":"a Solider great offence and defence"}
        print(self.supportClasses[self.wSelect]["descrpt"])
        
        

        
        
test =Roles()
test.Select()

        