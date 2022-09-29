from bottle import default_app, route, template, post
@route('/')
def menu():
    return template('menu.html')

"""
BMI Project + BB
"""
@route('/bmi')
def get_bmi_info():
    return template('form.html')

@post('/get_bmi')
def get_bmi():
    return template('result.html')

@route('/bmr')
def get_bmr_info():
    return template('bmrform.html')

@post('/get_bmr')
def get_bmr():
    return template('bmrresult.html')

"""
Final Project
"""

# needed to reference recipe to individual ingredients
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


# used ingredients to form each effect, at the end the potion's recipe is compared to the values to get the effect.
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

# stores the location of every picture based on the effect of the potion
# discord was used as an image server because other websites would not allow direct access
pictures = {
    "default" : "https://cdn.discordapp.com/attachments/917819620981882922/917819963765579796/Potion_blue.png",
    "swiftness" : "https://cdn.discordapp.com/attachments/856769615266840578/917819335211368518/PotionOfSwiftnessNew.png",
    "swiftness 2" : "https://cdn.discordapp.com/attachments/856769615266840578/917819335211368518/PotionOfSwiftnessNew.png",
    "swiftness+" : "https://cdn.discordapp.com/attachments/856769615266840578/917819335211368518/PotionOfSwiftnessNew.png",
    "leaping" : "https://cdn.discordapp.com/attachments/917819620981882922/917820071102021712/PotionOfLeapingNew.png",
    "leaping 2" : "https://cdn.discordapp.com/attachments/917819620981882922/917820071102021712/PotionOfLeapingNew.png",
    "leaping+" : "https://cdn.discordapp.com/attachments/917819620981882922/917820071102021712/PotionOfLeapingNew.png",
    "strength" : "https://cdn.discordapp.com/attachments/917819620981882922/917820219945259058/PotionOfStrengthNew.png",
    "strength 2" : "https://cdn.discordapp.com/attachments/917819620981882922/917820219945259058/PotionOfStrengthNew.png",
    "strength+" : "https://cdn.discordapp.com/attachments/917819620981882922/917820219945259058/PotionOfStrengthNew.png",
    "healing" : "https://cdn.discordapp.com/attachments/917819620981882922/917820031100923914/PotionOfHealing.png",
    "healing 2" : "https://cdn.discordapp.com/attachments/917819620981882922/917820031100923914/PotionOfHealing.png",
    "poison" : "https://cdn.discordapp.com/attachments/917819620981882922/917820113623859210/PotionOfPoisonNew.png",
    "poison 2" : "https://cdn.discordapp.com/attachments/917819620981882922/917820113623859210/PotionOfPoisonNew.png",
    "poison+" : "https://cdn.discordapp.com/attachments/917819620981882922/917820113623859210/PotionOfPoisonNew.png",
    "regeneration" : "https://cdn.discordapp.com/attachments/917819620981882922/917820138311544902/PotionOfRegenerationNew.png",
    "regeneration 2" : "https://cdn.discordapp.com/attachments/917819620981882922/917820138311544902/PotionOfRegenerationNew.png",
    "regeneration+" : "https://cdn.discordapp.com/attachments/917819620981882922/917820138311544902/PotionOfRegenerationNew.png",
    "fire resistance" : "https://cdn.discordapp.com/attachments/917819620981882922/917819985085235331/PotionOfFireResistanceNew.png",
    "fire resistance+" : "https://cdn.discordapp.com/attachments/917819620981882922/917819985085235331/PotionOfFireResistanceNew.png",
    "water breathing" : "https://cdn.discordapp.com/attachments/917819620981882922/917820308029849631/PotionOfWaterBreathingNew.png",
    "water breathing+" : "https://cdn.discordapp.com/attachments/917819620981882922/917820308029849631/PotionOfWaterBreathingNew.png",
    "night vision" : "https://cdn.discordapp.com/attachments/917819620981882922/917820090932678657/PotionOfNightVisionNew.png",
    "night vision+" : "https://cdn.discordapp.com/attachments/917819620981882922/917820090932678657/PotionOfNightVisionNew.png",
    "turtle master" : "https://cdn.discordapp.com/attachments/917819620981882922/917820269530345533/PotionOfTurtleMasterNew.png",
    "turtle master 2" : "https://cdn.discordapp.com/attachments/917819620981882922/917820269530345533/PotionOfTurtleMasterNew.png",
    "turtle master+" : "https://cdn.discordapp.com/attachments/917819620981882922/917820269530345533/PotionOfTurtleMasterNew.png",
    "slow falling" : "https://cdn.discordapp.com/attachments/917819620981882922/917820169072570428/PotionOfSlowFallingNew.png",
    "slow falling+" : "https://cdn.discordapp.com/attachments/917819620981882922/917820169072570428/PotionOfSlowFallingNew.png",
    "weakness" : "https://cdn.discordapp.com/attachments/917819620981882922/917820336043618324/PotionOfWeaknessNew.png",
    "weakness+" : "https://cdn.discordapp.com/attachments/917819620981882922/917820336043618324/PotionOfWeaknessNew.png"
    }

@route('/brew')
def phase_one():
    return template('brew_p1.html', ingredients = ingredients)

@post('/brewB')
def phase_two():
    return template('brew_p2.html', ingredients = ingredients)

@post('/brewResults')
def brew_results():
    return template('brew_done.html', effects = effects, ingredients = ingredients, pictures = pictures)

application = default_app()

