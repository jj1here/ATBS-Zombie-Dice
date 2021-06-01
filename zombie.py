import zombiedice
import random

class halfChance:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        # brains = 0
        # while diceRollResults is not None:
        #     brains += diceRollResults['brains']

        #     if brains < 2:
        #         diceRollResults = zombiedice.roll() # roll again
        #     else:
        #         break
        while diceRollResults and random.randint(0,1) == 0 :
            diceRollResults = zombiedice.roll()
        
class twoBrains:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.
        diceRollResult = zombiedice.roll() # first roll

        brains = 0
        while diceRollResult is not None:
            brains += diceRollResult['brains']
            if brains < 2 :
                diceRollResult = zombiedice.roll()
            else:
                break

class twoShots:
    def __init__(self, name) :
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        shotguns = 0
        while diceRollResults is not None :
            shotguns += diceRollResults['shotgun']
            if shotguns < 2 :
                diceRollResults = zombiedice.roll()
            else :
                break

class oneToFour:
    def __init__(self, name) :
        self.name = name
    def turn(self, gameState):
        
        rolls = random.randint(1,4)
        diceRollResults = zombiedice.roll()
        turn = 1
        shotguns = 0
        while diceRollResults is not None :
            shotguns += diceRollResults['shotgun']
            if turn != rolls or shotguns <2 :
                diceRollResults = zombiedice.roll()
                turn +=1
            else:
                break

class shotsObrains:
    def __init__(self, name) :
        self.name = name
    def turn(self, gameState) :

        diceRollsResults = zombiedice.roll()

        
        while diceRollsResults is not None :
            brains = 0
            shotguns = 0
            brains += diceRollsResults['brains']
            shotguns += diceRollsResults['shotgun']

            if brains >= shotguns :
                diceRollsResults = zombiedice.roll()
            else:
                break


zombies = (
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    halfChance(name='50/50'),
    twoBrains(name='Two Brains'),
    twoShots(name='Two Shotguns'),
    oneToFour(name='One to Four'),
    shotsObrains(name='Shots over Brains')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)