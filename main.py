from tkinter import *
from PIL import Image, ImageTk
from potion import Potion, ingredients

MYFONT = "Cursive 15"
BGCOLOR = "blue"

class App(Tk):
    def __init__(self):
        self.potion = Potion()

        Tk.__init__(self)
        self.titletext = Label(self, text = "Minecraft Potion Maker", font = "Impact 25")
        self.titletext.grid(row = 1, column = 1)

        self.inputlabel = Label(self, text = "Enter ingredient here: ", font = MYFONT)
        self.inputlabel.grid(column = 1)
        self.entry = Entry(self, font = MYFONT)
        self.entry.grid(column = 1)

        self.submit = Button(self, text = "submit", command = lambda: [self.potion.set_ingredient(self.entry.get()), self.update_bottle(self.potion), self.phase_one(True)])
        self.submit.grid(column = 1)

    
    def update_bottle(self, potion, is_first_time = False):
        path = ""
        pictures = {
            "swiftness" : "PotionOfSwiftnessNew.png",
            "swiftness 2" : "PotionOfSwiftnessNew.png",
            "swiftness+" : "PotionOfSwiftnessNew.png",
            "leaping" : "PotionOfLeapingNew.png",
            "leaping 2" : "PotionOfLeapingNew.png",
            "leaping+" : "PotionOfLeapingNew.png",
            "strength" : "PotionOfStrengthNew.png",
            "strength 2" : "PotionOfStrengthNew.png",
            "strength+" : "PotionOfStrengthNew.png",
            "healing" : "PotionOfHealing.png",
            "healing 2" : "PotionOfHealing.png",
            "poison" : "PotionOfPoisonNew.png",
            "poison 2" : "PotionOfPoisonNew.png",
            "poison+" : "PotionOfPoisonNew.png",
            "regeneration" : "PotionOfRegnerationNew.png",
            "regeneration 2" : "PotionOfRegnerationNew.png",
            "regeneration+" : "PotionOfRegnerationNew.png",
            "fire resistance" : "PotionOfFireResistanceNew.png",
            "fire resistance+" : "PotionOfFireResistanceNew.png",
            "water breathing" : "PotionOfWaterBreathingNew.png",
            "water breathing+" : "PotionOfWaterBreathingNew.png",
            "night vision" : "PotionOfNightVisionNew.png",
            "night vision+" : "PotionOfNightVisionNew.png",
            "turtle master" : "PotionOfTurtleMasterNew.png",
            "turtle master 2" : "PotionOfTurtleMasterNew.png",
            "turtle master+" : "PotionOfTurtleMasterNew.png",
            "slow falling" : "PotionOfSlowFallingNew.png",
            "slow falling+" : "PotionOfSlowFallingNew.png",
            "weakness" : "PotionOfWeaknessNew.png",
            "weakness+" : "PotionOfWeaknessNew.png"
        }
        potion_name = potion.get_effect()
        for key in pictures.keys():
            if potion_name == key:
                path = ".\static" + "\\" + pictures[key]
                print(path)
            else:
                path = ".\static\Potion_blue.png"


        self.bottle = Image.open(path)
        self.tkpic = ImageTk.PhotoImage(self.bottle)
        if is_first_time:
            self.label = Label(self, image = self.tkpic)
            self.label.grid(column = 1)
        else:
            self.label["image"] = self.tkpic
            self.label.image = self.tkpic
        

    def phase_one(self, delete = False):
        for count, name in enumerate(ingredients.keys()):
            if count > 0 and count <= 11 and not delete:
                self.label = Label(self, text = name, font = MYFONT)
                self.label.grid(column = 1)
            else:
                self.label["text"] = ""

    def modifier(self):
        for name in ingredients.keys():
            if name == "redstone" or name == "glowstone":
                self.button = Label(self, text = name, font = MYFONT)
                self.button.grid(column = 1)



def main():
    app = App()

    app.update_bottle(app.potion, True)
    app.phase_one()
    
    app.mainloop()

main()






