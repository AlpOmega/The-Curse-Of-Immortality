import pygame
import sys
import random
import json
import arabic_reshaper
import PyInstaller
from bidi.algorithm import get_display
import logic

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
ICON_WIDTH, ICON_HEIGHT = 70, 70
CHARACTER_WIDTH, CHARACTER_HEIGHT = 200, 200
FPS = 60

START = "start"
PLAY = "play"
MENU = "menu"


with open('./the-curse-of-immortality/images.json', 'r') as image_json:
    data = json.load(image_json)

# system data
main_menu_image = pygame.image.load(data['background'][0]['path'])
start_img_btn = pygame.image.load(data['menu'][0]['path'])

# captain data
captain_avatar = pygame.image.load(data['captain'][0]['path'])
captain_sprite = pygame.image.load(data['captain'][1]['path'])

# hunter data
hunter_sprite = pygame.image.load(data['hunter'][0]['path'])


captain_avatar_mod = pygame.transform.scale(captain_avatar, (ICON_WIDTH, ICON_HEIGHT))
captain_sprite_mod = pygame.transform.scale(captain_sprite, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
hunter_sprite_mod = pygame.transform.scale(hunter_sprite, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
hunter_sprite_flip = pygame.transform.flip(hunter_sprite_mod, True, False)

# fonts
ENGLISH_FONT_PATH = './the-curse-of-immortality/font/english.ttf'
ARABIC_FONT_PATH = './the-curse-of-immortality/font/arabic.ttf'
ENGLISH_FONT_SIZE = 20
ARABIC_FONT_SIZE = 24

english_font = pygame.font.Font(ENGLISH_FONT_PATH, ENGLISH_FONT_SIZE)
arabic_font = pygame.font.Font(ARABIC_FONT_PATH, ARABIC_FONT_SIZE)

current_language = "English"

def render_text(text, x, y, screen):
    if current_language == "English":
        text_surface = english_font.render(text, True, (200, 0, 0))
    else:
        # For Arabic, you might need to reshape and bidi-process the text first
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        text_surface = arabic_font.render(bidi_text, True, (255, 255, 255))
    
    screen.blit(text_surface, (x, y))

class GameState:
    def __init__(self, game):
        self.game = game


    def handle_events(self, events):
        pass

    def update(self):
        pass

    def render(self):
        pass

class StartMenu(GameState):
    def update(self):
        self.game.screen.blit(main_menu_image, (0, 0))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    self.game.change_state(MENU)

class MainMenu(GameState):
    def __init__(self, game):
        self.game = game
        self.start_button = logic.Button(100, 200, start_img_btn)

    def update(self):
        self.game.screen.fill('gold')    
        self.start_button.show(self.game.screen)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.game.change_state(PLAY)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.start_button.is_clicked(mouse_pos):
                    # print('mouse is working')
                    self.game.change_state(PLAY)
                    render_text("boss health:", 400, 400, self.game.screen)
            

class Play(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.captain = logic.Captain(captain_sprite_mod, 100, 150)
        self.hunter = logic.Hunter(hunter_sprite_flip, 500, 150)

    def update(self):
        self.captain.player_sprite(self.game.screen)
        self.hunter.hunter_sprite(self.game.screen)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    self.game.change_state(START)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.states = {
            'start': StartMenu(self),
            'menu': MainMenu(self),
            'play': Play(self)
        }
        self.current_state = self.states[START]

    def change_state(self, state_name):
        self.current_state = self.states[state_name]

    def run(self):
            while True:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                self.current_state.handle_events(events)
                self.current_state.update()
                self.current_state.render()

                pygame.display.flip()
                self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()