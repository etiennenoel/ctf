# Your AI for CTF must inherit from the base Commander class.  See how this is
# implemented by looking at the commander.py in the ./api/ folder.
from api import Commander

# The commander can send 'Commands' to individual bots.  These are listed and
# documented in commands.py from the ./api/ folder also.
from api import commands

# The maps for CTF are layed out along the X and Z axis in space, but can be
# effectively be considered 2D.
from api import Vector2

class PlaceholderCommander(Commander):
    """
    Rename and modify this class to create your own commander and add mycmd.Placeholder
    to the execution command you use to run the competition.
    """

    ##################################################################################
    ## Function   : initialize
    ## Description: Methode pour initialiser le commander 
    ## Parametres : self
    ##################################################################################    
    def initialize(self):
        """Use this function to setup your bot before the game starts."""
        self.verbose = True    # display the command descriptions next to the bot labels
        
        #Liste de buts
        self.BotGoal = [GoalKillAnyone(self.game), GoalKillSpecificDefender(self.game), GoalKillFlagCarrier(self.game), GoalGetEnemyFlag(self.game)]

        #Cherche les bonnes cases pour camper
        self.hidingSpot = []
        self.findHidingSpot()
                
    ##################################################################################
    ## Function   : findHidingSpot
    ## Description: Methode permettant de trouver les cachettes afin de pouvoir camper 
    ## Parametres : self
    ##################################################################################          
    def findHidingSpot(self):
        x = 0
        # Pour toutes les cases, on regarde s'il y a deux bloques adjacents
        for column in self.level.blockHeights:
            # Doit reinitialiser le y a chaque nouvelle ligne
            y=0
            for blockHeight in column:
                # On s'assure que la case courante n'est pas bloquer
                if blockHeight == 0:
                    # Variable contenant le nombre de mur pour une case donnee
                    numberOfAdjacentWall = 0
                
                    # On verifie si on est a coter d'un mur (extremiter de la map)
                    if x-1 < 0:
                        numberOfAdjacentWall +=1
                    
                    if x+1 > self.level.width:
                        numberOfAdjacentWall +=1
                    
                    if y-1 < 0:
                        numberOfAdjacentWall +=1
                    
                    if y+1 > self.level.height:
                        numberOfAdjacentWall +=1
                
                    # On verifie si on est a coter d'un bloque
                    if x-1>0 and x+1< self.level.width and y-1>0 and y+1< self.level.height:
                        #North
                        if self.level.blockHeights[x][y-1] > 1:
                            numberOfAdjacentWall +=1
                            #self.log.info(str(self.level.blockHeights[x][y-1])+" " + str(x) + " " + str(y) + "north")
                
                        #East
                        if self.level.blockHeights[x+1][y] > 1:
                            numberOfAdjacentWall +=1
                            #self.log.info(str(self.level.blockHeights[x+1][y])+" " + str(x) + " " + str(y)+ "east")

                        #South
                        if self.level.blockHeights[x][y+1] > 1:
                            numberOfAdjacentWall +=1
                            #self.log.info(str(self.level.blockHeights[x][y+1])+" " + str(x) + " " + str(y)+ "south")

                        #West
                        if self.level.blockHeights[x-1][y] > 1:
                            numberOfAdjacentWall +=1
                            #self.log.info(str(self.level.blockHeights[x-1][y])+" " + str(x) + " " + str(y)+ "West")
                
                    # On considere que c'est une bonne cachette s'il y a au moins deux murs
                    if numberOfAdjacentWall > 1:
                        self.hidingSpot.append((y,x))
                        self.log.info((x,y))
                
                # On veut la position de la prochaine case en x
                y += 1

            # On veut la prochaine ligne
            x+=1
                
                

    def tick(self):
        """Override this function for your own bots.  Here you can access all the information in self.game,
        which includes game information, and self.level which includes information about the level."""

        # for all bots which aren't currently doing anything
        for bot in self.game.bots_available:
            if bot.flag:
                # if a bot has the flag run to the scoring location
                flagScoreLocation = self.game.team.flagScoreLocation
                self.issue(commands.Charge, bot, flagScoreLocation, description = 'Run to my flag')
            else:
                # otherwise run to where the flag is
                enemyFlag = self.game.enemyTeam.flag.position

                # calcule l'utilite maximale
                maxUtility = -1
                doGoal = Goal(self.game)
                for goal in self.BotGoal:
                    utility = goal.calculateUtility
                    if maxUtility < goal.calculateUtility():
                        maxUtility = utility
                        doGoal = goal

                self.issue(commands.Charge, bot, enemyFlag, description = 'Run to enemy flag')

    def shutdown(self):
        """Use this function to teardown your bot after the game is over, or perform an
        analysis of the data accumulated during the game."""

        pass

##################################################################################
## Class   : Goal
## Description: Classe abstraite representant les buts
##################################################################################   
class Goal:
    ##################################################################################
    ## Function   : initialize
    ## Description: Methode pour initialiser le but 
    ## Parametres : self
    ##              gameInfo: informations sur la partie
    ##################################################################################    
    def __init__(self, gameInfo):
        self.gameInfo = gameInfo

    ##################################################################################
    ## Function   : calculteUtility
    ## Description: Methode permettant de calculer l'utilite du but
    ## Parametres : self
    ##################################################################################   
    def calculateUtility(self):
        abstract

##################################################################################
## Class   : GoalKillAnyone
## Description: Classe representant le but: Tuer un mechant - Un ennemi arbitraire
##################################################################################   
class GoalKillAnyone (Goal):
    ##################################################################################
    ## Function   : initialize
    ## Description: Methode pour initialiser le but 
    ## Parametres : self
    ##              gameInfo: informations sur la partie
    ##################################################################################
    def __init__(self, gameInfo):
        Goal.__init__(self, gameInfo)

    ##################################################################################
    ## Function   : calculteUtility
    ## Description: Methode permettant de calculer l'utilite du but de tuer le flag carrier
    ## Parametres : self
    ##################################################################################   
    def calculateUtility(self):
        return 0

##################################################################################
## Class   : GoalKillSpecificDefender
## Description: Classe representant le but: Tuer un mechant - Un defenseur renomme
##################################################################################   
class GoalKillSpecificDefender (Goal):
    ##################################################################################
    ## Function   : initialize
    ## Description: Methode pour initialiser le but 
    ## Parametres : self
    ##              gameInfo: informations sur la partie
    ##################################################################################
    def __init__(self, gameInfo):
        Goal.__init__(self, gameInfo)

    ##################################################################################
    ## Function   : calculteUtility
    ## Description: Methode permettant de calculer l'utilite du but de tuer un defenseur precis
    ## Parametres : self
    ##################################################################################   
    def calculateUtility(self):
        return 0

##################################################################################
## Class   : GoalKillFlagCarrier
## Description: Classe representant le but: Tuer un mechant - Leur flag carrier
##################################################################################   
class GoalKillFlagCarrier (Goal):
    ##################################################################################
    ## Function   : initialize
    ## Description: Methode pour initialiser le but 
    ## Parametres : self
    ##              gameInfo: informations sur la partie
    ##################################################################################
    def __init__(self, gameInfo):
        Goal.__init__(self, gameInfo)

    ##################################################################################
    ## Function   : calculteUtility
    ## Description: Methode permettant de calculer l'utilite du but de tuer le flag carrier
    ## Parametres : self
    ##################################################################################   
    def calculateUtility(self):
        return 0

##################################################################################
## Class   : GoalGetEnemyFlag
## Description: Classe representant le but: Aller chercher leur flag
##################################################################################   
class GoalGetEnemyFlag (Goal):
    ##################################################################################
    ## Function   : initialize
    ## Description: Methode pour initialiser le but 
    ## Parametres : self
    ##              gameInfo: informations sur la partie
    ##################################################################################
    def __init__(self, gameInfo):
        Goal.__init__(self, gameInfo)

    ##################################################################################
    ## Function   : calculteUtility
    ## Description: Methode permettant de calculer l'utilite du but d'aller chercher leur flag
    ## Parametres : self
    ##################################################################################   
    def calculateUtility(self):
        return 1