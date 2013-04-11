# Your AI for CTF must inherit from the base Commander class.  See how this is
# implemented by looking at the commander.py in the ./api/ folder.
from api import Commander

# The commander can send 'Commands' to individual bots.  These are listed and
# documented in commands.py from the ./api/ folder also.
from api import commands

# The maps for CTF are layed out along the X and Z axis in space, but can be
# effectively be considered 2D.
from api import Vector2

from goals.GoalPlanner import GoalPlanner
from goals.Goal import Goal

import math
from plans.PlanPlanner import PlanPlanner
from Blackboard import Blackboard

class ReploidCommander(Commander):
    """
    Rename and modify this class to create your own commander and add mycmd.Placeholder
    to the execution command you use to run the competition.
    """
   
    def initialize(self):
        """Use this function to setup your bot before the game starts."""
        self.verbose = True    # display the command descriptions next to the bot labels
        
        #Planner
        self.goalPlanner = GoalPlanner(self.game)
        self.planPlanner = PlanPlanner(self.game)

        #Dictionnaire liant un bot a son plan
        self.botsPlan = {}

        #Cherche les bonnes cases pour camper
        self.hidingLocations = []
        self.findHidingSpot()

        #Blackboard
        self.blackboard = Blackboard(self.hidingLocations, self.level, self)
        self.blackboard.numberOfDefender = math.floor(len(self.game.bots)/2 * 0.4)

        #Le jeu commence deja avec des events (le 2 c'est les flag qui spawn)
        self.lastEventCount = len(self.game.bots) + 2
                                  
    def findHidingSpot(self):
        """Methode permettant de trouver les cachettes afin de pouvoir camper """
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
                        square = HidingSquare(Vector2(x,y))
                        self.hidingLocations.append(square)
                
                # On veut la position de la prochaine case en x
                y += 1

            # On veut la prochaine ligne
            x+=1

    def tick(self):
        """Override this function for your own bots.  Here you can access all the information in self.game,
        which includes game information, and self.level which includes information about the level."""

        # Regarde s'il y a eu un fait marquant
        hasToUpdate = False
        if len(self.game.match.combatEvents) > self.lastEventCount:
            lastEvent = self.game.match.combatEvents[-1]
            if lastEvent.subject == self.game.team.flag or lastEvent.subject == self.game.enemyTeam.flag:
                print 'evenement marquant'
                hasToUpdate = True

            self.lastEventCount = len(self.game.match.combatEvents)


        for bot in self.game.team.members:
            # Plan a executer
            plan = ""

            # Regarde si le bot est disponible
            isAvailable = bot.health > 0 and bot.state == bot.STATE_IDLE
            
            # Clear les variables si le bot est mort
            if bot.state == bot.STATE_DEAD:
                if self.blackboard.botsAssignGoal[bot.name] == 'ProtectFlag':
                    self.blackboard.actualDefender -= 1

                # clear blackboard
                self.blackboard.botsAssignGoal[bot] = "Unknown"

            elif isAvailable or hasToUpdate:
                # S'il y a eu un evenement marquant alors le bot doit updater son but meme s'il est occuper
                
                # Bot n'a pas de plan
                if (not self.botsPlan.__contains__(bot)) or (not self.botsPlan[bot].isPlanValid()) or hasToUpdate:

                    if self.blackboard.botsAssignGoal.__contains__(bot.name) and self.blackboard.botsAssignGoal[bot.name] == 'ProtectFlag' and hasToUpdate:
                        self.blackboard.actualDefender -= 1

                    # Choix d'un but
                    goal = self.goalPlanner.findMostRevelantGoal(bot, self.blackboard)
                    self.blackboard.botsAssignGoal[bot.name] = goal.goalString

                    if goal.goalString == 'ProtectFlag':
                        self.blackboard.actualDefender += 1

                    # Choix du plan
                    plan = self.planPlanner.choosePlan(bot, self.blackboard)
                    self.botsPlan[bot] = plan
                else:
                    # Le plan est de continuer la sequence d'action
                    plan = self.botsPlan[bot]

                # On execute l'action
                action = plan.executePlan()
                action.params['description'] = plan.assignGoal
                self.issue(action.command, bot, action.target, **action.params);

            
    def shutdown(self):
        """Use this function to teardown your bot after the game is over, or perform an
        analysis of the data accumulated during the game."""

        pass

class HidingSquare:
    """Classe representant une case qui est consideree comme une cachette"""
    
    def __init__(self, position):
        """
        kill: nombre de kill fait a la position
        death: nombre de fois qu'un bot est mort a cette position
        position: Vector2 de la case
        botAtPosition: Liste de bots qui sont actuellement sur la case
        """
        self.kill = 0
        self.death = 0
        self.position = position
        self.botAtPosition = []
    
