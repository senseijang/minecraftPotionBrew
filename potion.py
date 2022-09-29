"""
Minecraft Potion Maker
with text-based IO
Andy Jang
"""
"""
Potion documentation:
Every potion will be under their own class for example:
    - potion, splash potion, and lingering potions will be classes.
    - splash and lingering will be a subclass of potion
potions are stored in an array [0, 0, 0] where:
    1. the first ingredient at index 0 is the ingredient that changes the behavior of the potion
        - ingredients on 1st step are: sugar, rabbit's foot, blaze powder, glittering melon, spider eye, ghast tear, magma cream, pufferfish, golden carrot, turtle shell, phantom membrane
    2. the second ingredient at index 1 is the ingredient that changes the magnitude of the potion (glowstone, redstone)
    3. if a fermented spider eye can be added, this will be the exception slot (only 3 potions are the outcome with a spider eye)
        - slowness, harming, invisibility

    things to add:
        -exclusivity of ingredients based off of phase
        -getting the effects of the potion depending on ingredients
"""

"""
Ingredients holds a unique value for each ingredient in order to evaluate what ingredients went into the potion.
So instead of comparing "sugar" in the storage, numbers can be used.
inv_ingredients is the inverse of the ingredient dictionary, the keys and values are flipped in order to get the name of the key by referencing the value.
"""
ingredients = {
    "nothing" : 0,
    "sugar" : 1,
    "rabbit's foot" : 2,
    "blaze powder" : 3,
    "glittering melon" : 4,
    "spider eye": 5,
    "ghast tear" : 6,
    "magma cream" : 7,
    "pufferfish" : 8,
    "golden carrot" : 9,
    "turtle shell" : 10,
    "phantom membrane" : 11,
    "glowstone" : 12,
    "redstone" : 13,
    "fermented spider's eye" : 14
    }

inv_ingredients = {value: key for key, value in ingredients.items()}

"""
__init__:
    phase = location of the ingredient being changed
    storage = the way to store the value of the potion in order to get the effect
    fingredient = first ingredient that makes the potion work. will either be nether wart, gunpowder, or gunpowder + dragon's breath
        *sort of a shortcut method, yes I know.*

get_ingredient:
    gets the ingredient at the current phase

set_ingredient:
    changes the ingredient at the specified location

next_phase:
    changes the phase/location of the ingredient being changed

get_all_ingredients:
    takes all of the ingredients in the storage and adds the names of the keys into a list and returns the list

get_effect:
    references the effects dictionary in order to get the effect of the potion dependent on the storage of the potion.

property(ingredient):
    honestly a lazy way of getting the ingredient at the location and to set lazily too.
"""
class Potion:
    def __init__(self, storage = [0, 0], fingredient = 'nether wart'):
        self.__phase = 0
        self.__storage = storage
        self.__fingredient = fingredient

    def get_ingredients(self):
        for item in ingredients:
            if self.__storage[self.__phase] == ingredients[item]:
                return inv_ingredients[ingredients[item]]

    def set_ingredient(self, item_name = ""):
        try:
            item_name = item_name.lower()
            self.__storage[self.__phase] = ingredients[item_name]
        except KeyError:
            print("That ingredient is not avaliable please try again. ")
        except:
            print("Something has gone wrong with the setter please try again. ")

    def next_phase(self):
        self.__phase += 1

    def get_all_ingredients(self):
        former_phase = self.__phase
        item_list = [self.__fingredient]
        for i in range(len(self.__storage)):
            self.__phase = i
            item_list.append(self.ingredient)
        self.__phase = former_phase
        return item_list
    
    def get_effect(self):
        effects = {
            "swiftness" : [1, 0],
            "swiftness 2" : [1, 12],
            "swiftness+" : [1, 13],
            "leaping" : [2, 0],
            "leaping 2" : [2, 12],
            "leaping+" : [2, 13],
            "strength" : [3, 0],
            "strength 2" : [3, 12],
            "strength+" : [3, 13],
            "healing" : [4, 0],
            "healing 2" : [4, 12],
            "poison" : [5, 0],
            "poison 2" : [5, 12],
            "poison+" : [5, 13],
            "regeneration" : [6, 0],
            "regeneration 2" : [6, 12],
            "regeneration+" : [6, 13],
            "fire resistance" : [7, 0],
            "fire resistance+" : [7, 13],
            "water breathing" : [8, 0],
            "water breathing+" : [8, 13],
            "night vision" : [9, 0],
            "night vision+" : [9, 13],
            "turtle master" : [10, 0],
            "turtle master 2" : [10, 12],
            "turtle master+" : [10, 13],
            "slow falling" : [11, 0],
            "slow falling+" : [11, 13],
            "weakness" : [14, 0],
            "weakness+" : [14, 13]
        }
        if self.__storage in effects.values():
            effects = list(effects.keys())[list(effects.values()).index(self.__storage)]
            print(f"Potion of {effects}\n")
            return effects

    ingredient = property(fget = get_ingredients, fset = set_ingredient)

user_potion = Potion([0, 0])


def addIngredient():
    for item in ingredients.keys():
        print(item)
    user_input = input("What item would you like to add? ")
    user_potion.set_ingredient(user_input)

def removeIngredient():
    user_potion.set_ingredient("nothing")

def check_input(user_input):
    global user_potion
    try:
        user_input = int(user_input)
    except:
        print("That was not a valid input please try again. ")
    
    if user_input == 1:
        user_potion = Potion([1, 0])
    elif user_input == 2:
        addIngredient()
    elif user_input == 3:
        removeIngredient()
    elif user_input == 4:
        print(f"Potion ingredients: {user_potion.get_all_ingredients()}")
    elif user_input == 5:
        user_potion.next_phase()
    elif user_input == 6:
        user_potion.get_effect()
    elif user_input == 0:
        quit()
    else:
        print("Something went wrong, try again ")

def main():
    isGoing = True
    while isGoing:
        print("MINECRAFT POTION MAKER")
        print("1. Make new potion ")
        print("2. Add an ingredient ")
        print("3. Remove an ingredient ")
        print("4. Show all ingredients ")
        print("5. Go to next phase")
        print("6. Get effect of the potion")
        print("0. exit ")
        user_input = input("What would you like to do? ")
        check_input(user_input)


if __name__ == "__main__":
    main()