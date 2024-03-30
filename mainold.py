# --------------------------------- Curse of immortailty -----------------------------------------
# this game will be rpg game, with attack, defence, item, power system
# create a game that have a player and a boss
# the game will allow the user to attack physical, power attack, defence to block the boss attacks, items to help the player with a discryption
# animation if you can do it
# a sentance to open the boss fight
# game will take turns, each with their own turn, the boss might sometimes warned the player about incoming high damage attack from the boss
# UI will be simple, 4 choices (attack, power, defence, item) and each will have their options like lightinings and healing items
# interaction will be with the mouse and keyboard {WASD and space to confirm}
# add save function so if the game will take longer it will be to continue of
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# save will save the current status of battle
# simple turn pace, nothing like speed or any thing change the turnings, only if you exculde weak attacks, it will give +1 move
# user interface would be simple squares
# for attack it would be physical ranging from thing to thing, like for exmaple 15 to 20
# power would have some elemental power, like lighting, healing, buff and debuff, it would cost some stamina points like 8 for example, there is physcial power attack that would consume hp percent, like 6 for example
# defence, that would remove 50% incoming damge
# item would feature these types of items: 1 healing 2 buff 3 debuff 4 damage items like bottle that has a lightining
# upon finsighing the insane mode will unlock
# insane mode second phase will make the boss in rage mode, have a speech and a different theme music, that is being in 2.5 damage and 3 moves, but the boss will have 0.5 health left with 0.7x defence
# insane mode upon complation will unlock the cheatings (infinate health, damage, items)
# the game would feature cheat code if someone doesn't want to play the normal game and want the insane, and also it will unlock infinte cheats (activite with typing 'master control' in cheat box)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# for animation, consider adding a still image and then move it using programming logic, add sounds and visuals to each move
# general classes > player classes > boss classes | don't forget this goes for functions too if they have to do with being specific to something || some functions might need to be defined before classes to usnure the game wouldn't break 
# game will feature insane mode, that will include the boss having two turns, douple damage and defence, boss will be more likely to evade attacks and phase two of the battle that the player didn't account for, the player will have two turns too, when the player win he will get unable cheats like infinte health stamina, items. 
# do not forget to add comments to have a clear way to return to when youre busy
# create classes to help with simlier attributes, use special class when you need it this way you can easily manage your code
# -------------------------------------------------------------------------------------------
# tasks
# skeatch how the game ui would look like {main menu, fight menu}
# make a story board that would suit the game (try not to type alot of lines)
# define game mechanics, physical, defense power, and item usage

# 1- [@] gather recorsecs {for graphics and sprites, collect for the player, boss, items animations if you can find for attacks}{sound and music, gather background music and sounds for attack, power usage, item effect}{fonts, get a font that fit with aesthetic}
# 2- development {set the game loop and inculde how the game will be played}{define main classes and theri realtionsships (not sure what it means)}{code the logic for the game (i. e. attacks) and every action works}{animation and visuals, implement animations and effects}{add background music and sound effect to enhance game experience, add text in a seperate file with Arabic text}
# 3- advanced features {work on insane mode, better if you watcha video about hard diffecility implmentaion on pygame}{save load, don't forget to watch something about this too}{cheat code (spoon)}{langauge switch from enlgish to arabic and reverse}
# 4- testing and debugging {playtest to look for bugs, balancing, and usability}{code reveiw and optimiztion, review for efficiency and readability, optimize performance}
# 6- final touch {polish the game}{documentation}
# -------------------------------------------------------------------------------------------
# tips:
# begin with corre mechanics before moving to advance features like insane mode
# develop in stages, start with playable version and add features later
# vwersion control, use git when you finish the game developement


import pygame
import sys
import random
import json
import arabic_reshaper
import PyInstaller
from bidi.algorithm import get_display

# import images.json
with open('./the-curse-of-immortality/images.json', 'r') as image_json:
    data = json.load(image_json)

main_menu_image = pygame.image.load(data['background'][0]['path'])
captain_avatar = pygame.image.load(data['captain'][0]['path'])



def load_and_scale_image(image_path, target_size):
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, target_size)


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
FPS = 60


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.start()
        self.play()

        self.gameStateManager = GameStateManager('start')
        self.menu = Menu(self.screen, self.gameStateManager, None, None)

        self.states = {'start': self.start, 'menu': self.menu.start_menu, 'play': self.play} # add here game states that would give you states

    def start(self):
        self.screen.blit(main_menu_image, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_2]:
            self.gameStateManager.set_state('menu')
    
    def play(self):
        self.screen.blit(captain_avatar,(200,300))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_3]:
            self.gameStateManager.set_state('play')
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        self.gameStateManager.set_state('menu')

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        self.gameStateManager.set_state('play')
        
            self.states[self.gameStateManager.get_state()]()

            pygame.display.update()
            self.clock.tick(FPS)

class GameStateManager():
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state


class Menu():
    def __init__(self, screen, gameStateManager, settings=None, language=None):
        self.screen = screen
        self.settings = settings
        self.language = language
        self.gameStateManager = gameStateManager

    def display_menu(self):
        self.screen.fill('pink')

    def start_menu(self):
        self.screen.fill('gold')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.gameStateManager.set_state('start')

# class Button():
#     def __init__(self):
#         self.

if __name__ == '__main__':
    game = Game()
    game.run()